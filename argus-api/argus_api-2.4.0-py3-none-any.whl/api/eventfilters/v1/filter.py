"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module
from requests import Response

log = logging.getLogger(__name__)


@register_command(
    extending=("eventfilters", "v1", "filter"),
    module=argus_cli_module
)
def error_stats(
    includeDetails: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch filter error statistics (INTERNAL)
    
    :param bool includeDetails: If true, include detailed error statistics per processing node
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

    route = "/eventfilters/v1/filter/errorstats".format(includeDetails=includeDetails)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send includeDetails if the argument was provided, dont send null values
    if includeDetails is not None:
        query_parameters.update({"includeDetails": includeDetails})

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
    extending=("eventfilters", "v1", "filter"),
    module=argus_cli_module
)
def get(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch filter  (INTERNAL)
    
    :param int id: ID of filter to fetch
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
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/eventfilters/v1/filter/{id}".format(id=id)

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
    extending=("eventfilters", "v1", "filter"),
    module=argus_cli_module
)
def hit_stats(
    period: int = 3600000,
    includeDetails: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch filter error statistics (INTERNAL)
    
    :param int period: Time period to fetch hit stats for (milliseconds)
    :param bool includeDetails: If true, include details about hits per processing node
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

    route = "/eventfilters/v1/filter/hitstats".format(period=period,
        includeDetails=includeDetails)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send period if the argument was provided, dont send null values
    if period is not None:
        query_parameters.update({"period": period})
    # Only send includeDetails if the argument was provided, dont send null values
    if includeDetails is not None:
        query_parameters.update({"includeDetails": includeDetails})

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
    extending=("eventfilters", "v1", "filter"),
    module=argus_cli_module
)
def list(
    search: str = None,
    customerID: int = None,
    type: str = None,
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
    """List filters (INTERNAL)
    
    :param str search: Limit result to filters matching this searchstring
    :param list customerID: Limit result to filters for this customerID
    :param str type: Limit result to filters of this type
    :param int limit: Limit result
    :param int offset: Offset result
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

    route = "/eventfilters/v1/filter".format(limit=limit,
        offset=offset,
        search=search,
        customerID=customerID,
        type=type)

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
    # Only send search if the argument was provided, dont send null values
    if search is not None:
        query_parameters.update({"search": search})
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        query_parameters.update({"customerID": customerID})
    # Only send type if the argument was provided, dont send null values
    if type is not None:
        query_parameters.update({"type": type})

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
    extending=("eventfilters", "v1", "filter"),
    module=argus_cli_module
)
def move_filter(
    id: int,
    customer: str = None,
    _global: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Move an eventfilter to another customer (DEV)
    
    :param int id: ID of event filter
    :param str customer: ID or shortname of customer to move filter to. Required unless global is true. 
    :param bool global: Set to true to move filter to a global filter. If true, customer cannot be specified. 
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

    route = "/eventfilters/v1/filter/{id}/move".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send global if the argument was provided, dont send null values
    if _global is not None:
        body.update({"global": _global})

    query_parameters = {}

    log.debug("PUT %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.put(
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
    extending=("eventfilters", "v1", "filter"),
    module=argus_cli_module
)
def revisions(
    id: int,
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
    """Fetch filter revisions by filter ID (INTERNAL)
    
    :param int id: Fetch revisions for filter with this ID
    :param int limit: Limit result
    :param int offset: Offset result
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
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/eventfilters/v1/filter/{id}/revisions".format(limit=limit,
        offset=offset,
        id=id)

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
    extending=("eventfilters", "v1", "filter"),
    module=argus_cli_module
)
def search(
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    includeFlags: int = None,
    excludeFlags: int = None,
    customerID: int = None,
    type: str = None,
    description: str = None,
    searchString: str = None,
    labels: str = None,
    masterID: int = None,
    userID: int = None,
    filterID: int = None,
    associatedCaseID: int = None,
    hitPeriod: int = None,
    minimumHits: int = None,
    maximumHits: int = None,
    includeCreatedTimestamp: bool = None,
    includeLastUpdatedTimestamp: bool = None,
    excludeExpired: bool = None,
    excludeFuture: bool = None,
    excludeValid: bool = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    sortBy: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Search filters (INTERNAL)
    
    :param int limit: Limit results 
    :param int offset: Offset results 
    :param bool includeDeleted: Also include deleted objects (where implemented) 
    :param int includeFlags: Search objects with these flags set 
    :param int excludeFlags: Exclude objects with these flags set 
    :param list customerID: Limit result to objects belonging to these customers 
    :param str type: Limit search to filters of this type 
    :param str description: Match filters by words in description 
    :param str searchString: Match filters by words in entire filter configuration 
    :param list labels: Limit search to filters with any of these filters 
    :param int masterID: Limit search to revisions of this master ID (by default, revisions are excluded) 
    :param list userID: Limit search to filters created/updated by any of these users 
    :param list filterID: Limit search to these spesific filters 
    :param list associatedCaseID: Limit search to filters associated to any of the listed cases. AssociatedCaseID 0 will include filters not associated to a case. 
    :param int hitPeriod: When searching by filter hits, look at hits for this period (previous time period in milliseconds) 
    :param int minimumHits: Limit search to filters reporting at least this number of hits for the hit period (SLOW) 
    :param int maximumHits: Limit search to filters reporting at most this number of hits for the hit period (SLOW) 
    :param bool includeCreatedTimestamp: When limiting filters by time, include filters by created timestamp 
    :param bool includeLastUpdatedTimestamp: When limiting filters by time, include filters by last updated timestamp 
    :param bool excludeExpired: Exclude filters which are expired (validToTimestamp has passed) 
    :param bool excludeFuture: Exclude filters which are not yet active (validFromTimestamp is in the future) 
    :param bool excludeValid: Exclude filters which are currently valid 
    :param int startTimestamp: Search objects from this timestamp 
    :param int endTimestamp: Search objects until this timestamp 
    :param list sortBy: Order results by these properties (prefix with - to sort descending) 
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

    route = "/eventfilters/v1/filter/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        body.update({"customerID": customerID})
    # Only send type if the argument was provided, dont send null values
    if type is not None:
        body.update({"type": type})
    # Only send description if the argument was provided, dont send null values
    if description is not None:
        body.update({"description": description})
    # Only send searchString if the argument was provided, dont send null values
    if searchString is not None:
        body.update({"searchString": searchString})
    # Only send labels if the argument was provided, dont send null values
    if labels is not None:
        body.update({"labels": labels})
    # Only send masterID if the argument was provided, dont send null values
    if masterID is not None:
        body.update({"masterID": masterID})
    # Only send userID if the argument was provided, dont send null values
    if userID is not None:
        body.update({"userID": userID})
    # Only send filterID if the argument was provided, dont send null values
    if filterID is not None:
        body.update({"filterID": filterID})
    # Only send associatedCaseID if the argument was provided, dont send null values
    if associatedCaseID is not None:
        body.update({"associatedCaseID": associatedCaseID})
    # Only send hitPeriod if the argument was provided, dont send null values
    if hitPeriod is not None:
        body.update({"hitPeriod": hitPeriod})
    # Only send minimumHits if the argument was provided, dont send null values
    if minimumHits is not None:
        body.update({"minimumHits": minimumHits})
    # Only send maximumHits if the argument was provided, dont send null values
    if maximumHits is not None:
        body.update({"maximumHits": maximumHits})
    # Only send includeCreatedTimestamp if the argument was provided, dont send null values
    if includeCreatedTimestamp is not None:
        body.update({"includeCreatedTimestamp": includeCreatedTimestamp})
    # Only send includeLastUpdatedTimestamp if the argument was provided, dont send null values
    if includeLastUpdatedTimestamp is not None:
        body.update({"includeLastUpdatedTimestamp": includeLastUpdatedTimestamp})
    # Only send excludeExpired if the argument was provided, dont send null values
    if excludeExpired is not None:
        body.update({"excludeExpired": excludeExpired})
    # Only send excludeFuture if the argument was provided, dont send null values
    if excludeFuture is not None:
        body.update({"excludeFuture": excludeFuture})
    # Only send excludeValid if the argument was provided, dont send null values
    if excludeValid is not None:
        body.update({"excludeValid": excludeValid})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})

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
    extending=("eventfilters", "v1", "filter"),
    module=argus_cli_module
)
def set_log_level(
    id: int,
    level: str = None,
    instanceID: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> Response:
    """Set log level for specified filter (INTERNAL)
    
    :param int id: ID of event filter
    :param str level: Log level to be set for event filter 
    :param int instanceID: ID of component instance to set log level for event filter, if not provided will set across instances 
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
    :raises OperationTimeoutException: on 408
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: requests.Response object
    
    """

    route = "/eventfilters/v1/filter/{id}/logging".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send level if the argument was provided, dont send null values
    if level is not None:
        body.update({"level": level})
    # Only send instanceID if the argument was provided, dont send null values
    if instanceID is not None:
        body.update({"instanceID": instanceID})

    query_parameters = {}

    log.debug("PUT %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.put(
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
    return response
    

