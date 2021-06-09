"""Autogenerated API schema"""
from argus_api import session


get_subject_1 = {'tags': ['useradmin/v2'], 'summary': 'Returns the specified subject (PUBLIC) (PUBLIC)', 'description': '', 'operationId': 'getSubject_1', 'produces': ['application/json'], 'parameters': [{'name': 'shortNameOrId', 'in': 'path', 'description': 'ID or shortname of subject to fetch', 'required': True, 'type': 'str'}, {'name': 'domain', 'in': 'query', 'description': 'Domain ID or short name (optional, defaults to current user domain)', 'required': False, 'type': 'str'}], 'responses': {'401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '412': {'description': 'Validation error'}}}
list_subjects_1 = {'tags': ['useradmin/v2'], 'summary': 'Returns the subjects matching the query (PUBLIC)', 'description': '', 'operationId': 'listSubjects_1', 'produces': ['application/json'], 'parameters': [{'name': 'offset', 'in': 'query', 'description': 'Skip a number of results', 'required': False, 'type': 'int', 'default': 0, 'minimum': 0}, {'name': 'limit', 'in': 'query', 'description': 'Maximum number of returned results', 'required': False, 'type': 'int', 'default': 25, 'minimum': 0}, {'name': 'domain', 'in': 'query', 'description': 'Domain to search in by short name or id', 'required': False, 'type': 'list', 'items': {'type': 'string'}, 'collectionFormat': 'multi'}, {'name': 'subject', 'in': 'query', 'description': 'Subject to search for by short name or id', 'required': False, 'type': 'list', 'items': {'type': 'string'}, 'collectionFormat': 'multi'}, {'name': 'customer', 'in': 'query', 'description': 'Customer to search for by short name or id', 'required': False, 'type': 'list', 'items': {'type': 'string'}, 'collectionFormat': 'multi'}, {'name': 'includeDeleted', 'in': 'query', 'description': 'Include deleted subjects', 'required': False, 'type': 'bool', 'default': False}, {'name': 'excludeFlag', 'in': 'query', 'description': 'Exclude subjects with flag', 'required': False, 'type': 'list', 'items': {'type': 'str', 'enum': ['deleted', 'blocked', 'forcePasswordChange', 'daemonAccount', 'passwordNotSet']}, 'collectionFormat': 'multi'}, {'name': 'includeFlag', 'in': 'query', 'description': 'Include subjects with flag', 'required': False, 'type': 'list', 'items': {'type': 'str', 'enum': ['deleted', 'blocked', 'forcePasswordChange', 'daemonAccount', 'passwordNotSet']}, 'collectionFormat': 'multi'}, {'name': 'keyword', 'in': 'query', 'description': 'Search by keywords', 'required': False, 'type': 'list', 'items': {'type': 'string'}, 'collectionFormat': 'multi'}, {'name': 'keywordMatch', 'in': 'query', 'description': 'Set match strategy for keyword search', 'required': False, 'type': 'str', 'default': 'all', 'enum': ['any', 'all']}, {'name': 'keywordField', 'in': 'query', 'description': 'Set field strategy for keyword search', 'required': False, 'type': 'list', 'items': {'type': 'str', 'enum': ['shortName', 'name', 'email', 'phoneNumber']}, 'collectionFormat': 'multi'}, {'name': 'sortBy', 'in': 'query', 'description': 'Field to sort by', 'required': False, 'type': 'list', 'items': {'type': 'string'}, 'collectionFormat': 'multi'}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'shortName': {'type': 'str', 'position': 0, 'description': "The subject's short name "}, 'name': {'type': 'str', 'position': 0, 'description': "The subject's name "}, 'description': {'type': 'str', 'position': 0, 'description': "The subject's description "}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the customer. '}, 'shortName': {'type': 'str', 'position': 0, 'description': 'Shortname of the customer. '}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}}}, 'memberOf': {'type': 'list', 'position': 0, 'description': 'Groups that the subject is a member of ', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'shortName': {'type': 'str', 'position': 0, 'description': "The subject's short name "}, 'name': {'type': 'str', 'position': 0, 'description': "The subject's name "}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the customer. '}, 'shortName': {'type': 'str', 'position': 0, 'description': 'Shortname of the customer. '}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}}}}}}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags that are set for the subject ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['deleted', 'blocked', 'forcePasswordChange', 'daemonAccount', 'passwordNotSet']}}, 'createdByUser': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'shortName': {'type': 'str', 'position': 0, 'description': "The subject's short name "}, 'name': {'type': 'str', 'position': 0, 'description': "The subject's name "}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the customer. '}, 'shortName': {'type': 'str', 'position': 0, 'description': 'Shortname of the customer. '}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}}}}}, 'createdTimestamp': {'type': 'int', 'position': 0, 'description': 'The time the object was created '}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'shortName': {'type': 'str', 'position': 0, 'description': "The subject's short name "}, 'name': {'type': 'str', 'position': 0, 'description': "The subject's name "}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the customer. '}, 'shortName': {'type': 'str', 'position': 0, 'description': 'Shortname of the customer. '}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}}}}}, 'lastUpdatedTimestamp': {'type': 'int', 'position': 0, 'description': 'The time the object was last updated '}, 'deletedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'shortName': {'type': 'str', 'position': 0, 'description': "The subject's short name "}, 'name': {'type': 'str', 'position': 0, 'description': "The subject's name "}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the customer. '}, 'shortName': {'type': 'str', 'position': 0, 'description': 'Shortname of the customer. '}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}}}}}, 'deletedTimestamp': {'type': 'int', 'position': 0, 'description': 'The time the object was deleted '}, 'type': 'str', 'options': ['user', 'group']}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '412': {'description': 'Validation error'}}}
search_subjects = {'tags': ['useradmin/v2'], 'summary': 'Returns the subjects matching the query (PUBLIC)', 'description': '', 'operationId': 'searchSubjects', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'Subject search request', 'required': False, 'schema': {'type': 'object', 'required': ['keywordFieldStrategy', 'keywordMatchStrategy', 'sortBy', 'timeFieldStrategy', 'timeMatchStrategy'], 'properties': {'domain': {'type': 'list', 'position': 0, 'description': 'Restrict the search to subjects in these domains, by domain ID or name. ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'subject': {'type': 'list', 'position': 0, 'description': 'Restrict search to specific subjects, by ID or shortname ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'ancestor': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects descending from specific groups, by ID or shortname ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'parent': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects which are direct member of specific groups, by ID or shortname ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'customer': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects bound to these customers (by ID or shortname). Customer groups will resolve to all subcustomers as well. ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'type': {'type': 'str', 'position': 0, 'description': 'Limit search to one type of subject ', 'enum': ['group', 'user']}, 'sortBy': {'type': 'list', 'position': 0, 'description': 'Field to sort by (default name)', 'items': {'type': 'str', 'enum': ['id', 'name', 'shortName', 'customer', 'createdTimestamp', 'lastUpdatedTimestamp']}}, 'includeDeleted': {'type': 'bool', 'position': 0, 'description': 'Whether or not to include deleted subjects. (default false)', 'default': False}, 'includeFlags': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects having all of the specified flags. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['deleted', 'blocked', 'forcePasswordChange', 'daemonAccount', 'passwordNotSet']}}, 'excludeFlags': {'type': 'list', 'position': 0, 'description': 'Exclude subjects with these flags from the search. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['deleted', 'blocked', 'forcePasswordChange', 'daemonAccount', 'passwordNotSet']}}, 'permissions': {'type': 'list', 'position': 0, 'description': 'Limit search to subjects with one of the given permissions ', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'function': {'type': 'str', 'position': 0, 'description': 'The name or id of the function the user should have '}, 'customer': {'type': 'str', 'position': 0, 'description': 'The name or id of the customer the function should belong to. Defaults to any customer '}, 'domain': {'type': 'str', 'position': 0, 'description': 'The name or id of the domain the customer should belong to. Defaults to the current users domain '}}}}, 'keywords': {'type': 'list', 'position': 0, 'description': 'Keywords to search for ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'keywordMatchStrategy': {'type': 'str', 'position': 0, 'description': 'Search based on all keywords (AND), or based on any keyword (OR) (default Match all keywords (AND))', 'enum': ['any', 'all']}, 'keywordFieldStrategy': {'type': 'list', 'position': 0, 'description': 'Which fields will be searched for the given keyword (default All supported fields)', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['shortName', 'name', 'email', 'phoneNumber']}}, 'startTimestamp': {'type': 'int', 'position': 0, 'description': 'The start time of the search (default 0)', 'minimum': 0, 'default': 0}, 'endTimestamp': {'type': 'int', 'position': 0, 'description': 'The end time of the search (default now)', 'minimum': 0}, 'timeMatchStrategy': {'type': 'str', 'position': 0, 'description': 'Search based on all time-field (AND), or based on any time-field (OR) (default Match any field)', 'enum': ['any', 'all']}, 'timeFieldStrategy': {'type': 'list', 'position': 0, 'description': 'The fields to limit the time search to (default All fields)', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['createdTimestamp', 'lastUpdatedTimestamp', 'lastLoginTimestamp', 'deletedTimestamp']}}, 'subCriteria': {'type': 'list', 'position': 0, 'description': 'Set additional criteria with AND, OR or AND NOT ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['keywordFieldStrategy', 'keywordMatchStrategy', 'sortBy', 'timeFieldStrategy', 'timeMatchStrategy'], 'properties': {'domain': {'type': 'list', 'position': 0, 'description': 'Restrict the search to subjects in these domains, by domain ID or name. ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'subject': {'type': 'list', 'position': 0, 'description': 'Restrict search to specific subjects, by ID or shortname ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'ancestor': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects descending from specific groups, by ID or shortname ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'parent': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects which are direct member of specific groups, by ID or shortname ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'customer': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects bound to these customers (by ID or shortname). Customer groups will resolve to all subcustomers as well. ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'type': 'str', 'sortBy': {'type': 'list', 'position': 0, 'description': 'Field to sort by (default name)', 'items': {'type': 'str', 'enum': ['id', 'name', 'shortName', 'customer', 'createdTimestamp', 'lastUpdatedTimestamp']}}, 'includeDeleted': {'type': 'bool', 'position': 0, 'description': 'Whether or not to include deleted subjects. (default false)', 'default': False}, 'includeFlags': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects having all of the specified flags. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['deleted', 'blocked', 'forcePasswordChange', 'daemonAccount', 'passwordNotSet']}}, 'excludeFlags': {'type': 'list', 'position': 0, 'description': 'Exclude subjects with these flags from the search. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['deleted', 'blocked', 'forcePasswordChange', 'daemonAccount', 'passwordNotSet']}}, 'permissions': {'type': 'list', 'position': 0, 'description': 'Limit search to subjects with one of the given permissions ', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'function': {'type': 'str', 'position': 0, 'description': 'The name or id of the function the user should have '}, 'customer': {'type': 'str', 'position': 0, 'description': 'The name or id of the customer the function should belong to. Defaults to any customer '}, 'domain': {'type': 'str', 'position': 0, 'description': 'The name or id of the domain the customer should belong to. Defaults to the current users domain '}}}}, 'keywords': {'type': 'list', 'position': 0, 'description': 'Keywords to search for ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'keywordMatchStrategy': {'type': 'str', 'position': 0, 'description': 'Search based on all keywords (AND), or based on any keyword (OR) (default Match all keywords (AND))', 'enum': ['any', 'all']}, 'keywordFieldStrategy': {'type': 'list', 'position': 0, 'description': 'Which fields will be searched for the given keyword (default All supported fields)', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['shortName', 'name', 'email', 'phoneNumber']}}, 'startTimestamp': {'type': 'int', 'position': 0, 'description': 'The start time of the search (default 0)', 'minimum': 0, 'default': 0}, 'endTimestamp': {'type': 'int', 'position': 0, 'description': 'The end time of the search (default now)', 'minimum': 0}, 'timeMatchStrategy': {'type': 'str', 'position': 0, 'description': 'Search based on all time-field (AND), or based on any time-field (OR) (default Match any field)', 'enum': ['any', 'all']}, 'timeFieldStrategy': {'type': 'list', 'position': 0, 'description': 'The fields to limit the time search to (default All fields)', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['createdTimestamp', 'lastUpdatedTimestamp', 'lastLoginTimestamp', 'deletedTimestamp']}}, 'subCriteria': {'type': 'list', 'position': 0, 'description': 'Set additional criteria with AND, OR or AND NOT ', 'uniqueItems': True, 'items': {'type': 'dict', 'required': ['keywordFieldStrategy', 'keywordMatchStrategy', 'sortBy', 'timeFieldStrategy', 'timeMatchStrategy'], 'properties': {'domain': {'type': 'list', 'position': 0, 'description': 'Restrict the search to subjects in these domains, by domain ID or name. ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'subject': {'type': 'list', 'position': 0, 'description': 'Restrict search to specific subjects, by ID or shortname ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'ancestor': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects descending from specific groups, by ID or shortname ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'parent': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects which are direct member of specific groups, by ID or shortname ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'customer': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects bound to these customers (by ID or shortname). Customer groups will resolve to all subcustomers as well. ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'type': 'str', 'sortBy': {'type': 'list', 'position': 0, 'description': 'Field to sort by (default name)', 'items': {'type': 'str', 'enum': ['id', 'name', 'shortName', 'customer', 'createdTimestamp', 'lastUpdatedTimestamp']}}, 'includeDeleted': {'type': 'bool', 'position': 0, 'description': 'Whether or not to include deleted subjects. (default false)', 'default': False}, 'includeFlags': {'type': 'list', 'position': 0, 'description': 'Restrict search to subjects having all of the specified flags. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['deleted', 'blocked', 'forcePasswordChange', 'daemonAccount', 'passwordNotSet']}}, 'excludeFlags': {'type': 'list', 'position': 0, 'description': 'Exclude subjects with these flags from the search. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['deleted', 'blocked', 'forcePasswordChange', 'daemonAccount', 'passwordNotSet']}}, 'permissions': {'type': 'list', 'position': 0, 'description': 'Limit search to subjects with one of the given permissions ', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'function': {'type': 'str', 'position': 0, 'description': 'The name or id of the function the user should have '}, 'customer': {'type': 'str', 'position': 0, 'description': 'The name or id of the customer the function should belong to. Defaults to any customer '}, 'domain': {'type': 'str', 'position': 0, 'description': 'The name or id of the domain the customer should belong to. Defaults to the current users domain '}}}}, 'keywords': {'type': 'list', 'position': 0, 'description': 'Keywords to search for ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'keywordMatchStrategy': {'type': 'str', 'position': 0, 'description': 'Search based on all keywords (AND), or based on any keyword (OR) (default Match all keywords (AND))', 'enum': ['any', 'all']}, 'keywordFieldStrategy': {'type': 'list', 'position': 0, 'description': 'Which fields will be searched for the given keyword (default All supported fields)', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['shortName', 'name', 'email', 'phoneNumber']}}, 'startTimestamp': {'type': 'int', 'position': 0, 'description': 'The start time of the search (default 0)', 'minimum': 0, 'default': 0}, 'endTimestamp': {'type': 'int', 'position': 0, 'description': 'The end time of the search (default now)', 'minimum': 0}, 'timeMatchStrategy': {'type': 'str', 'position': 0, 'description': 'Search based on all time-field (AND), or based on any time-field (OR) (default Match any field)', 'enum': ['any', 'all']}, 'timeFieldStrategy': {'type': 'list', 'position': 0, 'description': 'The fields to limit the time search to (default All fields)', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['createdTimestamp', 'lastUpdatedTimestamp', 'lastLoginTimestamp', 'deletedTimestamp']}}, 'subCriteria': {'type': 'list', 'position': 0, 'description': 'Set additional criteria with AND, OR or AND NOT ', 'uniqueItems': True, 'items': []}, 'required': {'type': 'bool', 'position': 0, 'description': 'Is this subcriteria required? If false it is OR-ed, if true it is AND-ed (default false)', 'default': False}, 'exclude': {'type': 'bool', 'position': 0, 'description': 'Exclude objects matching subcriteria? If true, the criteria is NOT-ed. (default false)', 'default': False}, 'options': ['group', 'user']}}}, 'required': {'type': 'bool', 'position': 0, 'description': 'Is this subcriteria required? If false it is OR-ed, if true it is AND-ed (default false)', 'default': False}, 'exclude': {'type': 'bool', 'position': 0, 'description': 'Exclude objects matching subcriteria? If true, the criteria is NOT-ed. (default false)', 'default': False}, 'options': ['group', 'user']}}}, 'limit': {'type': 'int', 'position': 0, 'description': 'The max amount of items to display (default 25)', 'minimum': 0, 'default': 25}, 'offset': {'type': 'int', 'position': 0, 'description': 'The amount of items to skip (default 0)', 'minimum': 0, 'default': 0}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'shortName': {'type': 'str', 'position': 0, 'description': "The subject's short name "}, 'name': {'type': 'str', 'position': 0, 'description': "The subject's name "}, 'description': {'type': 'str', 'position': 0, 'description': "The subject's description "}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the customer. '}, 'shortName': {'type': 'str', 'position': 0, 'description': 'Shortname of the customer. '}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}}}, 'memberOf': {'type': 'list', 'position': 0, 'description': 'Groups that the subject is a member of ', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'shortName': {'type': 'str', 'position': 0, 'description': "The subject's short name "}, 'name': {'type': 'str', 'position': 0, 'description': "The subject's name "}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the customer. '}, 'shortName': {'type': 'str', 'position': 0, 'description': 'Shortname of the customer. '}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}}}}}}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags that are set for the subject ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['deleted', 'blocked', 'forcePasswordChange', 'daemonAccount', 'passwordNotSet']}}, 'createdByUser': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'shortName': {'type': 'str', 'position': 0, 'description': "The subject's short name "}, 'name': {'type': 'str', 'position': 0, 'description': "The subject's name "}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the customer. '}, 'shortName': {'type': 'str', 'position': 0, 'description': 'Shortname of the customer. '}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}}}}}, 'createdTimestamp': {'type': 'int', 'position': 0, 'description': 'The time the object was created '}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'shortName': {'type': 'str', 'position': 0, 'description': "The subject's short name "}, 'name': {'type': 'str', 'position': 0, 'description': "The subject's name "}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the customer. '}, 'shortName': {'type': 'str', 'position': 0, 'description': 'Shortname of the customer. '}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}}}}}, 'lastUpdatedTimestamp': {'type': 'int', 'position': 0, 'description': 'The time the object was last updated '}, 'deletedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'shortName': {'type': 'str', 'position': 0, 'description': "The subject's short name "}, 'name': {'type': 'str', 'position': 0, 'description': "The subject's name "}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the customer. '}, 'shortName': {'type': 'str', 'position': 0, 'description': 'Shortname of the customer. '}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'ID of the response object. '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the domain. '}}}}}}}, 'deletedTimestamp': {'type': 'int', 'position': 0, 'description': 'The time the object was deleted '}, 'type': 'str', 'options': ['user', 'group']}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '412': {'description': 'Validation error'}}}