"""Autogenerated API schema"""
from argus_api import session


find_n_i_d_s_events = {'tags': ['events/v1'], 'summary': 'Search for NIDS events (PUBLIC)', 'description': '', 'operationId': 'findNIDSEvents', 'consumes': ['application/json'], 'produces': ['application/json', 'text/csv'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'Search criteria', 'required': False, 'schema': {'type': 'object', 'properties': {'signature': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'destinationIP': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'sourceIP': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'ip': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'destinationPort': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'sourcePort': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'port': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'minSeverity': {'type': 'str', 'enum': ['low', 'medium', 'high', 'critical']}, 'maxSeverity': {'type': 'str', 'enum': ['low', 'medium', 'high', 'critical']}, 'limit': {'type': 'int', 'xml': {'attribute': True}, 'position': 0, 'description': 'Limit results '}, 'offset': {'type': 'int', 'xml': {'attribute': True}, 'position': 0, 'description': 'Offset results '}, 'includeDeleted': {'type': 'bool', 'xml': {'attribute': True}, 'position': 0, 'description': 'Also include deleted objects (where implemented) '}, 'customerID': {'type': 'list', 'xml': {'name': 'Customers', 'wrapped': True}, 'position': 0, 'description': 'DEPRECATED! Use customer instead ', 'uniqueItems': True, 'items': {'type': 'int', 'xml': {'name': 'CustomerID'}}}, 'skipFutureEvents': {'type': 'bool', 'position': 0, 'description': 'Whether service should generate endTimestamp by current timestamp. (default false)', 'default': False}, 'exclude': {'type': 'bool', 'xml': {'attribute': True}, 'position': 0, 'description': 'Exclude these criteria from the parent criteria. '}, 'eventIdentifier': {'type': 'list', 'xml': {'name': 'EventIdentifiers', 'wrapped': True}, 'position': 0, 'description': 'Search for events specified by full ID (type/timestamp/customerid/eventid). ', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'type': 'str', 'timestamp': {'type': 'int', 'xml': {'attribute': True}}, 'customerID': {'type': 'int', 'xml': {'attribute': True}}, 'eventID': {'type': 'str', 'xml': {'attribute': True}}}}}, 'locationID': {'type': 'list', 'xml': {'name': 'Locations', 'wrapped': True}, 'position': 0, 'description': 'Search for events having these locations. ', 'uniqueItems': True, 'items': {'type': 'int', 'xml': {'name': 'LocationID'}}}, 'severity': {'type': 'list', 'position': 0, 'description': "Search events with specified severity. Can't be used together with minSeverity/maxSeverity. ", 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['low', 'medium', 'high', 'critical']}}, 'customer': {'type': 'list', 'position': 0, 'description': 'Search for events by customer (id or shortname). ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'alarmID': {'type': 'list', 'xml': {'name': 'Alarms', 'wrapped': True}, 'position': 0, 'description': 'Search for events having an attack identifier (signature) mapped to any of these alarms. ', 'uniqueItems': True, 'items': {'type': 'int', 'xml': {'name': 'AlarmID'}}}, 'attackCategoryID': {'type': 'list', 'xml': {'name': 'AttackCategories', 'wrapped': True}, 'position': 0, 'description': 'Search for events having an attack identifier (signature) mapped to any of these categories. ', 'uniqueItems': True, 'items': {'type': 'int', 'xml': {'name': 'AttackCategoryID'}}}, 'sourceGeoCountry': {'type': 'list', 'xml': {'name': 'SourceGeoCountry'}, 'position': 0, 'description': 'Search for events where source IP is registered in any of these countries. ', 'uniqueItems': True, 'items': {'type': 'str', 'xml': {'name': 'SourceGeoCountry'}}}, 'destinationGeoCountry': {'type': 'list', 'xml': {'name': 'DestinationGeoCountry'}, 'position': 0, 'description': 'Search for events where destination IP is registered in any of these countries. ', 'uniqueItems': True, 'items': {'type': 'str', 'xml': {'name': 'DestinationGeoCountry'}}}, 'geoCountry': {'type': 'list', 'xml': {'name': 'GeoCountry'}, 'position': 0, 'description': 'Search for events where source or destination IP is registered in any of these countries. ', 'uniqueItems': True, 'items': {'type': 'str', 'xml': {'name': 'GeoCountry'}}}, 'properties': {'type': 'dict', 'xml': {'name': 'Properties'}, 'position': 0, 'description': 'Search for events having these properties (logical AND). ', 'additionalProperties': {'type': 'string'}}, 'exactMatchProperties': {'type': 'bool', 'position': 0, 'description': 'If set to true, will execute in-memory filtering to only match events that have exact match of properties specified at top level "properties" field of search request. WARN: The count of response would not be reliable, as the filtering is applied in-memory of application server, but the count was done by search engine. (default true)', 'default': True}, 'sensorID': {'type': 'list', 'xml': {'name': 'Sensors', 'wrapped': True}, 'position': 0, 'description': 'List of sensor IDs that must have a match in the retrieved event. ', 'uniqueItems': True, 'items': {'type': 'int', 'xml': {'name': 'SensorID'}}}, 'subCriteria': {'type': 'list', 'xml': {'name': 'SubCriteria', 'wrapped': True}, 'position': 0, 'description': 'Subcriterias used in the search. ', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'signature': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'destinationIP': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'sourceIP': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'ip': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'destinationPort': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'sourcePort': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'port': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'string'}}, 'minSeverity': {'type': 'str', 'enum': ['low', 'medium', 'high', 'critical']}, 'maxSeverity': {'type': 'str', 'enum': ['low', 'medium', 'high', 'critical']}, 'limit': {'type': 'int', 'xml': {'attribute': True}, 'position': 0, 'description': 'Limit results '}, 'offset': {'type': 'int', 'xml': {'attribute': True}, 'position': 0, 'description': 'Offset results '}, 'includeDeleted': {'type': 'bool', 'xml': {'attribute': True}, 'position': 0, 'description': 'Also include deleted objects (where implemented) '}, 'customerID': {'type': 'list', 'xml': {'name': 'Customers', 'wrapped': True}, 'position': 0, 'description': 'DEPRECATED! Use customer instead ', 'uniqueItems': True, 'items': {'type': 'int', 'xml': {'name': 'CustomerID'}}}, 'skipFutureEvents': {'type': 'bool', 'position': 0, 'description': 'Whether service should generate endTimestamp by current timestamp. (default false)', 'default': False}, 'exclude': {'type': 'bool', 'xml': {'attribute': True}, 'position': 0, 'description': 'Exclude these criteria from the parent criteria. '}, 'eventIdentifier': {'type': 'list', 'xml': {'name': 'EventIdentifiers', 'wrapped': True}, 'position': 0, 'description': 'Search for events specified by full ID (type/timestamp/customerid/eventid). ', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'type': 'str', 'timestamp': {'type': 'int', 'xml': {'attribute': True}}, 'customerID': {'type': 'int', 'xml': {'attribute': True}}, 'eventID': {'type': 'str', 'xml': {'attribute': True}}}}}, 'locationID': {'type': 'list', 'xml': {'name': 'Locations', 'wrapped': True}, 'position': 0, 'description': 'Search for events having these locations. ', 'uniqueItems': True, 'items': {'type': 'int', 'xml': {'name': 'LocationID'}}}, 'severity': {'type': 'list', 'position': 0, 'description': "Search events with specified severity. Can't be used together with minSeverity/maxSeverity. ", 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['low', 'medium', 'high', 'critical']}}, 'customer': {'type': 'list', 'position': 0, 'description': 'Search for events by customer (id or shortname). ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'alarmID': {'type': 'list', 'xml': {'name': 'Alarms', 'wrapped': True}, 'position': 0, 'description': 'Search for events having an attack identifier (signature) mapped to any of these alarms. ', 'uniqueItems': True, 'items': {'type': 'int', 'xml': {'name': 'AlarmID'}}}, 'attackCategoryID': {'type': 'list', 'xml': {'name': 'AttackCategories', 'wrapped': True}, 'position': 0, 'description': 'Search for events having an attack identifier (signature) mapped to any of these categories. ', 'uniqueItems': True, 'items': {'type': 'int', 'xml': {'name': 'AttackCategoryID'}}}, 'sourceGeoCountry': {'type': 'list', 'xml': {'name': 'SourceGeoCountry'}, 'position': 0, 'description': 'Search for events where source IP is registered in any of these countries. ', 'uniqueItems': True, 'items': {'type': 'str', 'xml': {'name': 'SourceGeoCountry'}}}, 'destinationGeoCountry': {'type': 'list', 'xml': {'name': 'DestinationGeoCountry'}, 'position': 0, 'description': 'Search for events where destination IP is registered in any of these countries. ', 'uniqueItems': True, 'items': {'type': 'str', 'xml': {'name': 'DestinationGeoCountry'}}}, 'geoCountry': {'type': 'list', 'xml': {'name': 'GeoCountry'}, 'position': 0, 'description': 'Search for events where source or destination IP is registered in any of these countries. ', 'uniqueItems': True, 'items': {'type': 'str', 'xml': {'name': 'GeoCountry'}}}, 'properties': {'type': 'dict', 'xml': {'name': 'Properties'}, 'position': 0, 'description': 'Search for events having these properties (logical AND). ', 'additionalProperties': {'type': 'string'}}, 'exactMatchProperties': {'type': 'bool', 'position': 0, 'description': 'If set to true, will execute in-memory filtering to only match events that have exact match of properties specified at top level "properties" field of search request. WARN: The count of response would not be reliable, as the filtering is applied in-memory of application server, but the count was done by search engine. (default true)', 'default': True}, 'sensorID': {'type': 'list', 'xml': {'name': 'Sensors', 'wrapped': True}, 'position': 0, 'description': 'List of sensor IDs that must have a match in the retrieved event. ', 'uniqueItems': True, 'items': {'type': 'int', 'xml': {'name': 'SensorID'}}}, 'subCriteria': {'type': 'list', 'xml': {'name': 'SubCriteria', 'wrapped': True}, 'position': 0, 'description': 'Subcriterias used in the search. ', 'uniqueItems': True, 'items': []}, 'startTimestamp': {'type': 'int', 'xml': {'attribute': True}, 'position': 0, 'description': 'Search objects from this timestamp '}, 'endTimestamp': {'type': 'int', 'xml': {'attribute': True}, 'position': 0, 'description': 'Search objects until this timestamp '}, 'sortBy': {'type': 'list', 'position': 0, 'description': 'Order results by these properties (prefix with - to sort descending) ', 'items': {'type': 'string'}}, 'includeFlags': {'type': 'list', 'position': 0, 'description': 'Search objects with these flags set ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ESTABLISHED', 'BLOCKED', 'SNAPSHOT', 'FINALIZED', 'SOURCE_IS_CUSTOMERNET', 'DESTINATION_IS_CUSTOMERNET', 'SOURCE_IS_PARTIAL_CUSTOMERNET', 'DESTINATION_IS_PARTIAL_CUSTOMERNET', 'INTRUDER_IS_CUSTOMERNET', 'VICTIM_IS_CUSTOMERNET', 'INTRUDER_IS_PARTIAL_CUSTOMERNET', 'VICTIM_IS_PARTIAL_CUSTOMERNET', 'PARTIALLY_BLOCKED', 'FALSE_POSITIVE', 'NOT_A_THREAT', 'TUNING_CANDIDATE', 'NOTIFIED', 'PARTIALLY_NOTIFIED', 'FOLLOWUP', 'IDENTIFIED_THREAT', 'THREAT_CANDIDATE', 'ACKNOWLEDGED', 'PARTIALLY_ACKNOWLEDGED', 'SEVERITY_ADJUSTED', 'COMMENTED', 'FILTERED', 'CHECKED', 'INCOMPLETE_DETAILS', 'AGGREGATED_BASE_EVENT', 'REMOTE_STORAGE', 'CUSTOM_SOURCE_AGGREGATION', 'CUSTOM_DESTINATION_AGGREGATION', 'CUSTOM_INTRUDER_AGGREGATION', 'CUSTOM_VICTIM_AGGREGATION', 'HAS_PAYLOAD', 'HAS_PCAP', 'ASSOCIATED_TO_CASE_BY_FILTER', 'SEVERITY_INCREASED_BY_FILTER', 'SEVERITY_REDUCED_BY_FILTER', 'CREATED_BY_ANALYSIS_FILTER', 'EXTEND_EVENT_TTL', 'INITIAL_TUNING', 'POST_ANALYSIS', 'PARTIAL_SSL_TERMINATED', 'SSL_TERMINATED', 'AUTO_REPORT', 'MISSING_TIMESTAMP', 'CLOCK_OUT_OF_SYNC', 'DROP_ANALYSIS', 'ESCALATED_BY_REPUTATION', 'HAS_SAMPLE', 'STORE_EVENT', 'STORE_AGGREGATED']}}, 'excludeFlags': {'type': 'list', 'position': 0, 'description': 'Exclude objects with these flags set ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ESTABLISHED', 'BLOCKED', 'SNAPSHOT', 'FINALIZED', 'SOURCE_IS_CUSTOMERNET', 'DESTINATION_IS_CUSTOMERNET', 'SOURCE_IS_PARTIAL_CUSTOMERNET', 'DESTINATION_IS_PARTIAL_CUSTOMERNET', 'INTRUDER_IS_CUSTOMERNET', 'VICTIM_IS_CUSTOMERNET', 'INTRUDER_IS_PARTIAL_CUSTOMERNET', 'VICTIM_IS_PARTIAL_CUSTOMERNET', 'PARTIALLY_BLOCKED', 'FALSE_POSITIVE', 'NOT_A_THREAT', 'TUNING_CANDIDATE', 'NOTIFIED', 'PARTIALLY_NOTIFIED', 'FOLLOWUP', 'IDENTIFIED_THREAT', 'THREAT_CANDIDATE', 'ACKNOWLEDGED', 'PARTIALLY_ACKNOWLEDGED', 'SEVERITY_ADJUSTED', 'COMMENTED', 'FILTERED', 'CHECKED', 'INCOMPLETE_DETAILS', 'AGGREGATED_BASE_EVENT', 'REMOTE_STORAGE', 'CUSTOM_SOURCE_AGGREGATION', 'CUSTOM_DESTINATION_AGGREGATION', 'CUSTOM_INTRUDER_AGGREGATION', 'CUSTOM_VICTIM_AGGREGATION', 'HAS_PAYLOAD', 'HAS_PCAP', 'ASSOCIATED_TO_CASE_BY_FILTER', 'SEVERITY_INCREASED_BY_FILTER', 'SEVERITY_REDUCED_BY_FILTER', 'CREATED_BY_ANALYSIS_FILTER', 'EXTEND_EVENT_TTL', 'INITIAL_TUNING', 'POST_ANALYSIS', 'PARTIAL_SSL_TERMINATED', 'SSL_TERMINATED', 'AUTO_REPORT', 'MISSING_TIMESTAMP', 'CLOCK_OUT_OF_SYNC', 'DROP_ANALYSIS', 'ESCALATED_BY_REPUTATION', 'HAS_SAMPLE', 'STORE_EVENT', 'STORE_AGGREGATED']}}, 'lastUpdatedTimestamp': {'type': 'int', 'xml': {'attribute': True}, 'position': 0, 'description': 'Match only with events marked with a last updated time greater or equal to this. '}, 'indexStartTime': {'type': 'int', 'position': 0, 'description': 'Earliest created time of the indices searched. ', 'minimum': 0}, 'indexEndTime': {'type': 'int', 'position': 0, 'description': 'Last created time of the indices searched. ', 'minimum': 0}}, 'xml': {'name': 'NIDSEventSearchCriteria'}}}, 'startTimestamp': {'type': 'int', 'xml': {'attribute': True}, 'position': 0, 'description': 'Search objects from this timestamp '}, 'endTimestamp': {'type': 'int', 'xml': {'attribute': True}, 'position': 0, 'description': 'Search objects until this timestamp '}, 'sortBy': {'type': 'list', 'position': 0, 'description': 'Order results by these properties (prefix with - to sort descending) ', 'items': {'type': 'string'}}, 'includeFlags': {'type': 'list', 'position': 0, 'description': 'Search objects with these flags set ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ESTABLISHED', 'BLOCKED', 'SNAPSHOT', 'FINALIZED', 'SOURCE_IS_CUSTOMERNET', 'DESTINATION_IS_CUSTOMERNET', 'SOURCE_IS_PARTIAL_CUSTOMERNET', 'DESTINATION_IS_PARTIAL_CUSTOMERNET', 'INTRUDER_IS_CUSTOMERNET', 'VICTIM_IS_CUSTOMERNET', 'INTRUDER_IS_PARTIAL_CUSTOMERNET', 'VICTIM_IS_PARTIAL_CUSTOMERNET', 'PARTIALLY_BLOCKED', 'FALSE_POSITIVE', 'NOT_A_THREAT', 'TUNING_CANDIDATE', 'NOTIFIED', 'PARTIALLY_NOTIFIED', 'FOLLOWUP', 'IDENTIFIED_THREAT', 'THREAT_CANDIDATE', 'ACKNOWLEDGED', 'PARTIALLY_ACKNOWLEDGED', 'SEVERITY_ADJUSTED', 'COMMENTED', 'FILTERED', 'CHECKED', 'INCOMPLETE_DETAILS', 'AGGREGATED_BASE_EVENT', 'REMOTE_STORAGE', 'CUSTOM_SOURCE_AGGREGATION', 'CUSTOM_DESTINATION_AGGREGATION', 'CUSTOM_INTRUDER_AGGREGATION', 'CUSTOM_VICTIM_AGGREGATION', 'HAS_PAYLOAD', 'HAS_PCAP', 'ASSOCIATED_TO_CASE_BY_FILTER', 'SEVERITY_INCREASED_BY_FILTER', 'SEVERITY_REDUCED_BY_FILTER', 'CREATED_BY_ANALYSIS_FILTER', 'EXTEND_EVENT_TTL', 'INITIAL_TUNING', 'POST_ANALYSIS', 'PARTIAL_SSL_TERMINATED', 'SSL_TERMINATED', 'AUTO_REPORT', 'MISSING_TIMESTAMP', 'CLOCK_OUT_OF_SYNC', 'DROP_ANALYSIS', 'ESCALATED_BY_REPUTATION', 'HAS_SAMPLE', 'STORE_EVENT', 'STORE_AGGREGATED']}}, 'excludeFlags': {'type': 'list', 'position': 0, 'description': 'Exclude objects with these flags set ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ESTABLISHED', 'BLOCKED', 'SNAPSHOT', 'FINALIZED', 'SOURCE_IS_CUSTOMERNET', 'DESTINATION_IS_CUSTOMERNET', 'SOURCE_IS_PARTIAL_CUSTOMERNET', 'DESTINATION_IS_PARTIAL_CUSTOMERNET', 'INTRUDER_IS_CUSTOMERNET', 'VICTIM_IS_CUSTOMERNET', 'INTRUDER_IS_PARTIAL_CUSTOMERNET', 'VICTIM_IS_PARTIAL_CUSTOMERNET', 'PARTIALLY_BLOCKED', 'FALSE_POSITIVE', 'NOT_A_THREAT', 'TUNING_CANDIDATE', 'NOTIFIED', 'PARTIALLY_NOTIFIED', 'FOLLOWUP', 'IDENTIFIED_THREAT', 'THREAT_CANDIDATE', 'ACKNOWLEDGED', 'PARTIALLY_ACKNOWLEDGED', 'SEVERITY_ADJUSTED', 'COMMENTED', 'FILTERED', 'CHECKED', 'INCOMPLETE_DETAILS', 'AGGREGATED_BASE_EVENT', 'REMOTE_STORAGE', 'CUSTOM_SOURCE_AGGREGATION', 'CUSTOM_DESTINATION_AGGREGATION', 'CUSTOM_INTRUDER_AGGREGATION', 'CUSTOM_VICTIM_AGGREGATION', 'HAS_PAYLOAD', 'HAS_PCAP', 'ASSOCIATED_TO_CASE_BY_FILTER', 'SEVERITY_INCREASED_BY_FILTER', 'SEVERITY_REDUCED_BY_FILTER', 'CREATED_BY_ANALYSIS_FILTER', 'EXTEND_EVENT_TTL', 'INITIAL_TUNING', 'POST_ANALYSIS', 'PARTIAL_SSL_TERMINATED', 'SSL_TERMINATED', 'AUTO_REPORT', 'MISSING_TIMESTAMP', 'CLOCK_OUT_OF_SYNC', 'DROP_ANALYSIS', 'ESCALATED_BY_REPUTATION', 'HAS_SAMPLE', 'STORE_EVENT', 'STORE_AGGREGATED']}}, 'lastUpdatedTimestamp': {'type': 'int', 'xml': {'attribute': True}, 'position': 0, 'description': 'Match only with events marked with a last updated time greater or equal to this. '}, 'indexStartTime': {'type': 'int', 'position': 0, 'description': 'Earliest created time of the indices searched. ', 'minimum': 0}, 'indexEndTime': {'type': 'int', 'position': 0, 'description': 'Last created time of the indices searched. ', 'minimum': 0}}, 'xml': {'name': 'NIDSEventSearchCriteria'}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'customerInfo': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'properties': {'type': 'dict', 'additionalProperties': {'type': 'string'}}, 'comments': {'type': 'list', 'items': {'type': 'dict', 'properties': {'timestamp': {'type': 'int', 'position': 0, 'description': 'When the comment was added. '}, 'user': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'comment': {'type': 'str', 'position': 0, 'description': "The comment's text. "}}}}, 'sensor': {'type': 'dict', 'properties': {'sensorID': {'type': 'int'}, 'hostName': {'type': 'string'}, 'hostIpAddress': {'type': 'dict', 'properties': {'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'multicast': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}, 'hostIpString': {'type': 'string'}}}, 'location': {'type': 'dict', 'properties': {'shortName': {'type': 'string'}, 'name': {'type': 'string'}, 'timeZone': {'type': 'string'}, 'id': {'type': 'int'}}}, 'attackInfo': {'type': 'dict', 'properties': {'alarmID': {'type': 'int'}, 'alarmDescription': {'type': 'string'}, 'attackCategoryID': {'type': 'int'}, 'attackCategoryName': {'type': 'string'}, 'signature': {'type': 'string'}}}, 'count': {'type': 'int'}, 'engineTimestamp': {'type': 'int'}, 'protocolID': {'type': 'int'}, 'domain': {'type': 'dict', 'properties': {'fqdn': {'type': 'string'}}}, 'uri': {'type': 'string'}, 'source': {'type': 'dict', 'properties': {'port': {'type': 'int'}, 'geoLocation': {'type': 'dict', 'properties': {'countryCode': {'type': 'string'}, 'countryName': {'type': 'string'}, 'locationName': {'type': 'string'}, 'latitude': {'type': 'float'}, 'longitude': {'type': 'float'}}}, 'networkAddress': {'type': 'dict', 'properties': {'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'multicast': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}}}, 'destination': {'type': 'dict', 'properties': {'port': {'type': 'int'}, 'geoLocation': {'type': 'dict', 'properties': {'countryCode': {'type': 'string'}, 'countryName': {'type': 'string'}, 'locationName': {'type': 'string'}, 'latitude': {'type': 'float'}, 'longitude': {'type': 'float'}}}, 'networkAddress': {'type': 'dict', 'properties': {'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'multicast': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}}}, 'timestamp': {'type': 'int'}, 'severity': {'type': 'str', 'readOnly': True, 'enum': ['low', 'medium', 'high', 'critical']}, 'flags': {'type': 'list', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ESTABLISHED', 'BLOCKED', 'SNAPSHOT', 'FINALIZED', 'SOURCE_IS_CUSTOMERNET', 'DESTINATION_IS_CUSTOMERNET', 'SOURCE_IS_PARTIAL_CUSTOMERNET', 'DESTINATION_IS_PARTIAL_CUSTOMERNET', 'INTRUDER_IS_CUSTOMERNET', 'VICTIM_IS_CUSTOMERNET', 'INTRUDER_IS_PARTIAL_CUSTOMERNET', 'VICTIM_IS_PARTIAL_CUSTOMERNET', 'PARTIALLY_BLOCKED', 'FALSE_POSITIVE', 'NOT_A_THREAT', 'TUNING_CANDIDATE', 'NOTIFIED', 'PARTIALLY_NOTIFIED', 'FOLLOWUP', 'IDENTIFIED_THREAT', 'THREAT_CANDIDATE', 'ACKNOWLEDGED', 'PARTIALLY_ACKNOWLEDGED', 'SEVERITY_ADJUSTED', 'COMMENTED', 'FILTERED', 'CHECKED', 'INCOMPLETE_DETAILS', 'AGGREGATED_BASE_EVENT', 'REMOTE_STORAGE', 'CUSTOM_SOURCE_AGGREGATION', 'CUSTOM_DESTINATION_AGGREGATION', 'CUSTOM_INTRUDER_AGGREGATION', 'CUSTOM_VICTIM_AGGREGATION', 'HAS_PAYLOAD', 'HAS_PCAP', 'ASSOCIATED_TO_CASE_BY_FILTER', 'SEVERITY_INCREASED_BY_FILTER', 'SEVERITY_REDUCED_BY_FILTER', 'CREATED_BY_ANALYSIS_FILTER', 'EXTEND_EVENT_TTL', 'INITIAL_TUNING', 'POST_ANALYSIS', 'PARTIAL_SSL_TERMINATED', 'SSL_TERMINATED', 'AUTO_REPORT', 'MISSING_TIMESTAMP', 'CLOCK_OUT_OF_SYNC', 'DROP_ANALYSIS', 'ESCALATED_BY_REPUTATION', 'HAS_SAMPLE', 'STORE_EVENT', 'STORE_AGGREGATED']}}, 'id': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '412': {'description': 'Validation failed'}}}
list_n_i_d_s_events = {'tags': ['events/v1'], 'summary': 'Simple search for NIDS events (PUBLIC)', 'description': '', 'operationId': 'listNIDSEvents', 'produces': ['application/json', 'text/csv'], 'parameters': [{'name': 'customerID', 'in': 'query', 'description': 'Limit to customerID', 'required': False, 'type': 'list', 'items': {'type': 'int'}, 'collectionFormat': 'multi'}, {'name': 'signature', 'in': 'query', 'description': 'Limit to signature', 'required': False, 'type': 'list', 'items': {'type': 'string'}, 'collectionFormat': 'multi'}, {'name': 'ip', 'in': 'query', 'description': 'Limit to ip/network', 'required': False, 'type': 'list', 'items': {'type': 'string'}, 'collectionFormat': 'multi'}, {'name': 'startTimestamp', 'in': 'query', 'description': 'Limit to events after this timestamp (default is last 24 hours).', 'required': False, 'type': 'str', 'default': '-24hours'}, {'name': 'endTimestamp', 'in': 'query', 'description': 'Limit to events before this timestamp.', 'required': False, 'type': 'str', 'default': 'now'}, {'name': 'limit', 'in': 'query', 'description': 'Limit results', 'required': False, 'type': 'int', 'default': 25, 'minimum': 0}, {'name': 'offset', 'in': 'query', 'description': 'Offset results', 'required': False, 'type': 'int', 'default': 0, 'minimum': 0}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'customerInfo': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'properties': {'type': 'dict', 'additionalProperties': {'type': 'string'}}, 'comments': {'type': 'list', 'items': {'type': 'dict', 'properties': {'timestamp': {'type': 'int', 'position': 0, 'description': 'When the comment was added. '}, 'user': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'comment': {'type': 'str', 'position': 0, 'description': "The comment's text. "}}}}, 'sensor': {'type': 'dict', 'properties': {'sensorID': {'type': 'int'}, 'hostName': {'type': 'string'}, 'hostIpAddress': {'type': 'dict', 'properties': {'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'multicast': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}, 'hostIpString': {'type': 'string'}}}, 'location': {'type': 'dict', 'properties': {'shortName': {'type': 'string'}, 'name': {'type': 'string'}, 'timeZone': {'type': 'string'}, 'id': {'type': 'int'}}}, 'attackInfo': {'type': 'dict', 'properties': {'alarmID': {'type': 'int'}, 'alarmDescription': {'type': 'string'}, 'attackCategoryID': {'type': 'int'}, 'attackCategoryName': {'type': 'string'}, 'signature': {'type': 'string'}}}, 'count': {'type': 'int'}, 'engineTimestamp': {'type': 'int'}, 'protocolID': {'type': 'int'}, 'domain': {'type': 'dict', 'properties': {'fqdn': {'type': 'string'}}}, 'uri': {'type': 'string'}, 'source': {'type': 'dict', 'properties': {'port': {'type': 'int'}, 'geoLocation': {'type': 'dict', 'properties': {'countryCode': {'type': 'string'}, 'countryName': {'type': 'string'}, 'locationName': {'type': 'string'}, 'latitude': {'type': 'float'}, 'longitude': {'type': 'float'}}}, 'networkAddress': {'type': 'dict', 'properties': {'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'multicast': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}}}, 'destination': {'type': 'dict', 'properties': {'port': {'type': 'int'}, 'geoLocation': {'type': 'dict', 'properties': {'countryCode': {'type': 'string'}, 'countryName': {'type': 'string'}, 'locationName': {'type': 'string'}, 'latitude': {'type': 'float'}, 'longitude': {'type': 'float'}}}, 'networkAddress': {'type': 'dict', 'properties': {'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'public': {'type': 'boolean'}, 'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'multicast': {'type': 'boolean'}, 'maskBits': {'type': 'int'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}}}, 'timestamp': {'type': 'int'}, 'severity': {'type': 'str', 'readOnly': True, 'enum': ['low', 'medium', 'high', 'critical']}, 'flags': {'type': 'list', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ESTABLISHED', 'BLOCKED', 'SNAPSHOT', 'FINALIZED', 'SOURCE_IS_CUSTOMERNET', 'DESTINATION_IS_CUSTOMERNET', 'SOURCE_IS_PARTIAL_CUSTOMERNET', 'DESTINATION_IS_PARTIAL_CUSTOMERNET', 'INTRUDER_IS_CUSTOMERNET', 'VICTIM_IS_CUSTOMERNET', 'INTRUDER_IS_PARTIAL_CUSTOMERNET', 'VICTIM_IS_PARTIAL_CUSTOMERNET', 'PARTIALLY_BLOCKED', 'FALSE_POSITIVE', 'NOT_A_THREAT', 'TUNING_CANDIDATE', 'NOTIFIED', 'PARTIALLY_NOTIFIED', 'FOLLOWUP', 'IDENTIFIED_THREAT', 'THREAT_CANDIDATE', 'ACKNOWLEDGED', 'PARTIALLY_ACKNOWLEDGED', 'SEVERITY_ADJUSTED', 'COMMENTED', 'FILTERED', 'CHECKED', 'INCOMPLETE_DETAILS', 'AGGREGATED_BASE_EVENT', 'REMOTE_STORAGE', 'CUSTOM_SOURCE_AGGREGATION', 'CUSTOM_DESTINATION_AGGREGATION', 'CUSTOM_INTRUDER_AGGREGATION', 'CUSTOM_VICTIM_AGGREGATION', 'HAS_PAYLOAD', 'HAS_PCAP', 'ASSOCIATED_TO_CASE_BY_FILTER', 'SEVERITY_INCREASED_BY_FILTER', 'SEVERITY_REDUCED_BY_FILTER', 'CREATED_BY_ANALYSIS_FILTER', 'EXTEND_EVENT_TTL', 'INITIAL_TUNING', 'POST_ANALYSIS', 'PARTIAL_SSL_TERMINATED', 'SSL_TERMINATED', 'AUTO_REPORT', 'MISSING_TIMESTAMP', 'CLOCK_OUT_OF_SYNC', 'DROP_ANALYSIS', 'ESCALATED_BY_REPUTATION', 'HAS_SAMPLE', 'STORE_EVENT', 'STORE_AGGREGATED']}}, 'id': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '412': {'description': 'Validation failed'}}}