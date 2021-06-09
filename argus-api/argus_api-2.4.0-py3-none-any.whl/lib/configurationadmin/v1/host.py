"""Autogenerated API"""
from argus_api import session



def add_comment(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Add a comment to configuration host (INTERNAL)
    
    :param int id: ID of host to comment
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

    route = "/configurationadmin/v1/host/{id}/comment".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    

    response = session.post(
        route,
        params=query_parameters or None,
        data=body or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()



def create_2(
    name: str = None,
    information: str = None,
    properties: dict = None,
    agentUser: str = None,
    preprod: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Create new configuration host (INTERNAL)
    
    :param str name: [a-zA-Z0-9_\-\.]*
    :param str information: [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param dict properties: 
    :param str agentUser: Name or ID of the agent user to associate to this host. 
    :param bool preprod: If true, mark this host as a PREPROD host. (default false)
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

    route = "/configurationadmin/v1/host".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send information if the argument was provided, dont send null values
    if information is not None:
        body.update({"information": information})
    # Only send properties if the argument was provided, dont send null values
    if properties is not None:
        body.update({"properties": properties})
    # Only send agentUser if the argument was provided, dont send null values
    if agentUser is not None:
        body.update({"agentUser": agentUser})
    # Only send preprod if the argument was provided, dont send null values
    if preprod is not None:
        body.update({"preprod": preprod})

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



def delete_1(
    id: int,
    deleteInstances: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Delete configuration host (INTERNAL)
    
    :param int id: ID of host to delete
    :param bool deleteInstances: If true, force deletion of instances for this host first
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

    route = "/configurationadmin/v1/host/{id}".format(id=id,
        deleteInstances=deleteInstances)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send deleteInstances if the argument was provided, dont send null values
    if deleteInstances is not None:
        query_parameters.update({"deleteInstances": deleteInstances})

    

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



def disable_monitoring(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Disable monitoring of configuration host (INTERNAL)
    
    :param int id: ID of host to disable monitoring on
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

    route = "/configurationadmin/v1/host/{id}/monitoring/disable".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    

    response = session.put(
        route,
        params=query_parameters or None,
        data=body or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()



def duplicate_1(
    sourceID: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Duplicate a configuration host (INTERNAL)
    
    :param int sourceID: ID of host to duplicate
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

    route = "/configurationadmin/v1/host/{sourceID}/duplicate".format(sourceID=sourceID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    

    response = session.post(
        route,
        params=query_parameters or None,
        data=body or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()



def duplicate_2(
    hostID: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Create default instances on configuration host (INTERNAL)
    
    :param int hostID: ID of host to add instances to
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

    route = "/configurationadmin/v1/host/{hostID}/setupdefault".format(hostID=hostID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    

    response = session.put(
        route,
        params=query_parameters or None,
        data=body or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()



def enable_monitoring(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Enable monitoring of configuration host (INTERNAL)
    
    :param int id: ID of host to enable monitoring on
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

    route = "/configurationadmin/v1/host/{id}/monitoring/enable".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    

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



def list_2(
    search: str = None,
    orderDesc: bool = None,
    limit: int = 25,
    orderBy: str = "name",
    includeComments: bool = None,
    includeDeleted: bool = None,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """List configuration hosts (INTERNAL)
    
    :param str search: Limit results to hosts matching this searchstring
    :param bool orderDesc: Sort results descending
    :param int limit: Limit results
    :param str orderBy: Sort results
    :param bool includeComments: Include comments in output
    :param bool includeDeleted: Include deleted hosts in results
    :param int offset: Offset results
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

    route = "/configurationadmin/v1/host".format(limit=limit,
        orderBy=orderBy,
        search=search,
        includeComments=includeComments,
        includeDeleted=includeDeleted,
        offset=offset,
        orderDesc=orderDesc)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send orderBy if the argument was provided, dont send null values
    if orderBy is not None:
        query_parameters.update({"orderBy": orderBy})
    # Only send search if the argument was provided, dont send null values
    if search is not None:
        query_parameters.update({"search": search})
    # Only send includeComments if the argument was provided, dont send null values
    if includeComments is not None:
        query_parameters.update({"includeComments": includeComments})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        query_parameters.update({"includeDeleted": includeDeleted})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    # Only send orderDesc if the argument was provided, dont send null values
    if orderDesc is not None:
        query_parameters.update({"orderDesc": orderDesc})

    

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



def schedule_monitoring(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Schedule downtime for configuration host (INTERNAL)
    
    :param int id: ID of host to schedule downtime for
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

    route = "/configurationadmin/v1/host/{id}/monitoring/schedule".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    

    response = session.put(
        route,
        params=query_parameters or None,
        data=body or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()



def search_2(
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    subCriteria: dict = None,
    exclude: bool = None,
    required: bool = None,
    keywords: str = None,
    agentUser: str = None,
    host: str = None,
    inDowntime: bool = None,
    sortBy: str = None,
    includeFlags: str = None,
    excludeFlags: str = None,
    includeComments: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Search configuration hosts (INTERNAL)
    
    :param int limit: Set this value to set max number of results. By default, no restriction on result set size. 
    :param int offset: Set this value to skip the first (offset) objects. By default, return result from first object. 
    :param bool includeDeleted: Set to true to include deleted objects. By default, exclude deleted objects. 
    :param list subCriteria: Set additional criterias which are applied using a logical OR. 
    :param bool exclude: Only relevant for subcriteria. If set to true, objects matching this subcriteria object will be excluded. 
    :param bool required: Only relevant for subcriteria. If set to true, objects matching this subcriteria are required (AND-ed together with parent criteria). 
    :param list keywords: If set, filter hosts matching these keywords. 
    :param list agentUser: If set, limit the search result to hosts which are bound to these agents (id or username) 
    :param list host: If set, filter hosts by ID or hostname. 
    :param bool inDowntime: If true, only return hosts which are in scheduled downtime. If false, exclude. If not set, do not filter. 
    :param list sortBy: List of properties to sort by (prefix with "-" to sort descending). 
    :param list includeFlags: Only include objects which have includeFlags set. 
    :param list excludeFlags: Exclude objects which have excludeFlags set. 
    :param bool includeComments: If true, include comments on returned host configuration objects (default false)
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

    route = "/configurationadmin/v1/host/search".format()

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
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send exclude if the argument was provided, dont send null values
    if exclude is not None:
        body.update({"exclude": exclude})
    # Only send required if the argument was provided, dont send null values
    if required is not None:
        body.update({"required": required})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send includeComments if the argument was provided, dont send null values
    if includeComments is not None:
        body.update({"includeComments": includeComments})
    # Only send agentUser if the argument was provided, dont send null values
    if agentUser is not None:
        body.update({"agentUser": agentUser})
    # Only send host if the argument was provided, dont send null values
    if host is not None:
        body.update({"host": host})
    # Only send inDowntime if the argument was provided, dont send null values
    if inDowntime is not None:
        body.update({"inDowntime": inDowntime})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})

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



def update_1(
    hostID: int,
    id: int = None,
    name: str = None,
    information: str = None,
    properties: dict = None,
    agentUser: str = None,
    preprod: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Update configuration host (INTERNAL)
    
    :param int hostID: ID of host to update
    :param int id: 
    :param str name: [a-zA-Z0-9_\-\.]*
    :param str information: [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param dict properties: 
    :param str agentUser: Name or ID of the agent user to associate to this host. If not set, do not change. 
    :param bool preprod: If set, change the PREPROD flag on this host 
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

    route = "/configurationadmin/v1/host/{hostID}".format(hostID=hostID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send id if the argument was provided, dont send null values
    if id is not None:
        body.update({"id": id})
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send information if the argument was provided, dont send null values
    if information is not None:
        body.update({"information": information})
    # Only send properties if the argument was provided, dont send null values
    if properties is not None:
        body.update({"properties": properties})
    # Only send agentUser if the argument was provided, dont send null values
    if agentUser is not None:
        body.update({"agentUser": agentUser})
    # Only send preprod if the argument was provided, dont send null values
    if preprod is not None:
        body.update({"preprod": preprod})

    query_parameters = {}

    

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



def view(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch configuration host (INTERNAL)
    
    :param int id: ID of host to fetch
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

    route = "/configurationadmin/v1/host/{id}".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    

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

