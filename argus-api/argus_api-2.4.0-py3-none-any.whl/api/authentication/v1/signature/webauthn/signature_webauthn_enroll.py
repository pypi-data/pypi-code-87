"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("authentication", "v1", "signature", "webauthn", "enroll"),
    module=argus_cli_module
)
def get_webauthn_create_options(
    fqdn: str = "portal.mnemonic.no",
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Request parameters for enrolling new public key (DEV)
    
    :param str fqdn: The domain which the webauthn credentials will be bound to:param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/authentication/v1/signature/webauthn/enroll".format(fqdn=fqdn)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send fqdn if the argument was provided, dont send null values
    if fqdn is not None:
        query_parameters.update({"fqdn": fqdn})

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers
    )
    return response.json()

