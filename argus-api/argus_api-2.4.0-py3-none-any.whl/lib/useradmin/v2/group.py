"""Autogenerated API"""
from argus_api import session



def add_group(
    customer: str = None,
    shortName: str = None,
    name: str = None,
    description: str = None,
    daemonAccount: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Add new Group (PUBLIC)
    
    :param str customer: The shortname or ID for customer to register the subject to 
    :param str shortName: The shortname of the subject  => Sanitize by regex [a-zA-Z0-9_\-\.@]+
    :param str name: The name of the subject  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str description: The description of the subject  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param bool daemonAccount: If set, mark the group as a group for daemon accounts (default false)
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

    route = "/useradmin/v2/group".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send shortName if the argument was provided, dont send null values
    if shortName is not None:
        body.update({"shortName": shortName})
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send description if the argument was provided, dont send null values
    if description is not None:
        body.update({"description": description})
    # Only send daemonAccount if the argument was provided, dont send null values
    if daemonAccount is not None:
        body.update({"daemonAccount": daemonAccount})

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



def add_group_members(
    shortNameOrID: str,
    domain: str = None,
    subject: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Adds a set of subjects to a group (PUBLIC)
    
    :param str shortNameOrID: Short name or ID of group
    :param str domain: Name or ID of the domain of the group
    :param list subject: ID or shortname of subjects to add to the group 
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

    route = "/useradmin/v2/group/{shortNameOrID}/members".format(shortNameOrID=shortNameOrID,
        domain=domain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        body.update({"subject": subject})

    query_parameters = {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})

    

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



def delete_group(
    shortNameOrID: str,
    domain: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Deletes a group (PUBLIC)
    
    :param str shortNameOrID: Short name or ID of group
    :param str domain: Name or ID of the domain of the group
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

    route = "/useradmin/v2/group/{shortNameOrID}".format(shortNameOrID=shortNameOrID,
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



def get_group(
    shortNameOrID: str,
    domain: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Get a group (PUBLIC)
    
    :param str shortNameOrID: Short name or ID of group
    :param str domain: Name or ID of the domain of the group
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

    route = "/useradmin/v2/group/{shortNameOrID}".format(shortNameOrID=shortNameOrID,
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



def list_groups_1(
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
    """Returns the groups matching the query (DEV)
    
    :param list domain: Domain to search in by short name or id
    :param list subject: Subject to search for by short name or id
    :param list customer: Customer to search for by short name or id
    :param list excludeFlag: Exclude groups with flag
    :param list includeFlag: Include groups with flag
    :param list keyword: Search by keywords
    :param list keywordField: Set field strategy for keyword search
    :param list sortBy: Field to sort by
    :param int limit: Maximum number of returned results
    :param str keywordMatch: Set match strategy for keyword search
    :param int offset: Skip a number of results
    :param bool includeDeleted: Include deleted groups
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

    route = "/useradmin/v2/group".format(limit=limit,
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



def list_permissions_for_group(
    shortNameOrID: str,
    domain: str = None,
    limit: int = 25,
    includeInherited: bool = True,
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
    """List permissions for a group (PUBLIC)
    
    :param str shortNameOrID: Short name or ID of group
    :param str domain: Name or ID of the domain of the group
    :param int limit: Maximum number of returned results
    :param bool includeInherited: Include inherited permission
    :param int offset: Skip a number of results
    :param bool includeDeleted: Include deleted permission
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

    route = "/useradmin/v2/group/{shortNameOrID}/permissions".format(limit=limit,
        includeInherited=includeInherited,
        shortNameOrID=shortNameOrID,
        domain=domain,
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
    # Only send includeInherited if the argument was provided, dont send null values
    if includeInherited is not None:
        query_parameters.update({"includeInherited": includeInherited})
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})
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



def list_subjects_in_group(
    shortNameOrID: str,
    domain: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetches the set of active members of a group (PUBLIC)
    
    :param str shortNameOrID: Short name or ID of group
    :param str domain: Name or ID of the domain of the group
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

    route = "/useradmin/v2/group/{shortNameOrID}/members".format(shortNameOrID=shortNameOrID,
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



def move_group(
    shortNameOrID: str,
    domain: str = None,
    customer: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Move a group to another customer (DEV)
    
    :param str shortNameOrID: Short name or ID of group
    :param str domain: Domain ID or short name (optional, defaults to current user domain)
    :param str customer: ID or shortname of customer to move the subject to. The customer must be in same domain as the subject. 
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

    route = "/useradmin/v2/group/{shortNameOrID}/move".format(shortNameOrID=shortNameOrID,
        domain=domain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})

    query_parameters = {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})

    

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



def reenable_group(
    shortNameOrID: str,
    domain: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Reenables a deleted group (PUBLIC)
    
    :param str shortNameOrID: Short name or ID of group
    :param str domain: Name or ID of the domain of the group
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

    route = "/useradmin/v2/group/{shortNameOrID}/reenable".format(shortNameOrID=shortNameOrID,
        domain=domain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})

    

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



def remove_subjects_from_group(
    shortNameOrID: str,
    subject: str,
    domain: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Removes a set of members from the group (PUBLIC)
    
    :param str shortNameOrID: Short name or ID of group
    :param list subject: Subjects to remove from group
    :param str domain: Name or ID of the domain of the group
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

    route = "/useradmin/v2/group/{shortNameOrID}/members".format(shortNameOrID=shortNameOrID,
        domain=domain,
        subject=subject)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        query_parameters.update({"subject": subject})

    

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



def search_groups(
    domain: str = None,
    subject: str = None,
    ancestor: str = None,
    parent: str = None,
    customer: str = None,
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
    """Returns the groups matching the query (PUBLIC)
    
    :param list domain: Restrict the search to subjects in these domains, by domain ID or name. 
    :param list subject: Restrict search to specific subjects, by ID or shortname 
    :param list ancestor: Restrict search to subjects descending from specific groups, by ID or shortname 
    :param list parent: Restrict search to subjects which are direct member of specific groups, by ID or shortname 
    :param list customer: Restrict search to subjects bound to these customers (by ID or shortname). Customer groups will resolve to all subcustomers as well. 
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

    route = "/useradmin/v2/group/search".format()

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



def update_group(
    shortNameOrID: str,
    domain: str = None,
    shortName: str = None,
    name: str = None,
    description: str = None,
    daemonAccount: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Update a group (PUBLIC)
    
    :param str shortNameOrID: Short name or ID of group
    :param str domain: Name or ID of the domain of the group
    :param str shortName: The shortname of the subject  => Sanitize by regex [a-zA-Z0-9_\-\.@]+
    :param str name: The name of the subject  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str description: The description of the subject  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param bool daemonAccount: If set, change the daemon flag for this group 
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

    route = "/useradmin/v2/group/{shortNameOrID}".format(shortNameOrID=shortNameOrID,
        domain=domain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send shortName if the argument was provided, dont send null values
    if shortName is not None:
        body.update({"shortName": shortName})
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send description if the argument was provided, dont send null values
    if description is not None:
        body.update({"description": description})
    # Only send daemonAccount if the argument was provided, dont send null values
    if daemonAccount is not None:
        body.update({"daemonAccount": daemonAccount})

    query_parameters = {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})

    

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

