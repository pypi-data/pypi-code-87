"""Autogenerated API"""
from argus_api import session



def call(
    arguments: dict = None,
    method: str = None,
    pattern: dict = None,
    type: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Invoke operation (INTERNAL)
    
    :param list arguments: 
    :param str method: 
    :param dict pattern: 
    :param str type: 
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises RemoteInvocationFailedException: on 409
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/componentadmin/v1/invoke".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send arguments if the argument was provided, dont send null values
    if arguments is not None:
        body.update({"arguments": arguments})
    # Only send method if the argument was provided, dont send null values
    if method is not None:
        body.update({"method": method})
    # Only send pattern if the argument was provided, dont send null values
    if pattern is not None:
        body.update({"pattern": pattern})
    # Only send type if the argument was provided, dont send null values
    if type is not None:
        body.update({"type": type})

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

