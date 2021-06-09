"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("currentuser", "v1", "permissions"),
    module=argus_cli_module
)
def get_current_user_permissions(
    includeInherited: bool = True,
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
    """Get list of permissions which is granted to current user. Result will be sorted by id (ascending). NOTE! Some of these permissions may not be active for the current session, if the session is constrained. (PUBLIC)
    
    :param bool includeInherited: If false, do not include permissions inherited from groups
    :param int limit: Maximum number of values to return
    :param int offset: Skip this number of records
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/currentuser/v1/permissions".format(includeInherited=includeInherited,
        limit=limit,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send includeInherited if the argument was provided, dont send null values
    if includeInherited is not None:
        query_parameters.update({"includeInherited": includeInherited})
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

