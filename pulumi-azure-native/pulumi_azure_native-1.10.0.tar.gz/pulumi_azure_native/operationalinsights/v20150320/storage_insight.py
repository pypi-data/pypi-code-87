# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['StorageInsightArgs', 'StorageInsight']

@pulumi.input_type
class StorageInsightArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 storage_account: pulumi.Input['StorageAccountArgs'],
                 workspace_name: pulumi.Input[str],
                 containers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 storage_insight_name: Optional[pulumi.Input[str]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StorageInsight resource.
        :param pulumi.Input[str] resource_group_name: The Resource Group name.
        :param pulumi.Input['StorageAccountArgs'] storage_account: The storage account connection details
        :param pulumi.Input[str] workspace_name: The Log Analytics Workspace name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] containers: The names of the blob containers that the workspace should read
        :param pulumi.Input[str] e_tag: The ETag of the storage insight.
        :param pulumi.Input[str] storage_insight_name: Name of the storageInsightsConfigs resource
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tables: The names of the Azure tables that the workspace should read
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_account", storage_account)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if containers is not None:
            pulumi.set(__self__, "containers", containers)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if storage_insight_name is not None:
            pulumi.set(__self__, "storage_insight_name", storage_insight_name)
        if tables is not None:
            pulumi.set(__self__, "tables", tables)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The Resource Group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Input['StorageAccountArgs']:
        """
        The storage account connection details
        """
        return pulumi.get(self, "storage_account")

    @storage_account.setter
    def storage_account(self, value: pulumi.Input['StorageAccountArgs']):
        pulumi.set(self, "storage_account", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The Log Analytics Workspace name.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter
    def containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The names of the blob containers that the workspace should read
        """
        return pulumi.get(self, "containers")

    @containers.setter
    def containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "containers", value)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        The ETag of the storage insight.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter(name="storageInsightName")
    def storage_insight_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the storageInsightsConfigs resource
        """
        return pulumi.get(self, "storage_insight_name")

    @storage_insight_name.setter
    def storage_insight_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_insight_name", value)

    @property
    @pulumi.getter
    def tables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The names of the Azure tables that the workspace should read
        """
        return pulumi.get(self, "tables")

    @tables.setter
    def tables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tables", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class StorageInsight(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 containers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account: Optional[pulumi.Input[pulumi.InputType['StorageAccountArgs']]] = None,
                 storage_insight_name: Optional[pulumi.Input[str]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The top level storage insight resource container.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] containers: The names of the blob containers that the workspace should read
        :param pulumi.Input[str] e_tag: The ETag of the storage insight.
        :param pulumi.Input[str] resource_group_name: The Resource Group name.
        :param pulumi.Input[pulumi.InputType['StorageAccountArgs']] storage_account: The storage account connection details
        :param pulumi.Input[str] storage_insight_name: Name of the storageInsightsConfigs resource
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tables: The names of the Azure tables that the workspace should read
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] workspace_name: The Log Analytics Workspace name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageInsightArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The top level storage insight resource container.

        :param str resource_name: The name of the resource.
        :param StorageInsightArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageInsightArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 containers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account: Optional[pulumi.Input[pulumi.InputType['StorageAccountArgs']]] = None,
                 storage_insight_name: Optional[pulumi.Input[str]] = None,
                 tables: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = StorageInsightArgs.__new__(StorageInsightArgs)

            __props__.__dict__["containers"] = containers
            __props__.__dict__["e_tag"] = e_tag
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_account is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account'")
            __props__.__dict__["storage_account"] = storage_account
            __props__.__dict__["storage_insight_name"] = storage_insight_name
            __props__.__dict__["tables"] = tables
            __props__.__dict__["tags"] = tags
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:operationalinsights/v20150320:StorageInsight"), pulumi.Alias(type_="azure-native:operationalinsights:StorageInsight"), pulumi.Alias(type_="azure-nextgen:operationalinsights:StorageInsight"), pulumi.Alias(type_="azure-native:operationalinsights/v20200301preview:StorageInsight"), pulumi.Alias(type_="azure-nextgen:operationalinsights/v20200301preview:StorageInsight"), pulumi.Alias(type_="azure-native:operationalinsights/v20200801:StorageInsight"), pulumi.Alias(type_="azure-nextgen:operationalinsights/v20200801:StorageInsight")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StorageInsight, __self__).__init__(
            'azure-native:operationalinsights/v20150320:StorageInsight',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StorageInsight':
        """
        Get an existing StorageInsight resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StorageInsightArgs.__new__(StorageInsightArgs)

        __props__.__dict__["containers"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["storage_account"] = None
        __props__.__dict__["tables"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return StorageInsight(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def containers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The names of the blob containers that the workspace should read
        """
        return pulumi.get(self, "containers")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        The ETag of the storage insight.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.StorageInsightStatusResponse']:
        """
        The status of the storage insight
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Output['outputs.StorageAccountResponse']:
        """
        The storage account connection details
        """
        return pulumi.get(self, "storage_account")

    @property
    @pulumi.getter
    def tables(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The names of the Azure tables that the workspace should read
        """
        return pulumi.get(self, "tables")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

