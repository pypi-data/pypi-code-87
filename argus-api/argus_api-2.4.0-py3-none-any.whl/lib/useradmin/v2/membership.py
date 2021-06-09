"""Autogenerated API"""
from argus_api import session



def list_memberships(
    subject: str = None,
    limit: int = 25,
    offset: int = None,
    includeDeleted: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """List group memberships (PUBLIC)
    
    :param list subject: Filter out by user or group (by ID or shortname)
    :param int limit: Maximum number of returned results
    :param int offset: Skip a number of results
    :param bool includeDeleted: Include deleted memberships
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

    route = "/useradmin/v2/membership".format(limit=limit,
        subject=subject,
        offset=offset,
        includeDeleted=includeDeleted)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        query_parameters.update({"subject": subject})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        query_parameters.update({"includeDeleted": includeDeleted})

    

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



def search_memberships(
    startTimestamp: int = None,
    endTimestamp: int = None,
    subCriteria: dict = None,
    subject: str = None,
    subjectFieldStrategy: str = None,
    timeFieldStrategy: str = None,
    timeMatchStrategy: str = None,
    customer: str = None,
    domain: str = None,
    sortBy: str = None,
    includeDeleted: bool = None,
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
    """Search for group memberships (PUBLIC)
    
    :param int startTimestamp: 
    :param int endTimestamp: 
    :param list subCriteria: 
    :param list subject: Filter out memberships by subject (by ID or shortname). Se subjectFieldStrategy. 
    :param list subjectFieldStrategy: Determine fields to search for subjects by (defaults to groups and members) 
    :param list timeFieldStrategy: Determine fields to search for subjects by (defaults to groups and members) 
    :param str timeMatchStrategy: Specify if the specified time period must match all the searched time fields, or if it will match for any field. Default is any. 
    :param list customer: Filter out memberships where any of these customers are owning either the group or the member (by ID or shortname) 
    :param str domain: When providing subjects or customers, lookup subjects or customers within this domain. If not specified, subjects and customers will be looked up in the current users domain. 
    :param list sortBy: Field to sort result by (default groupShortName)
    :param bool includeDeleted: Include deleted memberships (default false)
    :param int limit: The max amount of items to display (default 25)
    :param int offset: The amount of items to skip (default 0)
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

    route = "/useradmin/v2/membership/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        body.update({"subject": subject})
    # Only send subjectFieldStrategy if the argument was provided, dont send null values
    if subjectFieldStrategy is not None:
        body.update({"subjectFieldStrategy": subjectFieldStrategy})
    # Only send timeFieldStrategy if the argument was provided, dont send null values
    if timeFieldStrategy is not None:
        body.update({"timeFieldStrategy": timeFieldStrategy})
    # Only send timeMatchStrategy if the argument was provided, dont send null values
    if timeMatchStrategy is not None:
        body.update({"timeMatchStrategy": timeMatchStrategy})
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})

    query_parameters = {}

    

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

