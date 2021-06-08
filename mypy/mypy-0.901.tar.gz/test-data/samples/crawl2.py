#!/usr/bin/env python3.4

"""A simple web crawler."""

# This is cloned from <asyncio>/examples/crawl.py,
# with type annotations added (PEP 484).
#
# This version (crawl2.) has also been converted to use `async def` +
# `await` (PEP 492).

import argparse
import asyncio
import cgi
from http.client import BadStatusLine
import logging
import re
import sys
import time
import urllib.parse
from typing import Any, Awaitable, IO, Optional, Sequence, Set, Tuple, List, Dict


ARGS = argparse.ArgumentParser(description="Web crawler")
ARGS.add_argument(
    '--iocp', action='store_true', dest='iocp',
    default=False, help='Use IOCP event loop (Windows only)')
ARGS.add_argument(
    '--select', action='store_true', dest='select',
    default=False, help='Use Select event loop instead of default')
ARGS.add_argument(
    'roots', nargs='*',
    default=[], help='Root URL (may be repeated)')
ARGS.add_argument(
    '--max_redirect', action='store', type=int, metavar='N',
    default=10, help='Limit redirection chains (for 301, 302 etc.)')
ARGS.add_argument(
    '--max_tries', action='store', type=int, metavar='N',
    default=4, help='Limit retries on network errors')
ARGS.add_argument(
    '--max_tasks', action='store', type=int, metavar='N',
    default=100, help='Limit concurrent connections')
ARGS.add_argument(
    '--max_pool', action='store', type=int, metavar='N',
    default=100, help='Limit connection pool size')
ARGS.add_argument(
    '--exclude', action='store', metavar='REGEX',
    help='Exclude matching URLs')
ARGS.add_argument(
    '--strict', action='store_true',
    default=True, help='Strict host matching (default)')
ARGS.add_argument(
    '--lenient', action='store_false', dest='strict',
    default=False, help='Lenient host matching')
ARGS.add_argument(
    '-v', '--verbose', action='count', dest='level',
    default=1, help='Verbose logging (repeat for more verbose)')
ARGS.add_argument(
    '-q', '--quiet', action='store_const', const=0, dest='level',
    default=1, help='Quiet logging (opposite of --verbose)')


ESCAPES = [('quot', '"'),
           ('gt', '>'),
           ('lt', '<'),
           ('amp', '&')  # Must be last.
           ]


def unescape(url: str) -> str:
    """Turn &amp; into &, and so on.

    This is the inverse of cgi.escape().
    """
    for name, char in ESCAPES:
        url = url.replace('&' + name + ';', char)
    return url


def fix_url(url: str) -> str:
    """Prefix a schema-less URL with http://."""
    if '://' not in url:
        url = 'http://' + url
    return url


class Logger:

    def __init__(self, level: int) -> None:
        self.level = level

    def _log(self, n: int, args: Sequence[Any]) -> None:
        if self.level >= n:
            print(*args, file=sys.stderr, flush=True)

    def log(self, n: int, *args: Any) -> None:
        self._log(n, args)

    def __call__(self, n: int, *args: Any) -> None:
        self._log(n, args)


KeyTuple = Tuple[str, int, bool]


class ConnectionPool:
    """A connection pool.

    To open a connection, use reserve().  To recycle it, use unreserve().

    The pool is mostly just a mapping from (host, port, ssl) tuples to
    lists of Connections.  The currently active connections are *not*
    in the data structure; get_connection() takes the connection out,
    and recycle_connection() puts it back in.  To recycle a
    connection, call conn.close(recycle=True).

    There are limits to both the overall pool and the per-key pool.
    """

    def __init__(self, log: Logger, max_pool: int = 10, max_tasks: int = 5) -> None:
        self.log = log
        self.max_pool = max_pool  # Overall limit.
        self.max_tasks = max_tasks  # Per-key limit.
        self.loop = asyncio.get_event_loop()
        self.connections = {}  # type: Dict[KeyTuple, List[Connection]]
        self.queue = []  # type: List[Connection]

    def close(self) -> None:
        """Close all connections available for reuse."""
        for conns in self.connections.values():
            for conn in conns:
                conn.close()
        self.connections.clear()
        self.queue.clear()

    async def get_connection(self, host: str, port: int, ssl: bool) -> 'Connection':
        """Create or reuse a connection."""
        port = port or (443 if ssl else 80)
        try:
            ipaddrs = await self.loop.getaddrinfo(host, port)
        except Exception as exc:
            self.log(0, 'Exception %r for (%r, %r)' % (exc, host, port))
            raise
        self.log(1, '* %s resolves to %s' %
                    (host, ', '.join(ip[4][0] for ip in ipaddrs)))

        # Look for a reusable connection.
        for _1, _2, _3, _4, (h, p, *_5) in ipaddrs:
            key = h, p, ssl
            conn = None
            conns = self.connections.get(key)
            while conns:
                conn = conns.pop(0)
                self.queue.remove(conn)
                if not conns:
                    del self.connections[key]
                if conn.stale():
                    self.log(1, 'closing stale connection for', key)
                    conn.close()  # Just in case.
                else:
                    self.log(1, '* Reusing pooled connection', key,
                                'FD =', conn.fileno())
                    return conn

        # Create a new connection.
        conn = Connection(self.log, self, host, port, ssl)
        await conn.connect()
        self.log(1, '* New connection', conn.key, 'FD =', conn.fileno())
        return conn

    def recycle_connection(self, conn: 'Connection') -> None:
        """Make a connection available for reuse.

        This also prunes the pool if it exceeds the size limits.
        """
        if conn.stale():
            conn.close()
            return

        key = conn.key
        conns = self.connections.setdefault(key, [])
        conns.append(conn)
        self.queue.append(conn)

        if len(conns) <= self.max_tasks and len(self.queue) <= self.max_pool:
            return

        # Prune the queue.

        # Close stale connections for this key first.
        stale = [conn for conn in conns if conn.stale()]
        if stale:
            for conn in stale:
                conns.remove(conn)
                self.queue.remove(conn)
                self.log(1, 'closing stale connection for', key)
                conn.close()
            if not conns:
                del self.connections[key]

        # Close oldest connection(s) for this key if limit reached.
        while len(conns) > self.max_tasks:
            conn = conns.pop(0)
            self.queue.remove(conn)
            self.log(1, 'closing oldest connection for', key)
            conn.close()

        if len(self.queue) <= self.max_pool:
            return

        # Close overall stale connections.
        stale = [conn for conn in self.queue if conn.stale()]
        if stale:
            for conn in stale:
                conns = self.connections.get(conn.key)
                conns.remove(conn)
                self.queue.remove(conn)
                self.log(1, 'closing stale connection for', key)
                conn.close()

        # Close oldest overall connection(s) if limit reached.
        while len(self.queue) > self.max_pool:
            conn = self.queue.pop(0)
            conns = self.connections.get(conn.key)
            c = conns.pop(0)
            assert conn == c, (conn.key, conn, c, conns)
            self.log(1, 'closing overall oldest connection for', conn.key)
            conn.close()


class Connection:

    def __init__(self, log: Logger, pool: ConnectionPool, host: str, port: int, ssl: bool) -> None:
        self.log = log
        self.pool = pool
        self.host = host
        self.port = port
        self.ssl = ssl
        self.reader = None  # type: asyncio.StreamReader
        self.writer = None  # type: asyncio.StreamWriter
        self.key = None  # type: KeyTuple

    def stale(self) -> bool:
        return self.reader is None or self.reader.at_eof()

    def fileno(self) -> Optional[int]:
        writer = self.writer
        if writer is not None:
            transport = writer.transport
            if transport is not None:
                sock = transport.get_extra_info('socket')
                if sock is not None:
                    return sock.fileno()
        return None

    async def connect(self) -> None:
        self.reader, self.writer = await asyncio.open_connection(
            self.host, self.port, ssl=self.ssl)
        peername = self.writer.get_extra_info('peername')
        if peername:
            self.host, self.port = peername[:2]
        else:
            self.log(1, 'NO PEERNAME???', self.host, self.port, self.ssl)
        self.key = self.host, self.port, self.ssl

    def close(self, recycle: bool = False) -> None:
        if recycle and not self.stale():
            self.pool.recycle_connection(self)
        else:
            self.writer.close()
            self.pool = self.reader = self.writer = None


class Request:
    """HTTP request.

    Use connect() to open a connection; send_request() to send the
    request; get_response() to receive the response headers.
    """

    def __init__(self, log: Logger, url: str, pool: ConnectionPool) -> None:
        self.log = log
        self.url = url
        self.pool = pool
        self.parts = urllib.parse.urlparse(self.url)
        self.scheme = self.parts.scheme
        assert self.scheme in ('http', 'https'), repr(url)
        self.ssl = self.parts.scheme == 'https'
        self.netloc = self.parts.netloc
        self.hostname = self.parts.hostname
        self.port = self.parts.port or (443 if self.ssl else 80)
        self.path = (self.parts.path or '/')
        self.query = self.parts.query
        if self.query:
            self.full_path = '%s?%s' % (self.path, self.query)
        else:
            self.full_path = self.path
        self.http_version = 'HTTP/1.1'
        self.method = 'GET'
        self.headers = []  # type: List[Tuple[str, str]]
        self.conn = None  # type: Connection

    async def connect(self) -> None:
        """Open a connection to the server."""
        self.log(1, '* Connecting to %s:%s using %s for %s' %
                    (self.hostname, self.port,
                     'ssl' if self.ssl else 'tcp',
                     self.url))
        self.conn = await self.pool.get_connection(self.hostname,
                                                        self.port, self.ssl)

    def close(self, recycle: bool = False) -> None:
        """Close the connection, recycle if requested."""
        if self.conn is not None:
            if not recycle:
                self.log(1, 'closing connection for', self.conn.key)
            self.conn.close(recycle)
            self.conn = None

    async def putline(self, line: str) -> None:
        """Write a line to the connection.

        Used for the request line and headers.
        """
        self.log(2, '>', line)
        self.conn.writer.write(line.encode('latin-1') + b'\r\n')

    async def send_request(self) -> None:
        """Send the request."""
        request_line = '%s %s %s' % (self.method, self.full_path,
                                     self.http_version)
        await self.putline(request_line)
        # TODO: What if a header is already set?
        self.headers.append(('User-Agent', 'asyncio-example-crawl/0.0'))
        self.headers.append(('Host', self.netloc))
        self.headers.append(('Accept', '*/*'))
        # self.headers.append(('Accept-Encoding', 'gzip'))
        for key, value in self.headers:
            line = '%s: %s' % (key, value)
            await self.putline(line)
        await self.putline('')

    async def get_response(self) -> 'Response':
        """Receive the response."""
        response = Response(self.log, self.conn.reader)
        await response.read_headers()
        return response


class Response:
    """HTTP response.

    Call read_headers() to receive the request headers.  Then check
    the status attribute and call get_header() to inspect the headers.
    Finally call read() to receive the body.
    """

    def __init__(self, log: Logger, reader: asyncio.StreamReader) -> None:
        self.log = log
        self.reader = reader
        self.http_version = None  # type: str  # 'HTTP/1.1'
        self.status = None  # type: int  # 200
        self.reason = None  # type: str  # 'Ok'
        self.headers = []  # type: List[Tuple[str, str]]  # [('Content-Type', 'text/html')]

    async def getline(self) -> str:
        """Read one line from the connection."""
        line = (await self.reader.readline()).decode('latin-1').rstrip()
        self.log(2, '<', line)
        return line

    async def read_headers(self) -> None:
        """Read the response status and the request headers."""
        status_line = await self.getline()
        status_parts = status_line.split(None, 2)
        if len(status_parts) != 3:
            self.log(0, 'bad status_line', repr(status_line))
            raise BadStatusLine(status_line)
        self.http_version, status, self.reason = status_parts
        self.status = int(status)
        while True:
            header_line = await self.getline()
            if not header_line:
                break
            # TODO: Continuation lines.
            key, value = header_line.split(':', 1)
            self.headers.append((key, value.strip()))

    def get_redirect_url(self, default: str = '') -> str:
        """Inspect the status and return the redirect url if appropriate."""
        if self.status not in (300, 301, 302, 303, 307):
            return default
        return self.get_header('Location', default)

    def get_header(self, key: str, default: str = '') -> str:
        """Get one header value, using a case insensitive header name."""
        key = key.lower()
        for k, v in self.headers:
            if k.lower() == key:
                return v
        return default

    async def read(self) -> bytes:
        """Read the response body.

        This honors Content-Length and Transfer-Encoding: chunked.
        """
        nbytes = None
        for key, value in self.headers:
            if key.lower() == 'content-length':
                nbytes = int(value)
                break
        if nbytes is None:
            if self.get_header('transfer-encoding').lower() == 'chunked':
                self.log(2, 'parsing chunked response')
                blocks = []
                while True:
                    size_header = await self.reader.readline()
                    if not size_header:
                        self.log(0, 'premature end of chunked response')
                        break
                    self.log(3, 'size_header =', repr(size_header))
                    parts = size_header.split(b';')
                    size = int(parts[0], 16)
                    if size:
                        self.log(3, 'reading chunk of', size, 'bytes')
                        block = await self.reader.readexactly(size)
                        assert len(block) == size, (len(block), size)
                        blocks.append(block)
                    crlf = await self.reader.readline()
                    assert crlf == b'\r\n', repr(crlf)
                    if not size:
                        break
                body = b''.join(blocks)
                self.log(1, 'chunked response had', len(body),
                            'bytes in', len(blocks), 'blocks')
            else:
                self.log(3, 'reading until EOF')
                body = await self.reader.read()
                # TODO: Should make sure not to recycle the connection
                # in this case.
        else:
            body = await self.reader.readexactly(nbytes)
        return body


class Fetcher:
    """Logic and state for one URL.

    When found in crawler.busy, this represents a URL to be fetched or
    in the process of being fetched; when found in crawler.done, this
    holds the results from fetching it.

    This is usually associated with a task.  This references the
    crawler for the connection pool and to add more URLs to its todo
    list.

    Call fetch() to do the fetching, then report() to print the results.
    """

    def __init__(self, log: Logger, url: str, crawler: 'Crawler',
                 max_redirect: int = 10, max_tries: int = 4) -> None:
        self.log = log
        self.url = url
        self.crawler = crawler
        # We don't loop resolving redirects here -- we just use this
        # to decide whether to add the redirect URL to crawler.todo.
        self.max_redirect = max_redirect
        # But we do loop to retry on errors a few times.
        self.max_tries = max_tries
        # Everything we collect from the response goes here.
        self.task = None  # type: asyncio.Task
        self.exceptions = []  # type: List[Exception]
        self.tries = 0
        self.request = None  # type: Request
        self.response = None  # type: Response
        self.body = None  # type: bytes
        self.next_url = None  # type: str
        self.ctype = None  # type: str
        self.pdict = None  # type: Dict[str, str]
        self.encoding = None  # type: str
        self.urls = None  # type: Set[str]
        self.new_urls = None  # type: Set[str]

    async def fetch(self) -> None:
        """Attempt to fetch the contents of the URL.

        If successful, and the data is HTML, extract further links and
        add them to the crawler.  Redirects are also added back there.
        """
        while self.tries < self.max_tries:
            self.tries += 1
            self.request = None
            try:
                self.request = Request(self.log, self.url, self.crawler.pool)
                await self.request.connect()
                await self.request.send_request()
                self.response = await self.request.get_response()
                self.body = await self.response.read()
                h_conn = self.response.get_header('connection').lower()
                if h_conn != 'close':
                    self.request.close(recycle=True)
                    self.request = None
                if self.tries > 1:
                    self.log(1, 'try', self.tries, 'for', self.url, 'success')
                break
            except (BadStatusLine, OSError) as exc:
                self.exceptions.append(exc)
                self.log(1, 'try', self.tries, 'for', self.url,
                            'raised', repr(exc))
                # import pdb; pdb.set_trace()
                # Don't reuse the connection in this case.
            finally:
                if self.request is not None:
                    self.request.close()
        else:
            # We never broke out of the while loop, i.e. all tries failed.
            self.log(0, 'no success for', self.url,
                        'in', self.max_tries, 'tries')
            return
        next_url = self.response.get_redirect_url()
        if next_url:
            self.next_url = urllib.parse.urljoin(self.url, next_url)
            if self.max_redirect > 0:
                self.log(1, 'redirect to', self.next_url, 'from', self.url)
                self.crawler.add_url(self.next_url, self.max_redirect - 1)
            else:
                self.log(0, 'redirect limit reached for', self.next_url,
                            'from', self.url)
        else:
            if self.response.status == 200:
                self.ctype = self.response.get_header('content-type')
                self.pdict = {}
                if self.ctype:
                    self.ctype, self.pdict = cgi.parse_header(self.ctype)
                self.encoding = self.pdict.get('charset', 'utf-8')
                if self.ctype == 'text/html':
                    body = self.body.decode(self.encoding, 'replace')
                    # Replace href with (?:href|src) to follow image links.
                    self.urls = set(re.findall(r'(?i)href=["\']?([^\s"\'<>]+)',
                                               body))
                    if self.urls:
                        self.log(1, 'got', len(self.urls),
                                    'distinct urls from', self.url)
                    self.new_urls = set()
                    for url in self.urls:
                        url = unescape(url)
                        url = urllib.parse.urljoin(self.url, url)
                        url, frag = urllib.parse.urldefrag(url)
                        if self.crawler.add_url(url):
                            self.new_urls.add(url)

    def report(self, stats: 'Stats', file: IO[str] = None) -> None:
        """Print a report on the state for this URL.

        Also update the Stats instance.
        """
        if self.task is not None:
            if not self.task.done():
                stats.add('pending')
                print(self.url, 'pending', file=file)
                return
            elif self.task.cancelled():
                stats.add('cancelled')
                print(self.url, 'cancelled', file=file)
                return
            elif self.task.exception():
                stats.add('exception')
                exc = self.task.exception()
                stats.add('exception_' + exc.__class__.__name__)
                print(self.url, exc, file=file)
                return
        if len(self.exceptions) == self.tries:
            stats.add('fail')
            exc = self.exceptions[-1]
            stats.add('fail_' + str(exc.__class__.__name__))
            print(self.url, 'error', exc, file=file)
        elif self.next_url:
            stats.add('redirect')
            print(self.url, self.response.status, 'redirect', self.next_url,
                  file=file)
        elif self.ctype == 'text/html':
            stats.add('html')
            size = len(self.body or b'')
            stats.add('html_bytes', size)
            if self.log.level:
                print(self.url, self.response.status,
                      self.ctype, self.encoding,
                      size,
                      '%d/%d' % (len(self.new_urls or ()), len(self.urls or ())),
                      file=file)
        elif self.response is None:
            print(self.url, 'no response object')
        else:
            size = len(self.body or b'')
            if self.response.status == 200:
                stats.add('other')
                stats.add('other_bytes', size)
            else:
                stats.add('error')
                stats.add('error_bytes', size)
                stats.add('status_%s' % self.response.status)
            print(self.url, self.response.status,
                  self.ctype, self.encoding,
                  size,
                  file=file)


class Stats:
    """Record stats of various sorts."""

    def __init__(self) -> None:
        self.stats = {}  # type: Dict[str, int]

    def add(self, key: str, count: int = 1) -> None:
        self.stats[key] = self.stats.get(key, 0) + count

    def report(self, file: IO[str] = None) -> None:
        for key, count in sorted(self.stats.items()):
            print('%10d' % count, key, file=file)


class Crawler:
    """Crawl a set of URLs.

    This manages three disjoint sets of URLs (todo, busy, done).  The
    data structures actually store dicts -- the values in todo give
    the redirect limit, while the values in busy and done are Fetcher
    instances.
    """
    def __init__(self, log: Logger,
                 roots: Set[str], exclude: str = None, strict: bool = True,  # What to crawl.
                 max_redirect: int = 10, max_tries: int = 4,  # Per-url limits.
                 max_tasks: int = 10, max_pool: int = 10,  # Global limits.
                 ) -> None:
        self.log = log
        self.roots = roots
        self.exclude = exclude
        self.strict = strict
        self.max_redirect = max_redirect
        self.max_tries = max_tries
        self.max_tasks = max_tasks
        self.max_pool = max_pool
        self.todo = {}  # type: Dict[str, int]
        self.busy = {}  # type: Dict[str, Fetcher]
        self.done = {}  # type: Dict[str, Fetcher]
        self.pool = ConnectionPool(self.log, max_pool, max_tasks)
        self.root_domains = set()  # type: Set[str]
        for root in roots:
            host = urllib.parse.urlparse(root).hostname
            if not host:
                continue
            if re.match(r'\A[\d\.]*\Z', host):
                self.root_domains.add(host)
            else:
                host = host.lower()
                if self.strict:
                    self.root_domains.add(host)
                    if host.startswith('www.'):
                        self.root_domains.add(host[4:])
                    else:
                        self.root_domains.add('www.' + host)
                else:
                    parts = host.split('.')
                    if len(parts) > 2:
                        host = '.'.join(parts[-2:])
                    self.root_domains.add(host)
        for root in roots:
            self.add_url(root)
        self.governor = asyncio.Semaphore(max_tasks)
        self.termination = asyncio.Condition()
        self.t0 = time.time()
        self.t1 = None  # type: Optional[float]

    def close(self) -> None:
        """Close resources (currently only the pool)."""
        self.pool.close()

    def host_okay(self, host: str) -> bool:
        """Check if a host should be crawled.

        A literal match (after lowercasing) is always good.  For hosts
        that don't look like IP addresses, some approximate matches
        are okay depending on the strict flag.
        """
        host = host.lower()
        if host in self.root_domains:
            return True
        if re.match(r'\A[\d\.]*\Z', host):
            return False
        if self.strict:
            return self._host_okay_strictish(host)
        else:
            return self._host_okay_lenient(host)

    def _host_okay_strictish(self, host: str) -> bool:
        """Check if a host should be crawled, strict-ish version.

        This checks for equality modulo an initial 'www.' component.
         """
        if host.startswith('www.'):
            if host[4:] in self.root_domains:
                return True
        else:
            if 'www.' + host in self.root_domains:
                return True
        return False

    def _host_okay_lenient(self, host: str) -> bool:
        """Check if a host should be crawled, lenient version.

        This compares the last two components of the host.
        """
        parts = host.split('.')
        if len(parts) > 2:
            host = '.'.join(parts[-2:])
        return host in self.root_domains

    def add_url(self, url: str, max_redirect: int = None) -> bool:
        """Add a URL to the todo list if not seen before."""
        if self.exclude and re.search(self.exclude, url):
            return False
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme not in ('http', 'https'):
            self.log(2, 'skipping non-http scheme in', url)
            return False
        host = parsed.hostname
        if not self.host_okay(host):
            self.log(2, 'skipping non-root host in', url)
            return False
        if max_redirect is None:
            max_redirect = self.max_redirect
        if url in self.todo or url in self.busy or url in self.done:
            return False
        self.log(1, 'adding', url, max_redirect)
        self.todo[url] = max_redirect
        return True

    async def crawl(self) -> None:
        """Run the crawler until all finished."""
        with (await self.termination):
            while self.todo or self.busy:
                if self.todo:
                    url, max_redirect = self.todo.popitem()
                    fetcher = Fetcher(self.log, url,
                                      crawler=self,
                                      max_redirect=max_redirect,
                                      max_tries=self.max_tries,
                                      )
                    self.busy[url] = fetcher
                    fetcher.task = asyncio.Task(self.fetch(fetcher))
                else:
                    await self.termination.wait()
        self.t1 = time.time()

    async def fetch(self, fetcher: Fetcher) -> None:
        """Call the Fetcher's fetch(), with a limit on concurrency.

        Once this returns, move the fetcher from busy to done.
        """
        url = fetcher.url
        with (await self.governor):
            try:
                await fetcher.fetch()  # Fetcher gonna fetch.
            finally:
                # Force GC of the task, so the error is logged.
                fetcher.task = None
        with (await self.termination):
            self.done[url] = fetcher
            del self.busy[url]
            self.termination.notify()

    def report(self, file: IO[str] = None) -> None:
        """Print a report on all completed URLs."""
        if self.t1 is None:
            self.t1 = time.time()
        dt = self.t1 - self.t0
        if dt and self.max_tasks:
            speed = len(self.done) / dt / self.max_tasks
        else:
            speed = 0
        stats = Stats()
        print('*** Report ***', file=file)
        try:
            show = []  # type: List[Tuple[str, Fetcher]]
            show.extend(self.done.items())
            show.extend(self.busy.items())
            show.sort()
            for url, fetcher in show:
                fetcher.report(stats, file=file)
        except KeyboardInterrupt:
            print('\nInterrupted', file=file)
        print('Finished', len(self.done),
              'urls in %.3f secs' % dt,
              '(max_tasks=%d)' % self.max_tasks,
              '(%.3f urls/sec/task)' % speed,
              file=file)
        stats.report(file=file)
        print('Todo:', len(self.todo), file=file)
        print('Busy:', len(self.busy), file=file)
        print('Done:', len(self.done), file=file)
        print('Date:', time.ctime(), 'local time', file=file)


def main() -> None:
    """Main program.

    Parse arguments, set up event loop, run crawler, print report.
    """
    args = ARGS.parse_args()
    if not args.roots:
        print('Use --help for command line help')
        return

    log = Logger(args.level)

    if args.iocp:
        if sys.platform == 'win32':
            from asyncio import ProactorEventLoop
            loop = ProactorEventLoop()  # type: ignore
            asyncio.set_event_loop(loop)
        else:
            assert False
    elif args.select:
        loop = asyncio.SelectorEventLoop()  # type: ignore
        asyncio.set_event_loop(loop)
    else:
        loop = asyncio.get_event_loop()  # type: ignore

    roots = {fix_url(root) for root in args.roots}

    crawler = Crawler(log,
                      roots, exclude=args.exclude,
                      strict=args.strict,
                      max_redirect=args.max_redirect,
                      max_tries=args.max_tries,
                      max_tasks=args.max_tasks,
                      max_pool=args.max_pool,
                      )
    try:
        loop.run_until_complete(crawler.crawl())  # Crawler gonna crawl.
    except KeyboardInterrupt:
        sys.stderr.flush()
        print('\nInterrupted\n')
    finally:
        crawler.report()
        crawler.close()
        loop.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # type: ignore
    main()
