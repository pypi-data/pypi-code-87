"""Autogenerated API schema"""
from argus_api import session


delete_data_store_entries = {'tags': ['datastores/v1'], 'summary': 'Deletes the specified datastore entries for the specified store. (PUBLIC)', 'description': '', 'operationId': 'deleteDataStoreEntries', 'produces': ['application/json'], 'parameters': [{'name': 'dataStore', 'in': 'path', 'description': 'Store name', 'required': True, 'type': 'str'}, {'name': 'key', 'in': 'query', 'description': 'Datastore keys to delete', 'required': True, 'type': 'list', 'items': {'type': 'string'}, 'collectionFormat': 'multi', 'maxItems': 2147483647, 'minItems': 1}, {'name': 'customerID', 'in': 'query', 'description': 'Specify datastore to delete entries from (default is users customer)', 'required': False, 'type': 'int', 'minimum': 0}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'dataStoreName': {'type': 'string'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'lastUpdatedTimestamp': {'type': 'int'}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'key': {'type': 'string'}, 'value': {'type': 'string'}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Store not found'}, '412': {'description': 'Validation error'}}}
get_entries_from_store = {'tags': ['datastores/v1'], 'summary': 'Returns datastore entries for the specified store, matching the search criteria. (PUBLIC)', 'description': '', 'operationId': 'getEntriesFromStore', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'name': 'dataStore', 'in': 'path', 'description': 'Store name', 'required': True, 'type': 'str'}, {'in': 'body', 'name': 'body', 'description': 'Search criteria', 'required': False, 'schema': {'type': 'object', 'properties': {'limit': {'type': 'int', 'position': 0, 'description': 'Set this value to set max number of results. By default, no restriction on result set size. '}, 'offset': {'type': 'int', 'position': 0, 'description': 'Set this value to skip the first (offset) objects. By default, return result from first object. '}, 'includeDeleted': {'type': 'bool', 'position': 0, 'description': 'Set to true to include deleted objects. By default, exclude deleted objects. '}, 'subCriteria': {'type': 'list', 'position': 0, 'description': 'Set additional criterias which are applied using a logical OR. ', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'limit': {'type': 'int', 'position': 0, 'description': 'Set this value to set max number of results. By default, no restriction on result set size. '}, 'offset': {'type': 'int', 'position': 0, 'description': 'Set this value to skip the first (offset) objects. By default, return result from first object. '}, 'includeDeleted': {'type': 'bool', 'position': 0, 'description': 'Set to true to include deleted objects. By default, exclude deleted objects. '}, 'subCriteria': {'type': 'list', 'position': 0, 'description': 'Set additional criterias which are applied using a logical OR. ', 'uniqueItems': True, 'items': []}, 'exclude': {'type': 'bool', 'position': 0, 'description': 'Only relevant for subcriteria. If set to true, objects matching this subcriteria object will be excluded. '}, 'required': {'type': 'bool', 'position': 0, 'description': 'Only relevant for subcriteria. If set to true, objects matching this subcriteria are required (AND-ed together with parent criteria). '}, 'customerID': {'type': 'list', 'position': 0, 'description': 'Restrict search to data belonging to specified customers. ', 'uniqueItems': True, 'items': {'type': 'int'}}, 'userID': {'type': 'list', 'position': 0, 'description': 'Restrict search to entries which was last updated by specified users. ', 'uniqueItems': True, 'items': {'type': 'int'}}, 'key': {'type': 'list', 'position': 0, 'description': 'Restrict search to the specified key (entries). ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'fromKey': {'type': 'str', 'position': 0, 'description': 'Restrict search to entries (map keys) which are greater than this key (including, by lexical order). '}, 'toKey': {'type': 'str', 'position': 0, 'description': 'Restrict search to entries (map keys) which are less than this key (including, by lexical order). '}, 'startTimestamp': {'type': 'int', 'position': 0, 'description': 'Restrict search to entries which are last updated after this timestamp (including). '}, 'endTimestamp': {'type': 'int', 'position': 0, 'description': 'Restrict search to entries which are last updated before this timestamp (including). '}, 'sortBy': {'type': 'list', 'position': 0, 'description': 'List of properties to sort by (prefix with "-" to sort descending). ', 'items': {'type': 'str', 'enum': ['key', 'lastUpdatedTimestamp']}}, 'includeFlags': {'type': 'list', 'position': 0, 'description': 'Only include objects which have includeFlags set. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}, 'excludeFlags': {'type': 'list', 'position': 0, 'description': 'Exclude objects which have excludeFlags set. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}}}}, 'exclude': {'type': 'bool', 'position': 0, 'description': 'Only relevant for subcriteria. If set to true, objects matching this subcriteria object will be excluded. '}, 'required': {'type': 'bool', 'position': 0, 'description': 'Only relevant for subcriteria. If set to true, objects matching this subcriteria are required (AND-ed together with parent criteria). '}, 'customerID': {'type': 'list', 'position': 0, 'description': 'Restrict search to data belonging to specified customers. ', 'uniqueItems': True, 'items': {'type': 'int'}}, 'userID': {'type': 'list', 'position': 0, 'description': 'Restrict search to entries which was last updated by specified users. ', 'uniqueItems': True, 'items': {'type': 'int'}}, 'key': {'type': 'list', 'position': 0, 'description': 'Restrict search to the specified key (entries). ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'fromKey': {'type': 'str', 'position': 0, 'description': 'Restrict search to entries (map keys) which are greater than this key (including, by lexical order). '}, 'toKey': {'type': 'str', 'position': 0, 'description': 'Restrict search to entries (map keys) which are less than this key (including, by lexical order). '}, 'startTimestamp': {'type': 'int', 'position': 0, 'description': 'Restrict search to entries which are last updated after this timestamp (including). '}, 'endTimestamp': {'type': 'int', 'position': 0, 'description': 'Restrict search to entries which are last updated before this timestamp (including). '}, 'sortBy': {'type': 'list', 'position': 0, 'description': 'List of properties to sort by (prefix with "-" to sort descending). ', 'items': {'type': 'str', 'enum': ['key', 'lastUpdatedTimestamp']}}, 'includeFlags': {'type': 'list', 'position': 0, 'description': 'Only include objects which have includeFlags set. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}, 'excludeFlags': {'type': 'list', 'position': 0, 'description': 'Exclude objects which have excludeFlags set. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'dataStoreName': {'type': 'string'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'lastUpdatedTimestamp': {'type': 'int'}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'key': {'type': 'string'}, 'value': {'type': 'string'}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Store not found'}, '412': {'description': 'Validation error'}}}
get_entries_from_store_simplified = {'tags': ['datastores/v1'], 'summary': 'Returns datastore entries for the specified store, matching query parameters. (PUBLIC)', 'description': '', 'operationId': 'getEntriesFromStoreSimplified', 'produces': ['application/json'], 'parameters': [{'name': 'dataStore', 'in': 'path', 'description': 'Store name', 'required': True, 'type': 'str'}, {'name': 'offset', 'in': 'query', 'description': 'Skip a number of results', 'required': False, 'type': 'int', 'default': 0, 'minimum': 0}, {'name': 'limit', 'in': 'query', 'description': 'Maximum number of returned results', 'required': False, 'type': 'int', 'default': 25, 'minimum': 0}, {'name': 'customerID', 'in': 'query', 'description': 'Limit search to entries for the specified customers', 'required': False, 'type': 'list', 'items': {'type': 'int'}, 'collectionFormat': 'multi'}, {'name': 'key', 'in': 'query', 'description': 'Limit search to the specified entry keys', 'required': False, 'type': 'list', 'items': {'type': 'string'}, 'collectionFormat': 'multi'}, {'name': 'includeDeleted', 'in': 'query', 'description': 'Include deleted/expired keys', 'required': False, 'type': 'bool', 'default': False}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'dataStoreName': {'type': 'string'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'lastUpdatedTimestamp': {'type': 'int'}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'key': {'type': 'string'}, 'value': {'type': 'string'}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Store not found'}, '412': {'description': 'Validation error'}}}
get_single_entry = {'tags': ['datastores/v1'], 'summary': 'Returns the specified datastore entry for the specified store, or null if it does not exist (PUBLIC)', 'description': '', 'operationId': 'getSingleEntry', 'produces': ['application/json'], 'parameters': [{'name': 'dataStore', 'in': 'path', 'description': 'Store name', 'required': True, 'type': 'str'}, {'name': 'key', 'in': 'path', 'description': 'Key to search', 'required': True, 'type': 'str'}, {'name': 'customerID', 'in': 'query', 'description': 'Search specified customer store for this key (default is users customer)', 'required': False, 'type': 'int'}, {'name': 'includeDeleted', 'in': 'query', 'description': 'Include deleted/expired key', 'required': False, 'type': 'bool', 'default': False}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'dataStoreName': {'type': 'string'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'lastUpdatedTimestamp': {'type': 'int'}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'key': {'type': 'string'}, 'value': {'type': 'string'}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Store not found'}, '412': {'description': 'Validation error'}}}
put_data_store_entries = {'tags': ['datastores/v1'], 'summary': 'Updates the provided datastore entries for the specified store. (PUBLIC)', 'description': '', 'operationId': 'putDataStoreEntries', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'name': 'dataStore', 'in': 'path', 'description': 'Store name', 'required': True, 'type': 'str'}, {'in': 'body', 'name': 'body', 'description': 'Request specifying data to add', 'required': False, 'schema': {'type': 'object', 'required': ['entries'], 'properties': {'customerID': {'type': 'int', 'position': 0, 'description': 'ID of customer to bind data to. If not set, default is to bind to the current users customer (or none, if datastore is global) ', 'minimum': 0}, 'entries': {'type': 'list', 'position': 0, 'description': 'Entries to add ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['key'], 'properties': {'value': {'type': 'str', 'position': 0, 'description': 'Map value. Not valid when writing data to list stores. ', 'readOnly': True, 'minLength': 0, 'maxLength': 2048}, 'key': {'type': 'str', 'position': 0, 'description': 'List entry or map key. ', 'minLength': 0, 'maxLength': 255}}}, 'maxItems': 2147483647, 'minItems': 1}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'dataStoreName': {'type': 'string'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'lastUpdatedTimestamp': {'type': 'int'}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'key': {'type': 'string'}, 'value': {'type': 'string'}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Store not found'}, '412': {'description': 'Validation error'}}}
put_single_data_store_entry = {'tags': ['datastores/v1'], 'summary': 'Adds the provided datastore entry for the specified store. To use for lists (key, no value) (PUBLIC)', 'description': '', 'operationId': 'putSingleDataStoreEntry', 'produces': ['application/json'], 'parameters': [{'name': 'dataStore', 'in': 'path', 'description': 'Store name', 'required': True, 'type': 'str'}, {'name': 'key', 'in': 'path', 'description': 'Datastore key to set', 'required': True, 'type': 'str'}, {'name': 'customerID', 'in': 'query', 'description': 'Specify datastore to put entry to (default is users customer)', 'required': False, 'type': 'int', 'minimum': 0}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'dataStoreName': {'type': 'string'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'lastUpdatedTimestamp': {'type': 'int'}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'key': {'type': 'string'}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Store not found'}, '412': {'description': 'Validation error'}}}
put_single_data_store_entry_1 = {'tags': ['datastores/v1'], 'summary': 'Updates the provided datastore entry for the specified store. To use for maps (key with value). (PUBLIC)', 'description': '', 'operationId': 'putSingleDataStoreEntry_1', 'produces': ['application/json'], 'parameters': [{'name': 'dataStore', 'in': 'path', 'description': 'Store name', 'required': True, 'type': 'str'}, {'name': 'key', 'in': 'path', 'description': 'Datastore key to set', 'required': True, 'type': 'str'}, {'name': 'value', 'in': 'path', 'description': 'Datastore value to set', 'required': True, 'type': 'str'}, {'name': 'customerID', 'in': 'query', 'description': 'Specify datastore to put entry to (default is users customer)', 'required': False, 'type': 'int', 'minimum': 0}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'dataStoreName': {'type': 'string'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'lastUpdatedTimestamp': {'type': 'int'}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'key': {'type': 'string'}, 'value': {'type': 'string'}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['DELETED']}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Store not found'}, '412': {'description': 'Validation error'}}}