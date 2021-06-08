# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ACIServiceArgs', 'ACIService']

@pulumi.input_type
class ACIServiceArgs:
    def __init__(__self__, *,
                 compute_type: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 app_insights_enabled: Optional[pulumi.Input[bool]] = None,
                 auth_enabled: Optional[pulumi.Input[bool]] = None,
                 cname: Optional[pulumi.Input[str]] = None,
                 container_resource_requirements: Optional[pulumi.Input['ContainerResourceRequirementsArgs']] = None,
                 data_collection: Optional[pulumi.Input['ACIServiceCreateRequestDataCollectionArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_name_label: Optional[pulumi.Input[str]] = None,
                 encryption_properties: Optional[pulumi.Input['ACIServiceCreateRequestEncryptionPropertiesArgs']] = None,
                 environment_image_request: Optional[pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs']] = None,
                 keys: Optional[pulumi.Input['CreateServiceRequestKeysArgs']] = None,
                 kv_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 ssl_certificate: Optional[pulumi.Input[str]] = None,
                 ssl_enabled: Optional[pulumi.Input[bool]] = None,
                 ssl_key: Optional[pulumi.Input[str]] = None,
                 vnet_configuration: Optional[pulumi.Input['ACIServiceCreateRequestVnetConfigurationArgs']] = None):
        """
        The set of arguments for constructing a ACIService resource.
        :param pulumi.Input[str] compute_type: The compute environment type for the service.
               Expected value is 'ACI'.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[bool] app_insights_enabled: Whether or not Application Insights is enabled.
        :param pulumi.Input[bool] auth_enabled: Whether or not authentication is enabled on the service.
        :param pulumi.Input[str] cname: The CName for the service.
        :param pulumi.Input['ContainerResourceRequirementsArgs'] container_resource_requirements: The container resource requirements.
        :param pulumi.Input['ACIServiceCreateRequestDataCollectionArgs'] data_collection: Details of the data collection options specified.
        :param pulumi.Input[str] description: The description of the service.
        :param pulumi.Input[str] dns_name_label: The Dns label for the service.
        :param pulumi.Input['ACIServiceCreateRequestEncryptionPropertiesArgs'] encryption_properties: The encryption properties.
        :param pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs'] environment_image_request: The Environment, models and assets needed for inferencing.
        :param pulumi.Input['CreateServiceRequestKeysArgs'] keys: The authentication keys.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] kv_tags: The service tag dictionary. Tags are mutable.
        :param pulumi.Input[str] location: The name of the Azure location/region.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The service properties dictionary. Properties are immutable.
        :param pulumi.Input[str] service_name: Name of the Azure Machine Learning service.
        :param pulumi.Input[str] ssl_certificate: The public SSL certificate in PEM format to use if SSL is enabled.
        :param pulumi.Input[bool] ssl_enabled: Whether or not SSL is enabled.
        :param pulumi.Input[str] ssl_key: The public SSL key in PEM format for the certificate.
        :param pulumi.Input['ACIServiceCreateRequestVnetConfigurationArgs'] vnet_configuration: The virtual network configuration.
        """
        pulumi.set(__self__, "compute_type", 'ACI')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if app_insights_enabled is None:
            app_insights_enabled = False
        if app_insights_enabled is not None:
            pulumi.set(__self__, "app_insights_enabled", app_insights_enabled)
        if auth_enabled is None:
            auth_enabled = False
        if auth_enabled is not None:
            pulumi.set(__self__, "auth_enabled", auth_enabled)
        if cname is not None:
            pulumi.set(__self__, "cname", cname)
        if container_resource_requirements is not None:
            pulumi.set(__self__, "container_resource_requirements", container_resource_requirements)
        if data_collection is not None:
            pulumi.set(__self__, "data_collection", data_collection)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dns_name_label is not None:
            pulumi.set(__self__, "dns_name_label", dns_name_label)
        if encryption_properties is not None:
            pulumi.set(__self__, "encryption_properties", encryption_properties)
        if environment_image_request is not None:
            pulumi.set(__self__, "environment_image_request", environment_image_request)
        if keys is not None:
            pulumi.set(__self__, "keys", keys)
        if kv_tags is not None:
            pulumi.set(__self__, "kv_tags", kv_tags)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if ssl_certificate is not None:
            pulumi.set(__self__, "ssl_certificate", ssl_certificate)
        if ssl_enabled is None:
            ssl_enabled = False
        if ssl_enabled is not None:
            pulumi.set(__self__, "ssl_enabled", ssl_enabled)
        if ssl_key is not None:
            pulumi.set(__self__, "ssl_key", ssl_key)
        if vnet_configuration is not None:
            pulumi.set(__self__, "vnet_configuration", vnet_configuration)

    @property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[str]:
        """
        The compute environment type for the service.
        Expected value is 'ACI'.
        """
        return pulumi.get(self, "compute_type")

    @compute_type.setter
    def compute_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "compute_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group in which workspace is located.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        Name of Azure Machine Learning workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="appInsightsEnabled")
    def app_insights_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not Application Insights is enabled.
        """
        return pulumi.get(self, "app_insights_enabled")

    @app_insights_enabled.setter
    def app_insights_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "app_insights_enabled", value)

    @property
    @pulumi.getter(name="authEnabled")
    def auth_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not authentication is enabled on the service.
        """
        return pulumi.get(self, "auth_enabled")

    @auth_enabled.setter
    def auth_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auth_enabled", value)

    @property
    @pulumi.getter
    def cname(self) -> Optional[pulumi.Input[str]]:
        """
        The CName for the service.
        """
        return pulumi.get(self, "cname")

    @cname.setter
    def cname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cname", value)

    @property
    @pulumi.getter(name="containerResourceRequirements")
    def container_resource_requirements(self) -> Optional[pulumi.Input['ContainerResourceRequirementsArgs']]:
        """
        The container resource requirements.
        """
        return pulumi.get(self, "container_resource_requirements")

    @container_resource_requirements.setter
    def container_resource_requirements(self, value: Optional[pulumi.Input['ContainerResourceRequirementsArgs']]):
        pulumi.set(self, "container_resource_requirements", value)

    @property
    @pulumi.getter(name="dataCollection")
    def data_collection(self) -> Optional[pulumi.Input['ACIServiceCreateRequestDataCollectionArgs']]:
        """
        Details of the data collection options specified.
        """
        return pulumi.get(self, "data_collection")

    @data_collection.setter
    def data_collection(self, value: Optional[pulumi.Input['ACIServiceCreateRequestDataCollectionArgs']]):
        pulumi.set(self, "data_collection", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the service.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dnsNameLabel")
    def dns_name_label(self) -> Optional[pulumi.Input[str]]:
        """
        The Dns label for the service.
        """
        return pulumi.get(self, "dns_name_label")

    @dns_name_label.setter
    def dns_name_label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_name_label", value)

    @property
    @pulumi.getter(name="encryptionProperties")
    def encryption_properties(self) -> Optional[pulumi.Input['ACIServiceCreateRequestEncryptionPropertiesArgs']]:
        """
        The encryption properties.
        """
        return pulumi.get(self, "encryption_properties")

    @encryption_properties.setter
    def encryption_properties(self, value: Optional[pulumi.Input['ACIServiceCreateRequestEncryptionPropertiesArgs']]):
        pulumi.set(self, "encryption_properties", value)

    @property
    @pulumi.getter(name="environmentImageRequest")
    def environment_image_request(self) -> Optional[pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs']]:
        """
        The Environment, models and assets needed for inferencing.
        """
        return pulumi.get(self, "environment_image_request")

    @environment_image_request.setter
    def environment_image_request(self, value: Optional[pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs']]):
        pulumi.set(self, "environment_image_request", value)

    @property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input['CreateServiceRequestKeysArgs']]:
        """
        The authentication keys.
        """
        return pulumi.get(self, "keys")

    @keys.setter
    def keys(self, value: Optional[pulumi.Input['CreateServiceRequestKeysArgs']]):
        pulumi.set(self, "keys", value)

    @property
    @pulumi.getter(name="kvTags")
    def kv_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The service tag dictionary. Tags are mutable.
        """
        return pulumi.get(self, "kv_tags")

    @kv_tags.setter
    def kv_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "kv_tags", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Azure location/region.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The service properties dictionary. Properties are immutable.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Azure Machine Learning service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="sslCertificate")
    def ssl_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The public SSL certificate in PEM format to use if SSL is enabled.
        """
        return pulumi.get(self, "ssl_certificate")

    @ssl_certificate.setter
    def ssl_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_certificate", value)

    @property
    @pulumi.getter(name="sslEnabled")
    def ssl_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not SSL is enabled.
        """
        return pulumi.get(self, "ssl_enabled")

    @ssl_enabled.setter
    def ssl_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ssl_enabled", value)

    @property
    @pulumi.getter(name="sslKey")
    def ssl_key(self) -> Optional[pulumi.Input[str]]:
        """
        The public SSL key in PEM format for the certificate.
        """
        return pulumi.get(self, "ssl_key")

    @ssl_key.setter
    def ssl_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_key", value)

    @property
    @pulumi.getter(name="vnetConfiguration")
    def vnet_configuration(self) -> Optional[pulumi.Input['ACIServiceCreateRequestVnetConfigurationArgs']]:
        """
        The virtual network configuration.
        """
        return pulumi.get(self, "vnet_configuration")

    @vnet_configuration.setter
    def vnet_configuration(self, value: Optional[pulumi.Input['ACIServiceCreateRequestVnetConfigurationArgs']]):
        pulumi.set(self, "vnet_configuration", value)


class ACIService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_insights_enabled: Optional[pulumi.Input[bool]] = None,
                 auth_enabled: Optional[pulumi.Input[bool]] = None,
                 cname: Optional[pulumi.Input[str]] = None,
                 compute_type: Optional[pulumi.Input[str]] = None,
                 container_resource_requirements: Optional[pulumi.Input[pulumi.InputType['ContainerResourceRequirementsArgs']]] = None,
                 data_collection: Optional[pulumi.Input[pulumi.InputType['ACIServiceCreateRequestDataCollectionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_name_label: Optional[pulumi.Input[str]] = None,
                 encryption_properties: Optional[pulumi.Input[pulumi.InputType['ACIServiceCreateRequestEncryptionPropertiesArgs']]] = None,
                 environment_image_request: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestEnvironmentImageRequestArgs']]] = None,
                 keys: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestKeysArgs']]] = None,
                 kv_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 ssl_certificate: Optional[pulumi.Input[str]] = None,
                 ssl_enabled: Optional[pulumi.Input[bool]] = None,
                 ssl_key: Optional[pulumi.Input[str]] = None,
                 vnet_configuration: Optional[pulumi.Input[pulumi.InputType['ACIServiceCreateRequestVnetConfigurationArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Machine Learning service object wrapped into ARM resource envelope.
        API Version: 2021-01-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] app_insights_enabled: Whether or not Application Insights is enabled.
        :param pulumi.Input[bool] auth_enabled: Whether or not authentication is enabled on the service.
        :param pulumi.Input[str] cname: The CName for the service.
        :param pulumi.Input[str] compute_type: The compute environment type for the service.
               Expected value is 'ACI'.
        :param pulumi.Input[pulumi.InputType['ContainerResourceRequirementsArgs']] container_resource_requirements: The container resource requirements.
        :param pulumi.Input[pulumi.InputType['ACIServiceCreateRequestDataCollectionArgs']] data_collection: Details of the data collection options specified.
        :param pulumi.Input[str] description: The description of the service.
        :param pulumi.Input[str] dns_name_label: The Dns label for the service.
        :param pulumi.Input[pulumi.InputType['ACIServiceCreateRequestEncryptionPropertiesArgs']] encryption_properties: The encryption properties.
        :param pulumi.Input[pulumi.InputType['CreateServiceRequestEnvironmentImageRequestArgs']] environment_image_request: The Environment, models and assets needed for inferencing.
        :param pulumi.Input[pulumi.InputType['CreateServiceRequestKeysArgs']] keys: The authentication keys.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] kv_tags: The service tag dictionary. Tags are mutable.
        :param pulumi.Input[str] location: The name of the Azure location/region.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The service properties dictionary. Properties are immutable.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] service_name: Name of the Azure Machine Learning service.
        :param pulumi.Input[str] ssl_certificate: The public SSL certificate in PEM format to use if SSL is enabled.
        :param pulumi.Input[bool] ssl_enabled: Whether or not SSL is enabled.
        :param pulumi.Input[str] ssl_key: The public SSL key in PEM format for the certificate.
        :param pulumi.Input[pulumi.InputType['ACIServiceCreateRequestVnetConfigurationArgs']] vnet_configuration: The virtual network configuration.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ACIServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Machine Learning service object wrapped into ARM resource envelope.
        API Version: 2021-01-01.

        :param str resource_name: The name of the resource.
        :param ACIServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ACIServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_insights_enabled: Optional[pulumi.Input[bool]] = None,
                 auth_enabled: Optional[pulumi.Input[bool]] = None,
                 cname: Optional[pulumi.Input[str]] = None,
                 compute_type: Optional[pulumi.Input[str]] = None,
                 container_resource_requirements: Optional[pulumi.Input[pulumi.InputType['ContainerResourceRequirementsArgs']]] = None,
                 data_collection: Optional[pulumi.Input[pulumi.InputType['ACIServiceCreateRequestDataCollectionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_name_label: Optional[pulumi.Input[str]] = None,
                 encryption_properties: Optional[pulumi.Input[pulumi.InputType['ACIServiceCreateRequestEncryptionPropertiesArgs']]] = None,
                 environment_image_request: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestEnvironmentImageRequestArgs']]] = None,
                 keys: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestKeysArgs']]] = None,
                 kv_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 ssl_certificate: Optional[pulumi.Input[str]] = None,
                 ssl_enabled: Optional[pulumi.Input[bool]] = None,
                 ssl_key: Optional[pulumi.Input[str]] = None,
                 vnet_configuration: Optional[pulumi.Input[pulumi.InputType['ACIServiceCreateRequestVnetConfigurationArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ACIServiceArgs.__new__(ACIServiceArgs)

            if app_insights_enabled is None:
                app_insights_enabled = False
            __props__.__dict__["app_insights_enabled"] = app_insights_enabled
            if auth_enabled is None:
                auth_enabled = False
            __props__.__dict__["auth_enabled"] = auth_enabled
            __props__.__dict__["cname"] = cname
            if compute_type is None and not opts.urn:
                raise TypeError("Missing required property 'compute_type'")
            __props__.__dict__["compute_type"] = 'ACI'
            __props__.__dict__["container_resource_requirements"] = container_resource_requirements
            __props__.__dict__["data_collection"] = data_collection
            __props__.__dict__["description"] = description
            __props__.__dict__["dns_name_label"] = dns_name_label
            __props__.__dict__["encryption_properties"] = encryption_properties
            __props__.__dict__["environment_image_request"] = environment_image_request
            __props__.__dict__["keys"] = keys
            __props__.__dict__["kv_tags"] = kv_tags
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["ssl_certificate"] = ssl_certificate
            if ssl_enabled is None:
                ssl_enabled = False
            __props__.__dict__["ssl_enabled"] = ssl_enabled
            __props__.__dict__["ssl_key"] = ssl_key
            __props__.__dict__["vnet_configuration"] = vnet_configuration
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["identity"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["sku"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["tags"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:machinelearningservices:ACIService"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200501preview:ACIService"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200501preview:ACIService"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200515preview:ACIService"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200515preview:ACIService"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200901preview:ACIService"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200901preview:ACIService"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210101:ACIService"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20210101:ACIService"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210301preview:ACIService"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20210301preview:ACIService"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210401:ACIService"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20210401:ACIService")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ACIService, __self__).__init__(
            'azure-native:machinelearningservices:ACIService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ACIService':
        """
        Get an existing ACIService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ACIServiceArgs.__new__(ACIServiceArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ACIService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        Service properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The sku of the workspace.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Specifies the type of the resource.
        """
        return pulumi.get(self, "type")

