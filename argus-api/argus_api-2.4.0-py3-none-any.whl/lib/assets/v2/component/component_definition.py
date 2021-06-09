"""Autogenerated API"""
from argus_api import session



def add_component_definition(
    domain: str = None,
    shortName: str = None,
    name: str = None,
    type: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Creates a new ComponentDefinition (DEV)
    
    :param str domain: ID or name of domain, if not specified current user domain will be assigned 
    :param str shortName: Component definition short name, required, and unique per domain  => [a-zA-Z0-9_\-\.]*
    :param str name: Component definition name, required  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str type: Type of component definition 
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

    route = "/assets/v2/component/definition".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send shortName if the argument was provided, dont send null values
    if shortName is not None:
        body.update({"shortName": shortName})
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send type if the argument was provided, dont send null values
    if type is not None:
        body.update({"type": type})

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



def delete_component_definition(
    definition: str,
    domain: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Marks a ComponentDefinition as deleted (DEV)
    
    :param str definition: ComponentDefinition ID or short name
    :param str domain: Domain ID or name (default is user's domain), only used when definition is short name
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

    route = "/assets/v2/component/definition/{definition}".format(definition=definition,
        domain=domain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})

    

    response = session.delete(
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



def get_component_definition(
    definition: str,
    domain: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Get ComponentDefinition (DEV)
    
    :param str definition: ComponentDefinition ID or short name
    :param str domain: Domain ID or name (default is user's domain), only used when definition is short name
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

    route = "/assets/v2/component/definition/{definition}".format(definition=definition,
        domain=domain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})

    

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



def search_component_definitions(
    sortBy: str = None,
    definition: str = None,
    domain: str = None,
    type: str = None,
    keywords: str = None,
    keywordFieldStrategy: str = None,
    keywordMatchStrategy: str = None,
    timeFieldStrategy: str = None,
    timeMatchStrategy: str = None,
    subCriteria: dict = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
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
    """Search ComponentDefinitions with specified criteria (DEV)
    
    :param list sortBy: 
    :param list definition: Restrict to specified Component definitions (ID or short name) 
    :param list domain: Restrict to specified domains (domain ID or name) 
    :param list type: Restrict to specified component types 
    :param list keywords: Search for keywords against fields defined by keywordFieldStrategy 
    :param list keywordFieldStrategy: Defines which fields will be searched by keywords (default all supported fields) (default all)
    :param str keywordMatchStrategy: Defines how strict different keywords should be matched (default match all keywords) (default all)
    :param list timeFieldStrategy: Defines which timestamps will be included in the search (default lastUpdatedTimestamp) (default lastUpdatedTimestamp)
    :param str timeMatchStrategy: Defines how strict to match against different timestamps (all/any) using start and end timestamp (default any) (default any)
    :param list subCriteria: Set additional criteria which are applied with logical OR by default 
    :param int startTimestamp: Restrict to a time frame based on the set timeFieldStrategy (start timestamp) (default 0)
    :param int endTimestamp: Restrict to a time frame based on the set timeFieldStrategy (end timestamp) (default 0)
    :param bool includeDeleted: Whether include deleted results (default false)
    :param int limit: Limit maximum amount of results (default 25)
    :param int offset: Skip specified amount of results (default 0)
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

    route = "/assets/v2/component/definition/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})
    # Only send definition if the argument was provided, dont send null values
    if definition is not None:
        body.update({"definition": definition})
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send type if the argument was provided, dont send null values
    if type is not None:
        body.update({"type": type})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send keywordFieldStrategy if the argument was provided, dont send null values
    if keywordFieldStrategy is not None:
        body.update({"keywordFieldStrategy": keywordFieldStrategy})
    # Only send keywordMatchStrategy if the argument was provided, dont send null values
    if keywordMatchStrategy is not None:
        body.update({"keywordMatchStrategy": keywordMatchStrategy})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send timeFieldStrategy if the argument was provided, dont send null values
    if timeFieldStrategy is not None:
        body.update({"timeFieldStrategy": timeFieldStrategy})
    # Only send timeMatchStrategy if the argument was provided, dont send null values
    if timeMatchStrategy is not None:
        body.update({"timeMatchStrategy": timeMatchStrategy})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
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



def search_component_definitions_simplified(
    keywords: str = None,
    keywordField: str = None,
    timeField: str = None,
    definition: str = None,
    domain: str = None,
    type: str = None,
    sortBy: str = None,
    limit: int = 25,
    keywordMatch: str = "all",
    startTimestamp: str = "0",
    endTimestamp: str = "0",
    timeMatch: str = "any",
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Search ComponentDefinitions with specified query parameters (DEV)
    
    :param list keywords: Search by keywords
    :param list keywordField: Set field strategy for keyword search
    :param list timeField: Set field strategy for time range search
    :param list definition: Search by definitions (ID or short name)
    :param list domain: Search by domains (domain ID or name)
    :param list type: Search by component types
    :param list sortBy: Sort search result
    :param int limit: Maximum number of returned results
    :param str keywordMatch: Set match strategy for keyword search
    :param str startTimestamp: Start timestamp for time range search
    :param str endTimestamp: End timestamp for time range search
    :param str timeMatch: Set match strategy for time range search
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
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/assets/v2/component/definition".format(limit=limit,
        keywordMatch=keywordMatch,
        startTimestamp=startTimestamp,
        endTimestamp=endTimestamp,
        timeMatch=timeMatch,
        offset=offset,
        keywords=keywords,
        keywordField=keywordField,
        timeField=timeField,
        definition=definition,
        domain=domain,
        type=type,
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
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        query_parameters.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        query_parameters.update({"endTimestamp": endTimestamp})
    # Only send timeMatch if the argument was provided, dont send null values
    if timeMatch is not None:
        query_parameters.update({"timeMatch": timeMatch})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        query_parameters.update({"keywords": keywords})
    # Only send keywordField if the argument was provided, dont send null values
    if keywordField is not None:
        query_parameters.update({"keywordField": keywordField})
    # Only send timeField if the argument was provided, dont send null values
    if timeField is not None:
        query_parameters.update({"timeField": timeField})
    # Only send definition if the argument was provided, dont send null values
    if definition is not None:
        query_parameters.update({"definition": definition})
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})
    # Only send type if the argument was provided, dont send null values
    if type is not None:
        query_parameters.update({"type": type})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        query_parameters.update({"sortBy": sortBy})

    

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

