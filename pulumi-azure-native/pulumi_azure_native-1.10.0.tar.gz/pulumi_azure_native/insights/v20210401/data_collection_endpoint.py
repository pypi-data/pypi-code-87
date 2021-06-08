# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['DataCollectionEndpointArgs', 'DataCollectionEndpoint']

@pulumi.input_type
class DataCollectionEndpointArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 data_collection_endpoint_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 immutable_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'KnownDataCollectionEndpointResourceKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_acls: Optional[pulumi.Input['DataCollectionEndpointNetworkAclsArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DataCollectionEndpoint resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] data_collection_endpoint_name: The name of the data collection endpoint. The name is case insensitive.
        :param pulumi.Input[str] description: Description of the data collection endpoint.
        :param pulumi.Input[str] immutable_id: The immutable ID of this data collection endpoint resource. This property is READ-ONLY.
        :param pulumi.Input[Union[str, 'KnownDataCollectionEndpointResourceKind']] kind: The kind of the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives.
        :param pulumi.Input['DataCollectionEndpointNetworkAclsArgs'] network_acls: Network access control rules for the endpoints.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if data_collection_endpoint_name is not None:
            pulumi.set(__self__, "data_collection_endpoint_name", data_collection_endpoint_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if immutable_id is not None:
            pulumi.set(__self__, "immutable_id", immutable_id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_acls is not None:
            pulumi.set(__self__, "network_acls", network_acls)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dataCollectionEndpointName")
    def data_collection_endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the data collection endpoint. The name is case insensitive.
        """
        return pulumi.get(self, "data_collection_endpoint_name")

    @data_collection_endpoint_name.setter
    def data_collection_endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_collection_endpoint_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the data collection endpoint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> Optional[pulumi.Input[str]]:
        """
        The immutable ID of this data collection endpoint resource. This property is READ-ONLY.
        """
        return pulumi.get(self, "immutable_id")

    @immutable_id.setter
    def immutable_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "immutable_id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'KnownDataCollectionEndpointResourceKind']]]:
        """
        The kind of the resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'KnownDataCollectionEndpointResourceKind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[pulumi.Input['DataCollectionEndpointNetworkAclsArgs']]:
        """
        Network access control rules for the endpoints.
        """
        return pulumi.get(self, "network_acls")

    @network_acls.setter
    def network_acls(self, value: Optional[pulumi.Input['DataCollectionEndpointNetworkAclsArgs']]):
        pulumi.set(self, "network_acls", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class DataCollectionEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_collection_endpoint_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 immutable_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'KnownDataCollectionEndpointResourceKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_acls: Optional[pulumi.Input[pulumi.InputType['DataCollectionEndpointNetworkAclsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Definition of ARM tracked top level resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_collection_endpoint_name: The name of the data collection endpoint. The name is case insensitive.
        :param pulumi.Input[str] description: Description of the data collection endpoint.
        :param pulumi.Input[str] immutable_id: The immutable ID of this data collection endpoint resource. This property is READ-ONLY.
        :param pulumi.Input[Union[str, 'KnownDataCollectionEndpointResourceKind']] kind: The kind of the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives.
        :param pulumi.Input[pulumi.InputType['DataCollectionEndpointNetworkAclsArgs']] network_acls: Network access control rules for the endpoints.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataCollectionEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of ARM tracked top level resource.

        :param str resource_name: The name of the resource.
        :param DataCollectionEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataCollectionEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_collection_endpoint_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 immutable_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'KnownDataCollectionEndpointResourceKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_acls: Optional[pulumi.Input[pulumi.InputType['DataCollectionEndpointNetworkAclsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = DataCollectionEndpointArgs.__new__(DataCollectionEndpointArgs)

            __props__.__dict__["data_collection_endpoint_name"] = data_collection_endpoint_name
            __props__.__dict__["description"] = description
            __props__.__dict__["immutable_id"] = immutable_id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["network_acls"] = network_acls
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["configuration_access"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["logs_ingestion"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:insights/v20210401:DataCollectionEndpoint"), pulumi.Alias(type_="azure-native:insights:DataCollectionEndpoint"), pulumi.Alias(type_="azure-nextgen:insights:DataCollectionEndpoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DataCollectionEndpoint, __self__).__init__(
            'azure-native:insights/v20210401:DataCollectionEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataCollectionEndpoint':
        """
        Get an existing DataCollectionEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataCollectionEndpointArgs.__new__(DataCollectionEndpointArgs)

        __props__.__dict__["configuration_access"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["immutable_id"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["logs_ingestion"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_acls"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return DataCollectionEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configurationAccess")
    def configuration_access(self) -> pulumi.Output[Optional['outputs.DataCollectionEndpointResponseConfigurationAccess']]:
        """
        The endpoint used by agents to access their configuration.
        """
        return pulumi.get(self, "configuration_access")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the data collection endpoint.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Resource entity tag (ETag).
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> pulumi.Output[Optional[str]]:
        """
        The immutable ID of this data collection endpoint resource. This property is READ-ONLY.
        """
        return pulumi.get(self, "immutable_id")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The kind of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logsIngestion")
    def logs_ingestion(self) -> pulumi.Output[Optional['outputs.DataCollectionEndpointResponseLogsIngestion']]:
        """
        The endpoint used by clients to ingest logs.
        """
        return pulumi.get(self, "logs_ingestion")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> pulumi.Output[Optional['outputs.DataCollectionEndpointResponseNetworkAcls']]:
        """
        Network access control rules for the endpoints.
        """
        return pulumi.get(self, "network_acls")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The resource provisioning state. This property is READ-ONLY.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.DataCollectionEndpointResourceResponseSystemData']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

