"""Autogenerated API schema"""
from argus_api import session


get_methods = {'tags': ['authentication/v1'], 'summary': 'List authentication methods available on this server (PUBLIC)', 'description': 'Returns a list of authentication methods available on the server. The last successful authentication performed on the client will be returned asmetaData.lastUsedAuthenticationMethod', 'operationId': 'getMethods', 'produces': ['application/json'], 'parameters': [{'name': 'argus_last_method', 'in': 'cookie', 'required': False, 'type': 'string'}], 'responses': {'200': {'description': 'successful operation', 'schema': {'type': 'string', 'enum': ['PASSWORD', 'SIGNATURE', 'SMS', 'RADIUS', 'TOTP', 'OTP', 'APIKEY', 'LDAP', 'IMPERSONATED', 'OPENID']}}}}