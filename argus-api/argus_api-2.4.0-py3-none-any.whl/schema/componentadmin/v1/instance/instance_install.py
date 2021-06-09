"""Autogenerated API schema"""
from argus_api import session


get_container_performance = {'tags': ['componentadmin/v1'], 'summary': 'Fetch performance details from specified component (INTERNAL)', 'description': '', 'operationId': 'getContainerPerformance', 'produces': ['application/json'], 'parameters': [{'name': 'id', 'in': 'path', 'description': 'ID of instance to fetch performance data from', 'required': True, 'type': 'int'}], 'responses': {'401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '409': {'description': 'Remote invocation failed'}}}
get_instance_status = {'tags': ['componentadmin/v1'], 'summary': 'Fetch status for specified component (INTERNAL)', 'description': '', 'operationId': 'getInstanceStatus', 'produces': ['application/json'], 'parameters': [{'name': 'id', 'in': 'path', 'description': 'ID of host to fetch status for', 'required': True, 'type': 'int'}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'installedInstanceRevision': {'type': 'int'}, 'installedTemplateRevision': {'type': 'int'}, 'status': {'type': 'dict', 'properties': {'identity': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}, 'state': {'type': 'str', 'enum': ['NOT_STARTED', 'INITIALIZING', 'STARTED', 'WARNING', 'STOPPING', 'STOPPED', 'FAILED']}}}, 'templateID': {'type': 'int'}, 'inDowntime': {'type': 'boolean'}, 'templateName': {'type': 'string'}, 'monitored': {'type': 'boolean'}, 'instanceID': {'type': 'int'}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}}}
install = {'tags': ['componentadmin/v1'], 'summary': 'Install configuration for instance (INTERNAL)', 'description': '', 'operationId': 'install', 'produces': ['application/json'], 'parameters': [{'name': 'id', 'in': 'path', 'description': 'ID of instance to install', 'required': True, 'type': 'int'}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '409': {'description': 'Remote invocation failed'}}}
reboot_1 = {'tags': ['componentadmin/v1'], 'summary': 'Reboot runtime instance (INTERNAL)', 'description': '', 'operationId': 'reboot_1', 'produces': ['application/json'], 'parameters': [{'name': 'id', 'in': 'path', 'description': 'ID of instance to reboot', 'required': True, 'type': 'int'}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'id': {'type': 'string'}, 'state': {'type': 'str', 'enum': ['RUNNING', 'DONE', 'EXCEPTION', 'TIMEOUT']}, 'target': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}, 'method': {'type': 'string'}, 'arguments': {'type': 'list', 'items': {'type': 'object'}}, 'result': {'type': 'object'}, 'started': {'type': 'int'}, 'finished': {'type': 'int'}, 'children': {'type': 'list', 'items': {'type': 'dict', 'properties': {'id': {'type': 'string'}, 'state': {'type': 'str', 'enum': ['RUNNING', 'DONE', 'EXCEPTION', 'TIMEOUT']}, 'target': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}, 'method': {'type': 'string'}, 'arguments': {'type': 'list', 'items': {'type': 'object'}}, 'result': {'type': 'object'}, 'started': {'type': 'int'}, 'finished': {'type': 'int'}, 'children': {'type': 'list', 'items': []}}}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '409': {'description': 'Remote invocation failed'}}}
refresh_instance_status = {'tags': ['componentadmin/v1'], 'summary': 'Request specified component to immediately refresh status (INTERNAL)', 'description': '', 'operationId': 'refreshInstanceStatus', 'produces': ['application/json'], 'parameters': [{'name': 'id', 'in': 'path', 'description': 'ID of component to request update from', 'required': True, 'type': 'int'}], 'responses': {'401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '409': {'description': 'Remote invocation failed'}}}
start = {'tags': ['componentadmin/v1'], 'summary': 'Initiate runtime instance (INTERNAL)', 'description': '', 'operationId': 'start', 'produces': ['application/json'], 'parameters': [{'name': 'id', 'in': 'path', 'description': 'ID of instance to start', 'required': True, 'type': 'int'}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'id': {'type': 'string'}, 'state': {'type': 'str', 'enum': ['RUNNING', 'DONE', 'EXCEPTION', 'TIMEOUT']}, 'target': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}, 'method': {'type': 'string'}, 'arguments': {'type': 'list', 'items': {'type': 'object'}}, 'result': {'type': 'object'}, 'started': {'type': 'int'}, 'finished': {'type': 'int'}, 'children': {'type': 'list', 'items': {'type': 'dict', 'properties': {'id': {'type': 'string'}, 'state': {'type': 'str', 'enum': ['RUNNING', 'DONE', 'EXCEPTION', 'TIMEOUT']}, 'target': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}, 'method': {'type': 'string'}, 'arguments': {'type': 'list', 'items': {'type': 'object'}}, 'result': {'type': 'object'}, 'started': {'type': 'int'}, 'finished': {'type': 'int'}, 'children': {'type': 'list', 'items': []}}}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '409': {'description': 'Remote invocation failed'}}}
stop = {'tags': ['componentadmin/v1'], 'summary': 'Shutdown runtime instance (INTERNAL)', 'description': '', 'operationId': 'stop', 'produces': ['application/json'], 'parameters': [{'name': 'id', 'in': 'path', 'description': 'ID of instance to stop', 'required': True, 'type': 'int'}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'id': {'type': 'string'}, 'state': {'type': 'str', 'enum': ['RUNNING', 'DONE', 'EXCEPTION', 'TIMEOUT']}, 'target': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}, 'method': {'type': 'string'}, 'arguments': {'type': 'list', 'items': {'type': 'object'}}, 'result': {'type': 'object'}, 'started': {'type': 'int'}, 'finished': {'type': 'int'}, 'children': {'type': 'list', 'items': {'type': 'dict', 'properties': {'id': {'type': 'string'}, 'state': {'type': 'str', 'enum': ['RUNNING', 'DONE', 'EXCEPTION', 'TIMEOUT']}, 'target': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}, 'method': {'type': 'string'}, 'arguments': {'type': 'list', 'items': {'type': 'object'}}, 'result': {'type': 'object'}, 'started': {'type': 'int'}, 'finished': {'type': 'int'}, 'children': {'type': 'list', 'items': []}}}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '409': {'description': 'Remote invocation failed'}}}
uninstall = {'tags': ['componentadmin/v1'], 'summary': 'Uninstall configuration for instance (INTERNAL)', 'description': '', 'operationId': 'uninstall', 'produces': ['application/json'], 'parameters': [{'name': 'id', 'in': 'path', 'description': 'ID of instance to uninstall', 'required': True, 'type': 'int'}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '409': {'description': 'Remote invocation failed'}}}