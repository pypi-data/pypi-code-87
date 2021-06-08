#
# Copyright (c) 2020-2021 Pinecone Systems Inc. All right reserved.
#
from pinecone.network.zmq.spec import Socket
from pinecone.utils import constants
import random
import socket
import asyncio
from typing import Dict
import zmq
from loguru import logger
from functools import partial
import os

SOCK_ADDR = 4
FAMILY = 0
HOST = 0


def get_dns_hosts(socket_spec: Socket):
    try:
        addrinfo = socket.getaddrinfo(socket_spec.host, socket_spec.port)
        return list(set([sock[SOCK_ADDR][HOST] for sock in addrinfo if sock[FAMILY] == socket.AF_INET]))
    except socket.gaierror:
        return []


class SocketWrapper:

    def __init__(self, socket_spec: Socket, context: zmq.Context, native: bool, disable_loadbalance: bool = False):
        """
        :param socket:
        :param context:
        :param native:
        """
        self.context = context
        self.native = native
        self.socket_spec = socket_spec
        self.socket = None
        self.socket_pool = dict()  # type: Dict[str, zmq.Socket]
        self.socket_q = []  # array for round-robin
        self.num_sockets = 0
        self.sock_q_pos = 0
        self.unused_sockets = set()
        self.socket_ready_event = asyncio.Event()
        self.executor = None  # use default executor
        if native or socket_spec.bind or disable_loadbalance:
            self.socket = self.get_socket(socket_spec)
        else:
            self.init_dns_sockets()

    def init_socket_q(self):
        self.socket_q = list(self.socket_pool.values())
        self.num_sockets = len(self.socket_q)
        if self.num_sockets > 0:
            self.sock_q_pos = random.randint(0, self.num_sockets - 1)
            self.socket_ready_event.set()
        else:
            self.socket_ready_event.clear()

    def init_dns_sockets(self):
        hosts = get_dns_hosts(self.socket_spec)
        for ip in hosts:
            self.socket_pool[ip] = self.get_socket(self.socket_for_host(ip))

        self.init_socket_q()

    async def check_connection(self) -> bool:
        if self.native:
            path = self.socket_spec.get_conn_string(self.native).replace('ipc://', '')
            return os.path.exists(path)
        loop = asyncio.get_event_loop()
        new_dns = await loop.run_in_executor(self.executor, partial(get_dns_hosts, self.socket_spec))
        return len(new_dns) > 0

    def socket_for_host(self, host: str) -> Socket:
        return Socket(self.socket_spec.bind, self.socket_spec.sock_type, self.socket_spec.port, host=host)

    def get_socket(self, socket_spec: Socket) -> zmq.Socket:
        if len(self.unused_sockets) > 0:
            zmq_socket, conn_str = self.unused_sockets.pop()
            zmq_socket.disconnect(conn_str)
        else:
            zmq_socket = socket_spec.zmq(self.context)
            zmq_socket.set_hwm(constants.MAX_MSGS_PENDING)  # needs to be set before bind/connect
            zmq_socket.setsockopt(zmq.RCVBUF, 2 * constants.MAX_MSG_SIZE)
            zmq_socket.setsockopt(zmq.SNDBUF, 2 * constants.MAX_MSG_SIZE)

        conn_str = socket_spec.get_conn_string(self.native)
        if socket_spec.bind:
            zmq_socket.bind(conn_str)
        else:
            zmq_socket.connect(conn_str)

        zmq_socket.setsockopt(zmq.LINGER, 0)
        return zmq_socket

    async def refresh_dns(self):
        loop = asyncio.get_event_loop()
        if not self.socket:  # only run for sockets that need dns load-balancing
            new_dns = await loop.run_in_executor(self.executor, partial(get_dns_hosts, self.socket_spec))

            old_dns = self.socket_pool.keys()

            hosts_to_close = set(old_dns) - set(new_dns)
            hosts_to_open = set(new_dns) - set(old_dns)
            if hosts_to_close or hosts_to_open:
                logger.debug(f"closing {len(hosts_to_close)} sockets, opening {len(hosts_to_open)}")
            for entry in hosts_to_open:
                if len(hosts_to_close) > 0:
                    host_to_disconnect = hosts_to_close.pop()
                    sock_to_recycle = self.socket_pool.pop(host_to_disconnect)

                    sock_to_recycle.disconnect(self.socket_for_host(host_to_disconnect).get_conn_string(self.native))
                    sock_to_recycle.connect(self.socket_for_host(entry).get_conn_string(self.native))
                    self.socket_pool[entry] = sock_to_recycle
                else:
                    new_sock = self.get_socket(self.socket_for_host(entry))
                    self.socket_pool[entry] = new_sock

            for entry in hosts_to_close:
                sock_to_close = self.socket_pool.pop(entry)
                sock_to_close.disconnect(self.socket_for_host(entry).get_conn_string(self.native))
                # connect to the host itself, so messages don't get dropped
                conn_str = self.socket_for_host(self.socket_spec.host).get_conn_string(self.native)
                sock_to_close.connect(conn_str)
                self.unused_sockets.add((sock_to_close, conn_str))
            self.init_socket_q()

    @property
    def next_socket(self):
        self.sock_q_pos = (self.sock_q_pos + 1) % self.num_sockets
        return self.socket_q[self.sock_q_pos]

    async def send(self, data: bytes):
        if self.socket:
            self.socket.send(data)
        else:
            await self.socket_ready_event.wait()
            await self.next_socket.send(data)

    async def recv(self) -> bytes:
        if self.socket:
            return await self.socket.recv()
        await self.socket_ready_event.wait()
        recv_socket = self.next_socket
        return await recv_socket.recv()

    def close(self):
        if self.socket:
            self.socket.close()
        for sock in self.socket_pool.values():
            if not sock.closed:
                sock.close()
        for sock, conn_str in self.unused_sockets:
            if not sock.closed:
                sock.close()

    @property
    def closed(self):
        if self.socket:
            return self.socket.closed
        return any([sock.closed for sock in self.socket_pool.values()])
