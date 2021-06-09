"""Autogenerated API schema"""
from argus_api import session


add_document_fragment = {'tags': ['documents/v1'], 'summary': 'Upload next fragment of data to a prepared document.Fragments MUST be uploaded in order, first fragment with index 0. (DEV)', 'description': 'Submit document fragment as raw data to this request.', 'operationId': 'addDocumentFragment', 'consumes': ['*'], 'produces': ['application/json'], 'parameters': [{'name': 'documentID', 'in': 'path', 'description': 'Document ID (as returned from the prepare endpoint)', 'required': True, 'type': 'int', 'minimum': 1}, {'name': 'idx', 'in': 'path', 'description': 'Fragment index', 'required': True, 'type': 'int'}, {'in': 'body', 'name': 'body', 'required': False, 'schema': {'type': 'object'}}], 'responses': {'201': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'Unique identifier of the folder/document '}, 'state': {'type': 'str', 'position': 0, 'description': 'Current state of the document ', 'enum': ['draft', 'published', 'discarded', 'incomplete']}, 'accessMode': {'type': 'str', 'position': 0, 'description': 'General access mode of the folder/document ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}, 'effectiveAccessMode': {'type': 'str', 'position': 0, 'description': 'Effective access mode of the folder/document ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}, 'currentUserAccessLevel': {'type': 'str', 'position': 0, 'description': 'Access level granted to the user viewing the folder/document ', 'enum': ['none', 'folder', 'read', 'write']}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the folder/document '}, 'masterID': {'type': 'int', 'position': 0, 'description': 'Points to the master document of this revision '}, 'revision': {'type': 'int', 'position': 0, 'description': 'Revision count '}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'createdTimestamp': {'type': 'int', 'position': 0, 'description': 'When the folder/document was created '}, 'createdByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'lastUpdatedTimestamp': {'type': 'int', 'position': 0, 'description': 'When the folder/document was last updated '}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'publishedTimestamp': {'type': 'int', 'position': 0, 'description': 'When the document was published '}, 'publishDueTimestamp': {'type': 'int', 'position': 0, 'description': 'When the document must be published (due date) '}, 'lockedUntilTimestamp': {'type': 'int', 'position': 0, 'description': 'Until when the document is locked '}, 'ownedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'lockedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'publishedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'mimeType': {'type': 'str', 'position': 0, 'description': 'MIME type of the document content '}, 'dataSize': {'type': 'int', 'position': 0, 'description': 'Size of the document content in bytes '}, 'sha256': {'type': 'str', 'position': 0, 'description': 'SHA256 digest of this document '}, 'labels': {'type': 'list', 'position': 0, 'description': 'Free-text labels assigned to the document ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'parentElements': {'type': 'list', 'position': 0, 'description': "Full path of the folder's/document's parent folders (ordered from root to parent folder; empty if root folder) ", 'items': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'Unique identifier of the folder '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the folder '}, 'accessMode': {'type': 'str', 'position': 0, 'description': 'The configured access mode set on this folder ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}}}}, 'currentUserLockStatus': {'type': 'str', 'position': 0, 'description': 'The lock status of this document, for the current user. ', 'enum': ['unlocked', 'lockedOtherUser', 'lockedCurrentUser', 'lockedOtherUserCanOverride']}, 'elementType': {'type': 'str', 'position': 0, 'description': "Will be 'document' ", 'enum': ['document', 'folder']}, 'documentType': {'type': 'str', 'position': 0, 'description': "Will be 'document' ", 'enum': ['document']}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ATTACHMENT', 'CONTROLLED_VERSION', 'UNCOMMITTED', 'LOCKED_BY_CURRENTUSER']}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Specified document ID does not exist'}, '412': {'description': 'Validation failed'}}}
complete_document_upload = {'tags': ['documents/v1'], 'summary': 'Finalize upload of document.Completion request must specify correct checksum and document size. (DEV)', 'description': 'Finalize upload of document', 'operationId': 'completeDocumentUpload', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'name': 'documentID', 'in': 'path', 'description': 'Document ID (as returned from the prepare endpoint)', 'required': True, 'type': 'int', 'minimum': 1}, {'in': 'body', 'name': 'body', 'description': 'Completion request', 'required': False, 'schema': {'type': 'object', 'required': ['sha256'], 'properties': {'documentID': {'type': 'int', 'position': 0, 'description': 'ID of the document to complete. '}, 'sha256': {'type': 'str', 'position': 0, 'description': 'The sha256 of the entire document. '}, 'notificationOptions': {'type': 'dict', 'properties': {'skip': {'type': 'bool', 'position': 0, 'description': 'If true, skip notification for current operation. '}}}}}}], 'responses': {'201': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'Unique identifier of the folder/document '}, 'state': {'type': 'str', 'position': 0, 'description': 'Current state of the document ', 'enum': ['draft', 'published', 'discarded', 'incomplete']}, 'accessMode': {'type': 'str', 'position': 0, 'description': 'General access mode of the folder/document ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}, 'effectiveAccessMode': {'type': 'str', 'position': 0, 'description': 'Effective access mode of the folder/document ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}, 'currentUserAccessLevel': {'type': 'str', 'position': 0, 'description': 'Access level granted to the user viewing the folder/document ', 'enum': ['none', 'folder', 'read', 'write']}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the folder/document '}, 'masterID': {'type': 'int', 'position': 0, 'description': 'Points to the master document of this revision '}, 'revision': {'type': 'int', 'position': 0, 'description': 'Revision count '}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'createdTimestamp': {'type': 'int', 'position': 0, 'description': 'When the folder/document was created '}, 'createdByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'lastUpdatedTimestamp': {'type': 'int', 'position': 0, 'description': 'When the folder/document was last updated '}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'publishedTimestamp': {'type': 'int', 'position': 0, 'description': 'When the document was published '}, 'publishDueTimestamp': {'type': 'int', 'position': 0, 'description': 'When the document must be published (due date) '}, 'lockedUntilTimestamp': {'type': 'int', 'position': 0, 'description': 'Until when the document is locked '}, 'ownedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'lockedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'publishedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'mimeType': {'type': 'str', 'position': 0, 'description': 'MIME type of the document content '}, 'dataSize': {'type': 'int', 'position': 0, 'description': 'Size of the document content in bytes '}, 'sha256': {'type': 'str', 'position': 0, 'description': 'SHA256 digest of this document '}, 'labels': {'type': 'list', 'position': 0, 'description': 'Free-text labels assigned to the document ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'parentElements': {'type': 'list', 'position': 0, 'description': "Full path of the folder's/document's parent folders (ordered from root to parent folder; empty if root folder) ", 'items': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'Unique identifier of the folder '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the folder '}, 'accessMode': {'type': 'str', 'position': 0, 'description': 'The configured access mode set on this folder ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}}}}, 'currentUserLockStatus': {'type': 'str', 'position': 0, 'description': 'The lock status of this document, for the current user. ', 'enum': ['unlocked', 'lockedOtherUser', 'lockedCurrentUser', 'lockedOtherUserCanOverride']}, 'elementType': {'type': 'str', 'position': 0, 'description': "Will be 'document' ", 'enum': ['document', 'folder']}, 'documentType': {'type': 'str', 'position': 0, 'description': "Will be 'document' ", 'enum': ['document']}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ATTACHMENT', 'CONTROLLED_VERSION', 'UNCOMMITTED', 'LOCKED_BY_CURRENTUSER']}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Specified document ID does not exist'}, '412': {'description': 'Validation failed'}}}
disard_document_upload = {'tags': ['documents/v1'], 'summary': 'Abort and discard fragmented upload. (DEV)', 'description': '', 'operationId': 'disardDocumentUpload', 'produces': ['application/json'], 'parameters': [{'name': 'documentID', 'in': 'path', 'description': 'Document ID (as returned from the prepare endpoint)', 'required': True, 'type': 'int', 'minimum': 1}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'Unique identifier of the folder/document '}, 'state': {'type': 'str', 'position': 0, 'description': 'Current state of the document ', 'enum': ['draft', 'published', 'discarded', 'incomplete']}, 'accessMode': {'type': 'str', 'position': 0, 'description': 'General access mode of the folder/document ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}, 'effectiveAccessMode': {'type': 'str', 'position': 0, 'description': 'Effective access mode of the folder/document ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}, 'currentUserAccessLevel': {'type': 'str', 'position': 0, 'description': 'Access level granted to the user viewing the folder/document ', 'enum': ['none', 'folder', 'read', 'write']}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the folder/document '}, 'masterID': {'type': 'int', 'position': 0, 'description': 'Points to the master document of this revision '}, 'revision': {'type': 'int', 'position': 0, 'description': 'Revision count '}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'createdTimestamp': {'type': 'int', 'position': 0, 'description': 'When the folder/document was created '}, 'createdByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'lastUpdatedTimestamp': {'type': 'int', 'position': 0, 'description': 'When the folder/document was last updated '}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'publishedTimestamp': {'type': 'int', 'position': 0, 'description': 'When the document was published '}, 'publishDueTimestamp': {'type': 'int', 'position': 0, 'description': 'When the document must be published (due date) '}, 'lockedUntilTimestamp': {'type': 'int', 'position': 0, 'description': 'Until when the document is locked '}, 'ownedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'lockedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'publishedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'mimeType': {'type': 'str', 'position': 0, 'description': 'MIME type of the document content '}, 'dataSize': {'type': 'int', 'position': 0, 'description': 'Size of the document content in bytes '}, 'sha256': {'type': 'str', 'position': 0, 'description': 'SHA256 digest of this document '}, 'labels': {'type': 'list', 'position': 0, 'description': 'Free-text labels assigned to the document ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'parentElements': {'type': 'list', 'position': 0, 'description': "Full path of the folder's/document's parent folders (ordered from root to parent folder; empty if root folder) ", 'items': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'Unique identifier of the folder '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the folder '}, 'accessMode': {'type': 'str', 'position': 0, 'description': 'The configured access mode set on this folder ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}}}}, 'currentUserLockStatus': {'type': 'str', 'position': 0, 'description': 'The lock status of this document, for the current user. ', 'enum': ['unlocked', 'lockedOtherUser', 'lockedCurrentUser', 'lockedOtherUserCanOverride']}, 'elementType': {'type': 'str', 'position': 0, 'description': "Will be 'document' ", 'enum': ['document', 'folder']}, 'documentType': {'type': 'str', 'position': 0, 'description': "Will be 'document' ", 'enum': ['document']}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ATTACHMENT', 'CONTROLLED_VERSION', 'UNCOMMITTED', 'LOCKED_BY_CURRENTUSER']}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Specified document ID does not exist'}, '412': {'description': 'Validation failed'}}}
prepare_upload = {'tags': ['documents/v1'], 'summary': 'Prepare upload of a new document (DEV)', 'description': 'Invoke this endpoint to prepare for fragmented document upload.Use the returned document ID to upload and complete fragments.', 'operationId': 'prepareUpload', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'Document prepare upload request', 'required': False, 'schema': {'type': 'object', 'required': ['accessMode', 'inheritExplicitPermissions', 'mimeType', 'name'], 'properties': {'parentFolderID': {'type': 'int'}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of new document  => Sanitize by regex \\A[^\\\\\\/:*"\'?<>|]{1,254}\\z'}, 'mimeType': {'type': 'str', 'position': 0, 'description': 'MIME type of document content '}, 'accessMode': {'type': 'str', 'position': 0, 'description': 'General access mode of new document (default roleBased)', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}, 'lockRequestTime': {'type': 'int', 'position': 0, 'description': 'Specify how long the document should be locked (default 0)', 'default': 0}, 'inheritExplicitPermissions': {'type': 'bool', 'position': 0, 'description': 'Inherit explicit permissions from parent folder (default false)', 'default': False}, 'overwriteExisting': {'type': 'bool', 'position': 0, 'description': 'If true, overwrite existing document with same name in parent folder, as a new revision. '}}}}], 'responses': {'201': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'Unique identifier of the folder/document '}, 'state': {'type': 'str', 'position': 0, 'description': 'Current state of the document ', 'enum': ['draft', 'published', 'discarded', 'incomplete']}, 'accessMode': {'type': 'str', 'position': 0, 'description': 'General access mode of the folder/document ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}, 'effectiveAccessMode': {'type': 'str', 'position': 0, 'description': 'Effective access mode of the folder/document ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}, 'currentUserAccessLevel': {'type': 'str', 'position': 0, 'description': 'Access level granted to the user viewing the folder/document ', 'enum': ['none', 'folder', 'read', 'write']}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the folder/document '}, 'masterID': {'type': 'int', 'position': 0, 'description': 'Points to the master document of this revision '}, 'revision': {'type': 'int', 'position': 0, 'description': 'Revision count '}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'createdTimestamp': {'type': 'int', 'position': 0, 'description': 'When the folder/document was created '}, 'createdByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'lastUpdatedTimestamp': {'type': 'int', 'position': 0, 'description': 'When the folder/document was last updated '}, 'lastUpdatedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'publishedTimestamp': {'type': 'int', 'position': 0, 'description': 'When the document was published '}, 'publishDueTimestamp': {'type': 'int', 'position': 0, 'description': 'When the document must be published (due date) '}, 'lockedUntilTimestamp': {'type': 'int', 'position': 0, 'description': 'Until when the document is locked '}, 'ownedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'lockedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'publishedByUser': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'mimeType': {'type': 'str', 'position': 0, 'description': 'MIME type of the document content '}, 'dataSize': {'type': 'int', 'position': 0, 'description': 'Size of the document content in bytes '}, 'sha256': {'type': 'str', 'position': 0, 'description': 'SHA256 digest of this document '}, 'labels': {'type': 'list', 'position': 0, 'description': 'Free-text labels assigned to the document ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'parentElements': {'type': 'list', 'position': 0, 'description': "Full path of the folder's/document's parent folders (ordered from root to parent folder; empty if root folder) ", 'items': {'type': 'dict', 'properties': {'id': {'type': 'int', 'position': 0, 'description': 'Unique identifier of the folder '}, 'name': {'type': 'str', 'position': 0, 'description': 'Name of the folder '}, 'accessMode': {'type': 'str', 'position': 0, 'description': 'The configured access mode set on this folder ', 'enum': ['roleBased', 'writeRestricted', 'readRestricted', 'explicit']}}}}, 'currentUserLockStatus': {'type': 'str', 'position': 0, 'description': 'The lock status of this document, for the current user. ', 'enum': ['unlocked', 'lockedOtherUser', 'lockedCurrentUser', 'lockedOtherUserCanOverride']}, 'elementType': {'type': 'str', 'position': 0, 'description': "Will be 'document' ", 'enum': ['document', 'folder']}, 'documentType': {'type': 'str', 'position': 0, 'description': "Will be 'document' ", 'enum': ['document']}, 'flags': {'type': 'list', 'position': 0, 'description': 'Flags assigned to the object. ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ATTACHMENT', 'CONTROLLED_VERSION', 'UNCOMMITTED', 'LOCKED_BY_CURRENTUSER']}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Parent folder not found'}, '412': {'description': 'Validation failed'}}}