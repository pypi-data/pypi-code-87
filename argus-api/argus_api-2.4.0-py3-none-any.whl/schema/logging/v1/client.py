"""Autogenerated API schema"""
from argus_api import session


submit_log_events_bulk = {'tags': ['logging/v1'], 'summary': 'Submit client log events in a bulk operation (DEV)', 'description': '', 'operationId': 'submitLogEventsBulk', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'Client log event bulk submission request', 'required': False, 'schema': {'type': 'object', 'required': ['logEntries'], 'properties': {'logEntries': {'type': 'list', 'position': 0, 'description': 'Log entries for submission. ', 'items': {'type': 'dict', 'required': ['clientBrowser', 'level', 'message', 'originatingPage', 'timestamp'], 'properties': {'timestamp': {'type': 'int', 'position': 0, 'description': 'Timestamp for event. Accepts ISO-8601 timestamp string. ', 'minimum': 1}, 'level': {'type': 'str', 'position': 0, 'description': 'Event level: debug, info, warning or error. ', 'enum': ['none', 'error', 'warning', 'info', 'debug']}, 'stacktrace': {'type': 'str', 'position': 0, 'description': 'Complete stacktrace for event., Max string length is 4096 characters. '}, 'context': {'type': 'dict', 'position': 0, 'description': 'Additional information that could be relevant in the context. ', 'additionalProperties': {'type': 'string'}}, 'message': {'type': 'str', 'position': 0, 'description': 'Event message '}, 'clientBrowser': {'type': 'str', 'position': 0, 'description': 'Browser running client. '}, 'originatingPage': {'type': 'str', 'position': 0, 'description': 'Client page on which the event occurred. '}, 'requestID': {'type': 'str', 'position': 0, 'description': 'RequestID used during event. '}}}, 'maxItems': 2147483647, 'minItems': 1}, 'ignoreOnFailed': {'type': 'bool', 'position': 0, 'description': 'Set this value for successful response even with failures occur while submitting. (default false)', 'default': False}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'accepted': {'type': 'int', 'position': 0, 'description': 'Number of successfully submitted logs. '}, 'rejected': {'type': 'int', 'position': 0, 'description': 'Number of logs that failed validation. '}, 'errorInformationList': {'type': 'list', 'position': 0, 'description': 'Information regarding any logs that are rejected during validation. ', 'items': {'type': 'dict', 'properties': {'logIndex': {'type': 'int', 'position': 0, 'description': 'Index of the log as it appears in the submission request. '}, 'errorMessages': {'type': 'list', 'position': 0, 'description': 'String message of error cause. ', 'items': {'type': 'string'}}}}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '412': {'description': 'Validation failed'}}}