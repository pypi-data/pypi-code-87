"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("sensors", "v1", "location"),
    module=argus_cli_module
)
def create_location(
    name: str = None,
    shortName: str = None,
    networkZone: str = None,
    customerID: int = None,
    timeZoneDescription: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Creates a location (DEV)
    
    :param str name: Name of some physical location  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str shortName: Short name of some physical location  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str networkZone: Network zone for some physical location 
    :param int customerID: CustomerID for some physical location 
    :param str timeZoneDescription: TimeZone description for some physical location (default Europe/Oslo)
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

    route = "/sensors/v1/location".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send shortName if the argument was provided, dont send null values
    if shortName is not None:
        body.update({"shortName": shortName})
    # Only send networkZone if the argument was provided, dont send null values
    if networkZone is not None:
        body.update({"networkZone": networkZone})
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        body.update({"customerID": customerID})
    # Only send timeZoneDescription if the argument was provided, dont send null values
    if timeZoneDescription is not None:
        body.update({"timeZoneDescription": timeZoneDescription})

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
    extending=("sensors", "v1", "location"),
    module=argus_cli_module
)
def delete_location(
    idOrShortName: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Deletes location (DEV)
    
    :param str idOrShortName: ID or short name of location to delete
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises LocationNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/sensors/v1/location/{idOrShortName}".format(idOrShortName=idOrShortName)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    log.debug("DELETE %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

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


@register_command(
    extending=("sensors", "v1", "location"),
    module=argus_cli_module
)
def find_locations(
    searchString: str = None,
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    subCriteria: dict = None,
    exclude: bool = None,
    required: bool = None,
    customerID: int = None,
    includeFlags: str = None,
    excludeFlags: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Search locations (DEV)
    
    :param str searchString: 
    :param int limit: Set this value to set max number of results. By default, no restriction on result set size. 
    :param int offset: Set this value to skip the first (offset) objects. By default, return result from first object. 
    :param bool includeDeleted: Set to true to include deleted objects. By default, exclude deleted objects. 
    :param list subCriteria: Set additional criterias which are applied using a logical OR. 
    :param bool exclude: Only relevant for subcriteria. If set to true, objects matching this subcriteria object will be excluded. 
    :param bool required: Only relevant for subcriteria. If set to true, objects matching this subcriteria are required (AND-ed together with parent criteria). 
    :param list customerID: Restrict search to data belonging to specified customers. 
    :param list includeFlags: Only include objects which have includeFlags set. 
    :param list excludeFlags: Exclude objects which have excludeFlags set. 
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

    route = "/sensors/v1/location/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send searchString if the argument was provided, dont send null values
    if searchString is not None:
        body.update({"searchString": searchString})
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
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        body.update({"customerID": customerID})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})

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
    extending=("sensors", "v1", "location"),
    module=argus_cli_module
)
def get_location(
    idOrShortName: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Fetch Location by ID or short name (DEV)
    
    :param str idOrShortName: ID or short name of location to fetch
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

    route = "/sensors/v1/location/{idOrShortName}".format(idOrShortName=idOrShortName)

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
    extending=("sensors", "v1", "location"),
    module=argus_cli_module
)
def list_locations(
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
    """List locations (DEV)
    
    :param list customerID: Limit search to these customer IDs
    :param int limit: Limit results
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

    route = "/sensors/v1/location".format(limit=limit,
        customerID=customerID,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        query_parameters.update({"customerID": customerID})
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
    extending=("sensors", "v1", "location"),
    module=argus_cli_module
)
def update_location(
    idOrShortName: str,
    name: str = None,
    shortName: str = None,
    networkZone: str = None,
    timeZoneIdOrName: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Updates location (DEV)
    
    :param str idOrShortName: ID or short name of location to update
    :param str name: Name of some physical location  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str shortName: Short name of some physical location  => Sanitize by regex (?!^\d+$)^[a-z0-9\-]+
    :param str networkZone: Network zone for some physical location 
    :param str timeZoneIdOrName: TimeZone description or ID for some physical location 
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

    route = "/sensors/v1/location/{idOrShortName}".format(idOrShortName=idOrShortName)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send shortName if the argument was provided, dont send null values
    if shortName is not None:
        body.update({"shortName": shortName})
    # Only send networkZone if the argument was provided, dont send null values
    if networkZone is not None:
        body.update({"networkZone": networkZone})
    # Only send timeZoneIdOrName if the argument was provided, dont send null values
    if timeZoneIdOrName is not None:
        body.update({"timeZoneIdOrName": timeZoneIdOrName})

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

