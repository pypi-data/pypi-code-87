"""Autogenerated API schema"""
from argus_api import session


lookup_who_is = {'tags': ['world/v1'], 'summary': 'Get WHOIS information by IP or host name (PUBLIC)', 'description': '', 'operationId': 'lookupWhoIs', 'produces': ['application/json'], 'parameters': [{'name': 'lookup', 'in': 'query', 'description': 'Lookup WhoIs information for specified value', 'required': False, 'type': 'str'}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'info': {'type': 'str', 'position': 0, 'description': 'Resolved WHOIS information '}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Not found'}, '412': {'description': 'Validation error'}}}