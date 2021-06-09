"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module
from requests import Response

log = logging.getLogger(__name__)


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def get_evil_samples(
    customerID: int = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    tlp: str = None,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Searches for evil samples. (PUBLIC)
    
    :param list customerID: Set of customer IDs to limit samples result. 
    :param int startTimestamp: Start of time search period for submission creation date. (default 24 hours before timestamp of request.)
    :param int endTimestamp: End of time search period for submission creation date. (default Timestamp of request.)
    :param list tlp: Set of TLPs to search for. 
    :param int limit: Set this value to set max number of results. (default 25)
    :param int offset: Set this value to skip the first (offset) objects. By default, return result from first object. (default 0)
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/sampledb/v1/sample/search/evil".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        body.update({"customerID": customerID})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send tlp if the argument was provided, dont send null values
    if tlp is not None:
        body.update({"tlp": tlp})

    query_parameters = {}

    log.debug("POST %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.post(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def get_sample(
    sha256: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch sample info identified by SHA256. (PUBLIC)
    
    :param str sha256: SHA256 to identify sample info
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/sampledb/v1/sample/{sha256}".format(sha256=sha256)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def get_sample_aggregated(
    sha256: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch sample aggregated info identified by SHA256. (PUBLIC)
    
    :param str sha256: SHA256 to identify sample aggregated info
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/sampledb/v1/sample/{sha256}/aggregated".format(sha256=sha256)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def get_sample_children(
    sha256: str,
    customerID: int = None,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Get sample children submissions with search defined by query params (PUBLIC)
    
    :param str sha256: SHA256 to identify parent sample
    :param list customerID: Search by customer IDs
    :param int limit: Maximum number of returned results
    :param int offset: Skip a number of results
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/sampledb/v1/sample/{sha256}/children".format(limit=limit,
        sha256=sha256,
        offset=offset,
        customerID=customerID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        query_parameters.update({"customerID": customerID})

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def get_sample_download(
    sha256: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch and download sample by SHA256 (PUBLIC)
    
    :param str sha256: SHA256 to identify sample
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: requests.Response object or dictionary translated from JSON
    """

    route = "/sampledb/v1/sample/{sha256}/download".format(sha256=sha256)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
        'content': None
    }
    if json:
        headers['content'] = 'application/json'

    body = body or {}

    query_parameters = {}

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def get_sample_tags(
    sha256: str,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch tags of sample which sample is identified by SHA256. (PUBLIC)
    
    :param str sha256: SHA256 to identify sample which tags belongs to
    :param int limit: Maximum number of returned results
    :param int offset: Skip a number of results
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/sampledb/v1/sample/{sha256}/tags".format(limit=limit,
        sha256=sha256,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def get_sandbox_pcap(
    sha256: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch and download sandbox pcap by sample SHA256 (PUBLIC)
    
    :param str sha256: SHA256 to identify sample which sandbox pcap belongs to
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: requests.Response object or dictionary translated from JSON
    """

    route = "/sampledb/v1/sample/{sha256}/sandbox/pcap".format(sha256=sha256)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
        'content': None
    }
    if json:
        headers['content'] = 'application/json'

    body = body or {}

    query_parameters = {}

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def get_sandbox_procgraph(
    sha256: str,
    runUUID: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch sandbox procgraph by sample SHA256 and id (PUBLIC)
    
    :param str sha256: SHA256 to identify sample which sandbox procgraph belongs to
    :param str runUUID: Sandbox procgraph ID
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: requests.Response object or dictionary translated from JSON
    """

    route = "/sampledb/v1/sample/{sha256}/sandbox/{runUUID}/procgraph".format(sha256=sha256,
        runUUID=runUUID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
        'content': None
    }
    if json:
        headers['content'] = 'application/json'

    body = body or {}

    query_parameters = {}

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def get_sandbox_runs(
    sha256: str,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch sandbox runs of sample which sample is identified by SHA256. (PUBLIC)
    
    :param str sha256: SHA256 to identify sample which sandbox runs belongs to
    :param int limit: Maximum number of returned results
    :param int offset: Skip a number of results
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/sampledb/v1/sample/{sha256}/sandbox".format(limit=limit,
        sha256=sha256,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def list_submissions_by_sample_id(
    sha256: str,
    customerID: int = None,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Search for submissions with defined by query params (PUBLIC)
    
    :param str sha256: SHA256 to identify sample submissions
    :param list customerID: Search by customer IDs
    :param int limit: Maximum number of returned results
    :param int offset: Skip a number of results
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/sampledb/v1/sample/{sha256}/submission".format(limit=limit,
        sha256=sha256,
        offset=offset,
        customerID=customerID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        query_parameters.update({"customerID": customerID})

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()


@register_command(
    extending=("sampledb", "v1", "sample"),
    module=argus_cli_module
)
def submit(
    customer: str = None,
    tlp: str = None,
    data: str = None,
    clientName: str = None,
    fileName: str = None,
    enableSandboxAnalysis: bool = True,
    allowSandboxInternetAccess: bool = None,
    enableAntivirusScan: bool = True,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Submit a sample for analysis (PUBLIC)
    
    :param str customer: Customer ID or short name of the customer to register this sample to. 
    :param str tlp: TLP level of the sample. 
    :param str data: The sample data. 
    :param str clientName: Name of client application.  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str fileName: Name of submitted file.  => Sanitize by regex [a-zA-Z0-9ÅåØøÆæ_\-\. ]*
    :param bool enableSandboxAnalysis: Enable sandbox analysis of sample. (default true)
    :param bool allowSandboxInternetAccess: Allow internet access to sandbox. (default false)
    :param bool enableAntivirusScan: Enable antivirus scan of sample. (default true)
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/sampledb/v1/sample".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send tlp if the argument was provided, dont send null values
    if tlp is not None:
        body.update({"tlp": tlp})
    # Only send data if the argument was provided, dont send null values
    if data is not None:
        body.update({"data": data})
    # Only send enableSandboxAnalysis if the argument was provided, dont send null values
    if enableSandboxAnalysis is not None:
        body.update({"enableSandboxAnalysis": enableSandboxAnalysis})
    # Only send allowSandboxInternetAccess if the argument was provided, dont send null values
    if allowSandboxInternetAccess is not None:
        body.update({"allowSandboxInternetAccess": allowSandboxInternetAccess})
    # Only send enableAntivirusScan if the argument was provided, dont send null values
    if enableAntivirusScan is not None:
        body.update({"enableAntivirusScan": enableAntivirusScan})
    # Only send clientName if the argument was provided, dont send null values
    if clientName is not None:
        body.update({"clientName": clientName})
    # Only send fileName if the argument was provided, dont send null values
    if fileName is not None:
        body.update({"fileName": fileName})

    query_parameters = {}

    log.debug("POST %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.post(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()

