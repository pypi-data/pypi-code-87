"""Autogenerated API schema"""
from argus_api import session


client_host_asset_scanned = {'tags': ['assets/v1'], 'summary': 'Marks a single Client HostAsset as scanned. The host is identified by the host name, and it must be of type CLIENT. (DEV)', 'description': '', 'operationId': 'clientHostAssetScanned', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'name': 'customerID', 'in': 'path', 'description': 'Customer ID', 'required': True, 'type': 'int', 'minimum': 1}, {'name': 'hostName', 'in': 'path', 'description': 'Name of host asset', 'required': True, 'type': 'str'}, {'in': 'body', 'name': 'body', 'description': 'HostAsset scanned request', 'required': False, 'schema': {'type': 'object', 'required': ['detectedVulnerabilities'], 'properties': {'detectedVulnerabilities': {'type': 'list', 'position': 0, 'description': 'Specify (vulnerabilityID, socket string) objects of detected vulnerabilities. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['vulnerabilityID'], 'properties': {'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Specify vulnerability ID of detected vulnerability '}, 'socket': {'type': 'str', 'position': 0, 'description': 'Specify socket of detected vulnerability (e.g. tcp/80), or omit if vulnerability not related to a socket '}}}}, 'detectedApplications': {'type': 'list', 'position': 0, 'description': 'Specify sockets of detected applications (e.g. tcp/80). ', 'uniqueItems': True, 'items': {'type': 'string'}}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'required': ['ipAddress', 'resultCode'], 'properties': {'ipAddress': {'type': 'dict', 'properties': {'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'multicast': {'type': 'boolean'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}, 'resultCode': {'type': 'str', 'position': 0, 'description': 'Scanned host exists or does not exist in database. ', 'enum': ['HostExists', 'HostNotExists']}, 'hostID': {'type': 'str', 'position': 0, 'description': 'UUID of scanned host if host exists in database. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of scanned host if host exists in database. '}, 'existingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were detected by the scan and already exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of application found in database. '}, 'cpe': {'type': 'str', 'position': 0, 'description': 'CPE of application (might be unknown). ', 'readOnly': True}, 'socket': {'type': 'str', 'position': 0, 'description': 'Socket where application is available as reported by the scanner. ', 'readOnly': True}}}}, 'missingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were NOT detected by the scan but exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of application found in database. '}, 'cpe': {'type': 'str', 'position': 0, 'description': 'CPE of application (might be unknown). ', 'readOnly': True}, 'socket': {'type': 'str', 'position': 0, 'description': 'Socket where application is available as reported by the scanner. ', 'readOnly': True}}}}, 'existingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were detected by the scan and already exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id', 'resolution', 'vulnerabilityID'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of vulnerability found in database. '}, 'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'resolution': {'type': 'str', 'position': 0, 'description': 'Resolution code of vulnerability (might be unresolved). ', 'enum': ['ACCEPTED', 'FALSE_POSITIVE', 'SERVICE_NOT_AVAILABLE', 'NO_LONGER_VULNERABLE', 'UNRESOLVED']}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'missingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were NOT detected by the scan but exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id', 'resolution', 'vulnerabilityID'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of vulnerability found in database. '}, 'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'resolution': {'type': 'str', 'position': 0, 'description': 'Resolution code of vulnerability (might be unresolved). ', 'enum': ['ACCEPTED', 'FALSE_POSITIVE', 'SERVICE_NOT_AVAILABLE', 'NO_LONGER_VULNERABLE', 'UNRESOLVED']}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'notExistingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were detected by the scan but do NOT exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['vulnerabilityID'], 'properties': {'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'operatingSystemCPE': {'type': 'str', 'position': 0, 'description': 'Operating system CPE of scanned host if host exists in database (might be unknown). ', 'readOnly': True}, 'ipAddresses': {'type': 'list', 'position': 0, 'description': 'All IP addresses of scanned host if host exists in database. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}, 'aliases': {'type': 'list', 'position': 0, 'description': 'All aliases of scanned host if host exists in database. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}, 'notExistingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were detected by the scan but do NOT exist in the database. Returns a set of socket strings. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '412': {'description': 'Validation error'}}}
host_asset_bulk_scanned = {'tags': ['assets/v1'], 'summary': 'Marks multiple HostAsset as scanned. (PUBLIC)', 'description': '', 'operationId': 'hostAssetBulkScanned', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'HostAsset bulk scanned request', 'required': False, 'schema': {'type': 'object', 'required': ['customerID', 'scannedIpRanges', 'scannedRequests'], 'properties': {'customerID': {'type': 'int', 'position': 0, 'description': 'Define customer which was scanned. ', 'minimum': 1}, 'scannedRequests': {'type': 'list', 'position': 0, 'description': 'Set of host scan requests. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['detectedVulnerabilities', 'ipAddress'], 'properties': {'detectedVulnerabilities': {'type': 'list', 'position': 0, 'description': 'Specify (vulnerabilityID, socket string) objects of detected vulnerabilities. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['vulnerabilityID'], 'properties': {'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Specify vulnerability ID of detected vulnerability '}, 'socket': {'type': 'str', 'position': 0, 'description': 'Specify socket of detected vulnerability (e.g. tcp/80), or omit if vulnerability not related to a socket '}}}}, 'ipAddress': {'type': 'str', 'position': 0, 'description': 'Specify IP address of scanned host. '}, 'detectedApplications': {'type': 'list', 'position': 0, 'description': 'Specify sockets of detected applications (e.g. tcp/80). ', 'uniqueItems': True, 'items': {'type': 'string'}}}}, 'maxItems': 2147483647, 'minItems': 1}, 'scannedIpRanges': {'type': 'list', 'position': 0, 'description': 'Set of scanned IP address ranges as list of single IPs (1.1.1.1), CIDR networks (1.1.1.0/24) or ranges (1.1.1.1-1.1.1.2) ', 'uniqueItems': True, 'items': {'type': 'string'}}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'missingHosts': {'type': 'list', 'position': 0, 'description': 'List all hosts which were NOT detected by the scan but exist in the database. Returns a set of (UUID, IP address) objects. ', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'id': {'type': 'str'}, 'ipAddress': {'type': 'dict', 'properties': {'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'multicast': {'type': 'boolean'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}}}}, 'scannedResponses': {'type': 'list', 'position': 0, 'description': 'Set of host scanned responses. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['ipAddress', 'resultCode'], 'properties': {'ipAddress': {'type': 'dict', 'properties': {'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'multicast': {'type': 'boolean'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}, 'resultCode': {'type': 'str', 'position': 0, 'description': 'Scanned host exists or does not exist in database. ', 'enum': ['HostExists', 'HostNotExists']}, 'hostID': {'type': 'str', 'position': 0, 'description': 'UUID of scanned host if host exists in database. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of scanned host if host exists in database. '}, 'existingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were detected by the scan and already exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of application found in database. '}, 'cpe': {'type': 'str', 'position': 0, 'description': 'CPE of application (might be unknown). ', 'readOnly': True}, 'socket': {'type': 'str', 'position': 0, 'description': 'Socket where application is available as reported by the scanner. ', 'readOnly': True}}}}, 'missingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were NOT detected by the scan but exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of application found in database. '}, 'cpe': {'type': 'str', 'position': 0, 'description': 'CPE of application (might be unknown). ', 'readOnly': True}, 'socket': {'type': 'str', 'position': 0, 'description': 'Socket where application is available as reported by the scanner. ', 'readOnly': True}}}}, 'existingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were detected by the scan and already exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id', 'resolution', 'vulnerabilityID'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of vulnerability found in database. '}, 'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'resolution': {'type': 'str', 'position': 0, 'description': 'Resolution code of vulnerability (might be unresolved). ', 'enum': ['ACCEPTED', 'FALSE_POSITIVE', 'SERVICE_NOT_AVAILABLE', 'NO_LONGER_VULNERABLE', 'UNRESOLVED']}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'missingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were NOT detected by the scan but exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id', 'resolution', 'vulnerabilityID'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of vulnerability found in database. '}, 'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'resolution': {'type': 'str', 'position': 0, 'description': 'Resolution code of vulnerability (might be unresolved). ', 'enum': ['ACCEPTED', 'FALSE_POSITIVE', 'SERVICE_NOT_AVAILABLE', 'NO_LONGER_VULNERABLE', 'UNRESOLVED']}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'notExistingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were detected by the scan but do NOT exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['vulnerabilityID'], 'properties': {'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'operatingSystemCPE': {'type': 'str', 'position': 0, 'description': 'Operating system CPE of scanned host if host exists in database (might be unknown). ', 'readOnly': True}, 'ipAddresses': {'type': 'list', 'position': 0, 'description': 'All IP addresses of scanned host if host exists in database. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}, 'aliases': {'type': 'list', 'position': 0, 'description': 'All aliases of scanned host if host exists in database. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}, 'notExistingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were detected by the scan but do NOT exist in the database. Returns a set of socket strings. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}}}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '412': {'description': 'Validation error'}}}
host_asset_scanned = {'tags': ['assets/v1'], 'summary': 'Marks a single HostAsset as scanned. (PUBLIC)', 'description': '', 'operationId': 'hostAssetScanned', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'name': 'customerID', 'in': 'path', 'description': 'Customer ID', 'required': True, 'type': 'int', 'minimum': 1}, {'name': 'ip', 'in': 'path', 'description': 'IP address of scanned HostAsset', 'required': True, 'type': 'str'}, {'in': 'body', 'name': 'body', 'description': 'HostAsset scanned request', 'required': False, 'schema': {'type': 'object', 'required': ['detectedVulnerabilities'], 'properties': {'detectedVulnerabilities': {'type': 'list', 'position': 0, 'description': 'Specify (vulnerabilityID, socket string) objects of detected vulnerabilities. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['vulnerabilityID'], 'properties': {'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Specify vulnerability ID of detected vulnerability '}, 'socket': {'type': 'str', 'position': 0, 'description': 'Specify socket of detected vulnerability (e.g. tcp/80), or omit if vulnerability not related to a socket '}}}}, 'detectedApplications': {'type': 'list', 'position': 0, 'description': 'Specify sockets of detected applications (e.g. tcp/80). ', 'uniqueItems': True, 'items': {'type': 'string'}}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'required': ['ipAddress', 'resultCode'], 'properties': {'ipAddress': {'type': 'dict', 'properties': {'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'multicast': {'type': 'boolean'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}, 'resultCode': {'type': 'str', 'position': 0, 'description': 'Scanned host exists or does not exist in database. ', 'enum': ['HostExists', 'HostNotExists']}, 'hostID': {'type': 'str', 'position': 0, 'description': 'UUID of scanned host if host exists in database. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of scanned host if host exists in database. '}, 'existingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were detected by the scan and already exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of application found in database. '}, 'cpe': {'type': 'str', 'position': 0, 'description': 'CPE of application (might be unknown). ', 'readOnly': True}, 'socket': {'type': 'str', 'position': 0, 'description': 'Socket where application is available as reported by the scanner. ', 'readOnly': True}}}}, 'missingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were NOT detected by the scan but exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of application found in database. '}, 'cpe': {'type': 'str', 'position': 0, 'description': 'CPE of application (might be unknown). ', 'readOnly': True}, 'socket': {'type': 'str', 'position': 0, 'description': 'Socket where application is available as reported by the scanner. ', 'readOnly': True}}}}, 'existingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were detected by the scan and already exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id', 'resolution', 'vulnerabilityID'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of vulnerability found in database. '}, 'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'resolution': {'type': 'str', 'position': 0, 'description': 'Resolution code of vulnerability (might be unresolved). ', 'enum': ['ACCEPTED', 'FALSE_POSITIVE', 'SERVICE_NOT_AVAILABLE', 'NO_LONGER_VULNERABLE', 'UNRESOLVED']}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'missingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were NOT detected by the scan but exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id', 'resolution', 'vulnerabilityID'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of vulnerability found in database. '}, 'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'resolution': {'type': 'str', 'position': 0, 'description': 'Resolution code of vulnerability (might be unresolved). ', 'enum': ['ACCEPTED', 'FALSE_POSITIVE', 'SERVICE_NOT_AVAILABLE', 'NO_LONGER_VULNERABLE', 'UNRESOLVED']}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'notExistingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were detected by the scan but do NOT exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['vulnerabilityID'], 'properties': {'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'operatingSystemCPE': {'type': 'str', 'position': 0, 'description': 'Operating system CPE of scanned host if host exists in database (might be unknown). ', 'readOnly': True}, 'ipAddresses': {'type': 'list', 'position': 0, 'description': 'All IP addresses of scanned host if host exists in database. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}, 'aliases': {'type': 'list', 'position': 0, 'description': 'All aliases of scanned host if host exists in database. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}, 'notExistingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were detected by the scan but do NOT exist in the database. Returns a set of socket strings. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '412': {'description': 'Validation error'}}}
host_asset_scanned_by_id = {'tags': ['assets/v1'], 'summary': 'Marks a single HostAsset as scanned. The host is identified by ID. (DEV)', 'description': '', 'operationId': 'hostAssetScannedByID', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'name': 'hostID', 'in': 'path', 'description': 'ID of the host asset', 'required': True, 'type': 'str'}, {'in': 'body', 'name': 'body', 'description': 'HostAsset scanned request', 'required': False, 'schema': {'type': 'object', 'required': ['detectedVulnerabilities'], 'properties': {'detectedVulnerabilities': {'type': 'list', 'position': 0, 'description': 'Specify (vulnerabilityID, socket string) objects of detected vulnerabilities. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['vulnerabilityID'], 'properties': {'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Specify vulnerability ID of detected vulnerability '}, 'socket': {'type': 'str', 'position': 0, 'description': 'Specify socket of detected vulnerability (e.g. tcp/80), or omit if vulnerability not related to a socket '}}}}, 'detectedApplications': {'type': 'list', 'position': 0, 'description': 'Specify sockets of detected applications (e.g. tcp/80). ', 'uniqueItems': True, 'items': {'type': 'string'}}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'required': ['ipAddress', 'resultCode'], 'properties': {'ipAddress': {'type': 'dict', 'properties': {'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'multicast': {'type': 'boolean'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}, 'resultCode': {'type': 'str', 'position': 0, 'description': 'Scanned host exists or does not exist in database. ', 'enum': ['HostExists', 'HostNotExists']}, 'hostID': {'type': 'str', 'position': 0, 'description': 'UUID of scanned host if host exists in database. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of scanned host if host exists in database. '}, 'existingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were detected by the scan and already exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of application found in database. '}, 'cpe': {'type': 'str', 'position': 0, 'description': 'CPE of application (might be unknown). ', 'readOnly': True}, 'socket': {'type': 'str', 'position': 0, 'description': 'Socket where application is available as reported by the scanner. ', 'readOnly': True}}}}, 'missingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were NOT detected by the scan but exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of application found in database. '}, 'cpe': {'type': 'str', 'position': 0, 'description': 'CPE of application (might be unknown). ', 'readOnly': True}, 'socket': {'type': 'str', 'position': 0, 'description': 'Socket where application is available as reported by the scanner. ', 'readOnly': True}}}}, 'existingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were detected by the scan and already exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id', 'resolution', 'vulnerabilityID'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of vulnerability found in database. '}, 'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'resolution': {'type': 'str', 'position': 0, 'description': 'Resolution code of vulnerability (might be unresolved). ', 'enum': ['ACCEPTED', 'FALSE_POSITIVE', 'SERVICE_NOT_AVAILABLE', 'NO_LONGER_VULNERABLE', 'UNRESOLVED']}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'missingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were NOT detected by the scan but exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['id', 'resolution', 'vulnerabilityID'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'UUID of vulnerability found in database. '}, 'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'resolution': {'type': 'str', 'position': 0, 'description': 'Resolution code of vulnerability (might be unresolved). ', 'enum': ['ACCEPTED', 'FALSE_POSITIVE', 'SERVICE_NOT_AVAILABLE', 'NO_LONGER_VULNERABLE', 'UNRESOLVED']}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'notExistingVulnerabilities': {'type': 'list', 'position': 0, 'description': 'List all vulnerabilities which were detected by the scan but do NOT exist in the database. ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['vulnerabilityID'], 'properties': {'vulnerabilityID': {'type': 'str', 'position': 0, 'description': 'Vulnerability identifier, e.g. CVE reference, as reported by the scanner. '}, 'socket': {'type': 'str', 'position': 0, 'description': 'Vulnerable socket on host as reported by the scanner (might be unknown). ', 'readOnly': True}}}}, 'operatingSystemCPE': {'type': 'str', 'position': 0, 'description': 'Operating system CPE of scanned host if host exists in database (might be unknown). ', 'readOnly': True}, 'ipAddresses': {'type': 'list', 'position': 0, 'description': 'All IP addresses of scanned host if host exists in database. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}, 'aliases': {'type': 'list', 'position': 0, 'description': 'All aliases of scanned host if host exists in database. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}, 'notExistingApplications': {'type': 'list', 'position': 0, 'description': 'List all applications which were detected by the scan but do NOT exist in the database. Returns a set of socket strings. ', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Object not found'}, '412': {'description': 'Validation error'}}}