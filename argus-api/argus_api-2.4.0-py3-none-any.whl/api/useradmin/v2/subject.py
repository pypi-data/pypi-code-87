"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("useradmin", "v2", "subject"),
    module=argus_cli_module
)
def get_subject_1(
    shortNameOrId: str,
    domain: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Returns the specified subject (PUBLIC) (PUBLIC)
    
    :param str shortNameOrId: ID or shortname of subject to fetch
    :param str domain: Domain ID or short name (optional, defaults to current user domain)
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

    route = "/useradmin/v2/subject/{shortNameOrId}".format(shortNameOrId=shortNameOrId,
        domain=domain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})

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
    extending=("useradmin", "v2", "subject"),
    module=argus_cli_module
)
def list_subjects_1(
    domain: str = None,
    subject: str = None,
    customer: str = None,
    excludeFlag: str = None,
    includeFlag: str = None,
    keyword: str = None,
    keywordField: str = None,
    sortBy: str = None,
    limit: int = 25,
    keywordMatch: str = "all",
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
    """Returns the subjects matching the query (PUBLIC)
    
    :param list domain: Domain to search in by short name or id
    :param list subject: Subject to search for by short name or id
    :param list customer: Customer to search for by short name or id
    :param list excludeFlag: Exclude subjects with flag
    :param list includeFlag: Include subjects with flag
    :param list keyword: Search by keywords
    :param list keywordField: Set field strategy for keyword search
    :param list sortBy: Field to sort by
    :param int limit: Maximum number of returned results
    :param str keywordMatch: Set match strategy for keyword search
    :param int offset: Skip a number of results
    :param bool includeDeleted: Include deleted subjects
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

    route = "/useradmin/v2/subject".format(limit=limit,
        keywordMatch=keywordMatch,
        offset=offset,
        domain=domain,
        subject=subject,
        customer=customer,
        includeDeleted=includeDeleted,
        excludeFlag=excludeFlag,
        includeFlag=includeFlag,
        keyword=keyword,
        keywordField=keywordField,
        sortBy=sortBy)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send keywordMatch if the argument was provided, dont send null values
    if keywordMatch is not None:
        query_parameters.update({"keywordMatch": keywordMatch})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        query_parameters.update({"subject": subject})
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        query_parameters.update({"customer": customer})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        query_parameters.update({"includeDeleted": includeDeleted})
    # Only send excludeFlag if the argument was provided, dont send null values
    if excludeFlag is not None:
        query_parameters.update({"excludeFlag": excludeFlag})
    # Only send includeFlag if the argument was provided, dont send null values
    if includeFlag is not None:
        query_parameters.update({"includeFlag": includeFlag})
    # Only send keyword if the argument was provided, dont send null values
    if keyword is not None:
        query_parameters.update({"keyword": keyword})
    # Only send keywordField if the argument was provided, dont send null values
    if keywordField is not None:
        query_parameters.update({"keywordField": keywordField})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        query_parameters.update({"sortBy": sortBy})

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
    extending=("useradmin", "v2", "subject"),
    module=argus_cli_module
)
def search_subjects(
    domain: str = None,
    subject: str = None,
    ancestor: str = None,
    parent: str = None,
    customer: str = None,
    type: str = None,
    sortBy: str = None,
    includeFlags: str = None,
    excludeFlags: str = None,
    permissions: dict = None,
    keywords: str = None,
    keywordMatchStrategy: str = None,
    keywordFieldStrategy: str = None,
    endTimestamp: int = None,
    timeMatchStrategy: str = None,
    timeFieldStrategy: str = None,
    subCriteria: dict = None,
    includeDeleted: bool = None,
    startTimestamp: int = None,
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
    """Returns the subjects matching the query (PUBLIC)
    
    :param list domain: Restrict the search to subjects in these domains, by domain ID or name. 
    :param list subject: Restrict search to specific subjects, by ID or shortname 
    :param list ancestor: Restrict search to subjects descending from specific groups, by ID or shortname 
    :param list parent: Restrict search to subjects which are direct member of specific groups, by ID or shortname 
    :param list customer: Restrict search to subjects bound to these customers (by ID or shortname). Customer groups will resolve to all subcustomers as well. 
    :param str type: Limit search to one type of subject 
    :param list sortBy: Field to sort by (default name)
    :param list includeFlags: Restrict search to subjects having all of the specified flags. 
    :param list excludeFlags: Exclude subjects with these flags from the search. 
    :param list permissions: Limit search to subjects with one of the given permissions 
    :param list keywords: Keywords to search for 
    :param str keywordMatchStrategy: Search based on all keywords (AND), or based on any keyword (OR) (default Match all keywords (AND))
    :param list keywordFieldStrategy: Which fields will be searched for the given keyword (default All supported fields)
    :param int endTimestamp: The end time of the search (default now)
    :param str timeMatchStrategy: Search based on all time-field (AND), or based on any time-field (OR) (default Match any field)
    :param list timeFieldStrategy: The fields to limit the time search to (default All fields)
    :param list subCriteria: Set additional criteria with AND, OR or AND NOT 
    :param bool includeDeleted: Whether or not to include deleted subjects. (default false)
    :param int startTimestamp: The start time of the search (default 0)
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
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/useradmin/v2/subject/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        body.update({"subject": subject})
    # Only send ancestor if the argument was provided, dont send null values
    if ancestor is not None:
        body.update({"ancestor": ancestor})
    # Only send parent if the argument was provided, dont send null values
    if parent is not None:
        body.update({"parent": parent})
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send type if the argument was provided, dont send null values
    if type is not None:
        body.update({"type": type})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})
    # Only send permissions if the argument was provided, dont send null values
    if permissions is not None:
        body.update({"permissions": permissions})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send keywordMatchStrategy if the argument was provided, dont send null values
    if keywordMatchStrategy is not None:
        body.update({"keywordMatchStrategy": keywordMatchStrategy})
    # Only send keywordFieldStrategy if the argument was provided, dont send null values
    if keywordFieldStrategy is not None:
        body.update({"keywordFieldStrategy": keywordFieldStrategy})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send timeMatchStrategy if the argument was provided, dont send null values
    if timeMatchStrategy is not None:
        body.update({"timeMatchStrategy": timeMatchStrategy})
    # Only send timeFieldStrategy if the argument was provided, dont send null values
    if timeFieldStrategy is not None:
        body.update({"timeFieldStrategy": timeFieldStrategy})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
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

