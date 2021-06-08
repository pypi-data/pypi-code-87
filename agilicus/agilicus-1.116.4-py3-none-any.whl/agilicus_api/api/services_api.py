"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.06.02
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.api_client import ApiClient, Endpoint as _Endpoint
from agilicus_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from agilicus_api.model.error_message import ErrorMessage
from agilicus_api.model.list_services_response import ListServicesResponse
from agilicus_api.model.service import Service


class ServicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_service(
            self,
            service,
            **kwargs
        ):
            """Create a Service  # noqa: E501

            Creates a new Service. Note that the Service's name must be unique across all other services an Applications, regardless of the Organisation.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_service(service, async_req=True)
            >>> result = thread.get()

            Args:
                service (Service):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Service
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['service'] = \
                service
            return self.call_with_http_info(**kwargs)

        if self.create_service is None:
            self.create_service = _Endpoint(
                settings={
                    'response_type': (Service,),
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v2/services',
                    'operation_id': 'create_service',
                    'http_method': 'POST',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'service',
                    ],
                    'required': [
                        'service',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                    ]
                },
                root_map={
                    'validations': {
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'service':
                            (Service,),
                    },
                    'attribute_map': {
                    },
                    'location_map': {
                        'service': 'body',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [
                        'application/json'
                    ]
                },
                api_client=api_client,
                callable=__create_service
            )

        def __delete_service(
            self,
            service_id,
            org_id,
            **kwargs
        ):
            """Remove a Service  # noqa: E501

            Remove a Service  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_service(service_id, org_id, async_req=True)
            >>> result = thread.get()

            Args:
                service_id (str): Service unique identifier
                org_id (str): Organisation unique identifier

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['service_id'] = \
                service_id
            kwargs['org_id'] = \
                org_id
            return self.call_with_http_info(**kwargs)

        if self.delete_service is None:
            self.delete_service = _Endpoint(
                settings={
                    'response_type': None,
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v2/services/{service_id}',
                    'operation_id': 'delete_service',
                    'http_method': 'DELETE',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'service_id',
                        'org_id',
                    ],
                    'required': [
                        'service_id',
                        'org_id',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                        'service_id',
                        'org_id',
                    ]
                },
                root_map={
                    'validations': {
                        ('service_id',): {

                            'regex': {
                                'pattern': r'^[a-zA-Z0-9-]+$',  # noqa: E501
                            },
                        },
                        ('org_id',): {

                            'regex': {
                                'pattern': r'^[a-zA-Z0-9-]+$',  # noqa: E501
                            },
                        },
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'service_id':
                            (str,),
                        'org_id':
                            (str,),
                    },
                    'attribute_map': {
                        'service_id': 'service_id',
                        'org_id': 'org_id',
                    },
                    'location_map': {
                        'service_id': 'path',
                        'org_id': 'query',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__delete_service
            )

        def __get_service(
            self,
            service_id,
            **kwargs
        ):
            """Get a single Service  # noqa: E501

            Get a single Service  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_service(service_id, async_req=True)
            >>> result = thread.get()

            Args:
                service_id (str): Service unique identifier

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Service
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['service_id'] = \
                service_id
            return self.call_with_http_info(**kwargs)

        if self.get_service is None:
            self.get_service = _Endpoint(
                settings={
                    'response_type': (Service,),
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v2/services/{service_id}',
                    'operation_id': 'get_service',
                    'http_method': 'GET',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'service_id',
                    ],
                    'required': [
                        'service_id',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                        'service_id',
                    ]
                },
                root_map={
                    'validations': {
                        ('service_id',): {

                            'regex': {
                                'pattern': r'^[a-zA-Z0-9-]+$',  # noqa: E501
                            },
                        },
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'service_id':
                            (str,),
                    },
                    'attribute_map': {
                        'service_id': 'service_id',
                    },
                    'location_map': {
                        'service_id': 'path',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__get_service
            )

        def __list_services(
            self,
            **kwargs
        ):
            """Get a subset of the Services  # noqa: E501

            Retrieves all Services owned by the Organisation.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_services(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                org_id (str): Organisation Unique identifier. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListServicesResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        if self.list_services is None:
            self.list_services = _Endpoint(
                settings={
                    'response_type': (ListServicesResponse,),
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v2/services',
                    'operation_id': 'list_services',
                    'http_method': 'GET',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'org_id',
                    ],
                    'required': [],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                    ]
                },
                root_map={
                    'validations': {
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'org_id':
                            (str,),
                    },
                    'attribute_map': {
                        'org_id': 'org_id',
                    },
                    'location_map': {
                        'org_id': 'query',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__list_services
            )

        def __replace_service(
            self,
            service_id,
            **kwargs
        ):
            """Create or update a Service.  # noqa: E501

            Create or update a Service.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.replace_service(service_id, async_req=True)
            >>> result = thread.get()

            Args:
                service_id (str): Service unique identifier

            Keyword Args:
                service (Service): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Service
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['service_id'] = \
                service_id
            return self.call_with_http_info(**kwargs)

        if self.replace_service is None:
            self.replace_service = _Endpoint(
                settings={
                    'response_type': (Service,),
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v2/services/{service_id}',
                    'operation_id': 'replace_service',
                    'http_method': 'PUT',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'service_id',
                        'service',
                    ],
                    'required': [
                        'service_id',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                        'service_id',
                    ]
                },
                root_map={
                    'validations': {
                        ('service_id',): {

                            'regex': {
                                'pattern': r'^[a-zA-Z0-9-]+$',  # noqa: E501
                            },
                        },
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'service_id':
                            (str,),
                        'service':
                            (Service,),
                    },
                    'attribute_map': {
                        'service_id': 'service_id',
                    },
                    'location_map': {
                        'service_id': 'path',
                        'service': 'body',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [
                        'application/json'
                    ]
                },
                api_client=api_client,
                callable=__replace_service
            )

    create_service = None 
    delete_service = None 
    get_service = None 
    list_services = None 
    replace_service = None 
