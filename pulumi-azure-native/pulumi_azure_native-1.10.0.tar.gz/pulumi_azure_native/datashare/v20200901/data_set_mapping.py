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

__all__ = ['DataSetMappingArgs', 'DataSetMapping']

@pulumi.input_type
class DataSetMappingArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 kind: pulumi.Input[Union[str, 'DataSetMappingKind']],
                 resource_group_name: pulumi.Input[str],
                 share_subscription_name: pulumi.Input[str],
                 data_set_mapping_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataSetMapping resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[Union[str, 'DataSetMappingKind']] kind: Kind of data set mapping.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_subscription_name: The name of the share subscription which will hold the data set sink.
        :param pulumi.Input[str] data_set_mapping_name: The name of the data set mapping to be created.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "share_subscription_name", share_subscription_name)
        if data_set_mapping_name is not None:
            pulumi.set(__self__, "data_set_mapping_name", data_set_mapping_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the share account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[Union[str, 'DataSetMappingKind']]:
        """
        Kind of data set mapping.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[Union[str, 'DataSetMappingKind']]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="shareSubscriptionName")
    def share_subscription_name(self) -> pulumi.Input[str]:
        """
        The name of the share subscription which will hold the data set sink.
        """
        return pulumi.get(self, "share_subscription_name")

    @share_subscription_name.setter
    def share_subscription_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "share_subscription_name", value)

    @property
    @pulumi.getter(name="dataSetMappingName")
    def data_set_mapping_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the data set mapping to be created.
        """
        return pulumi.get(self, "data_set_mapping_name")

    @data_set_mapping_name.setter
    def data_set_mapping_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_set_mapping_name", value)


warnings.warn("""Please use one of the variants: ADLSGen2FileDataSetMapping, ADLSGen2FileSystemDataSetMapping, ADLSGen2FolderDataSetMapping, BlobContainerDataSetMapping, BlobDataSetMapping, BlobFolderDataSetMapping, KustoClusterDataSetMapping, KustoDatabaseDataSetMapping, SqlDBTableDataSetMapping, SqlDWTableDataSetMapping, SynapseWorkspaceSqlPoolTableDataSetMapping.""", DeprecationWarning)


class DataSetMapping(pulumi.CustomResource):
    warnings.warn("""Please use one of the variants: ADLSGen2FileDataSetMapping, ADLSGen2FileSystemDataSetMapping, ADLSGen2FolderDataSetMapping, BlobContainerDataSetMapping, BlobDataSetMapping, BlobFolderDataSetMapping, KustoClusterDataSetMapping, KustoDatabaseDataSetMapping, SqlDBTableDataSetMapping, SqlDWTableDataSetMapping, SynapseWorkspaceSqlPoolTableDataSetMapping.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 data_set_mapping_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'DataSetMappingKind']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A data set mapping data transfer object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] data_set_mapping_name: The name of the data set mapping to be created.
        :param pulumi.Input[Union[str, 'DataSetMappingKind']] kind: Kind of data set mapping.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_subscription_name: The name of the share subscription which will hold the data set sink.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataSetMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A data set mapping data transfer object.

        :param str resource_name: The name of the resource.
        :param DataSetMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataSetMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 data_set_mapping_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'DataSetMappingKind']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""DataSetMapping is deprecated: Please use one of the variants: ADLSGen2FileDataSetMapping, ADLSGen2FileSystemDataSetMapping, ADLSGen2FolderDataSetMapping, BlobContainerDataSetMapping, BlobDataSetMapping, BlobFolderDataSetMapping, KustoClusterDataSetMapping, KustoDatabaseDataSetMapping, SqlDBTableDataSetMapping, SqlDWTableDataSetMapping, SynapseWorkspaceSqlPoolTableDataSetMapping.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataSetMappingArgs.__new__(DataSetMappingArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["data_set_mapping_name"] = data_set_mapping_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if share_subscription_name is None and not opts.urn:
                raise TypeError("Missing required property 'share_subscription_name'")
            __props__.__dict__["share_subscription_name"] = share_subscription_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:datashare/v20200901:DataSetMapping"), pulumi.Alias(type_="azure-native:datashare:DataSetMapping"), pulumi.Alias(type_="azure-nextgen:datashare:DataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20181101preview:DataSetMapping"), pulumi.Alias(type_="azure-nextgen:datashare/v20181101preview:DataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20191101:DataSetMapping"), pulumi.Alias(type_="azure-nextgen:datashare/v20191101:DataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20201001preview:DataSetMapping"), pulumi.Alias(type_="azure-nextgen:datashare/v20201001preview:DataSetMapping")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DataSetMapping, __self__).__init__(
            'azure-native:datashare/v20200901:DataSetMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataSetMapping':
        """
        Get an existing DataSetMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataSetMappingArgs.__new__(DataSetMappingArgs)

        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return DataSetMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of data set mapping.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")

