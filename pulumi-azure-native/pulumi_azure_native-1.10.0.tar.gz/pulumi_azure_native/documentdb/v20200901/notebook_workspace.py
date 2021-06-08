# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['NotebookWorkspaceArgs', 'NotebookWorkspace']

@pulumi.input_type
class NotebookWorkspaceArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 notebook_workspace_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NotebookWorkspace resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] notebook_workspace_name: The name of the notebook workspace resource.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if notebook_workspace_name is not None:
            pulumi.set(__self__, "notebook_workspace_name", notebook_workspace_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Cosmos DB database account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

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
    @pulumi.getter(name="notebookWorkspaceName")
    def notebook_workspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the notebook workspace resource.
        """
        return pulumi.get(self, "notebook_workspace_name")

    @notebook_workspace_name.setter
    def notebook_workspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notebook_workspace_name", value)


class NotebookWorkspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 notebook_workspace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A notebook workspace resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] notebook_workspace_name: The name of the notebook workspace resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotebookWorkspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A notebook workspace resource

        :param str resource_name: The name of the resource.
        :param NotebookWorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotebookWorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 notebook_workspace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = NotebookWorkspaceArgs.__new__(NotebookWorkspaceArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["notebook_workspace_name"] = notebook_workspace_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["notebook_server_endpoint"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:documentdb/v20200901:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20190801:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20190801:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20191212:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20191212:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20200301:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20200301:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20200401:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20200401:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20200601preview:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20200601preview:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20210115:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210115:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20210301preview:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210301preview:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20210315:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210315:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20210401preview:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210401preview:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20210415:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210415:NotebookWorkspace"), pulumi.Alias(type_="azure-native:documentdb/v20210515:NotebookWorkspace"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210515:NotebookWorkspace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NotebookWorkspace, __self__).__init__(
            'azure-native:documentdb/v20200901:NotebookWorkspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NotebookWorkspace':
        """
        Get an existing NotebookWorkspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NotebookWorkspaceArgs.__new__(NotebookWorkspaceArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["notebook_server_endpoint"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["type"] = None
        return NotebookWorkspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the database account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notebookServerEndpoint")
    def notebook_server_endpoint(self) -> pulumi.Output[str]:
        """
        Specifies the endpoint of Notebook server.
        """
        return pulumi.get(self, "notebook_server_endpoint")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the notebook workspace. Possible values are: Creating, Online, Deleting, Failed, Updating.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")

