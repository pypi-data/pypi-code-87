"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("sampledb", "v1", "submission", "search"),
    module=argus_cli_module
)
def get_submission_by_id(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch submission info identified by id. (PUBLIC)
    
    :param int id: Submission ID
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

    route = "/sampledb/v1/submission/{id}".format(id=id)

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
    extending=("sampledb", "v1", "submission", "search"),
    module=argus_cli_module
)
def search_meta_submissions(
    customerID: int = None,
    tlp: str = None,
    keywords: str = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    includeAnonymousResults: bool = True,
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
    """Search for submissions matching given search criteria (PUBLIC)
    
    :param list customerID: Set of customer IDs containing submissions. If not specified, search will be performed against all accessible customers. 
    :param list tlp: Set of TLPs to search for. If not specified, search will be performed against all TLPs (WHITE, GREEN, AMBER, RED). 
    :param list keywords: A set of keywords matched against the metafields of the submission. 
    :param int startTimestamp: Start of time search period for submission creation date. (default 7 days before timestamp of request.)
    :param int endTimestamp: End of time search period for submission creation date. (default Timestamp of request.)
    :param bool includeAnonymousResults: Whether include anonymous results (default true)
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

    route = "/sampledb/v1/submission/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        body.update({"customerID": customerID})
    # Only send tlp if the argument was provided, dont send null values
    if tlp is not None:
        body.update({"tlp": tlp})
    # Only send includeAnonymousResults if the argument was provided, dont send null values
    if includeAnonymousResults is not None:
        body.update({"includeAnonymousResults": includeAnonymousResults})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})

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

