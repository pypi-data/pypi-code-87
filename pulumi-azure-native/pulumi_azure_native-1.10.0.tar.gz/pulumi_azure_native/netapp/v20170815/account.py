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

__all__ = ['AccountArgs', 'Account']

@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 account_name: Optional[pulumi.Input[str]] = None,
                 active_directories: Optional[pulumi.Input[Sequence[pulumi.Input['ActiveDirectoryArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a Account resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[Sequence[pulumi.Input['ActiveDirectoryArgs']]] active_directories: Active Directories
        :param pulumi.Input[str] location: Resource location
        :param Any tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if active_directories is not None:
            pulumi.set(__self__, "active_directories", active_directories)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the NetApp account
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="activeDirectories")
    def active_directories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ActiveDirectoryArgs']]]]:
        """
        Active Directories
        """
        return pulumi.get(self, "active_directories")

    @active_directories.setter
    def active_directories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ActiveDirectoryArgs']]]]):
        pulumi.set(self, "active_directories", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 active_directories: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActiveDirectoryArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        """
        NetApp account resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActiveDirectoryArgs']]]] active_directories: Active Directories
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param Any tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NetApp account resource

        :param str resource_name: The name of the resource.
        :param AccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 active_directories: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActiveDirectoryArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
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
            __props__ = AccountArgs.__new__(AccountArgs)

            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["active_directories"] = active_directories
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:netapp/v20170815:Account"), pulumi.Alias(type_="azure-native:netapp:Account"), pulumi.Alias(type_="azure-nextgen:netapp:Account"), pulumi.Alias(type_="azure-native:netapp/v20190501:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20190501:Account"), pulumi.Alias(type_="azure-native:netapp/v20190601:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20190601:Account"), pulumi.Alias(type_="azure-native:netapp/v20190701:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20190701:Account"), pulumi.Alias(type_="azure-native:netapp/v20190801:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20190801:Account"), pulumi.Alias(type_="azure-native:netapp/v20191001:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20191001:Account"), pulumi.Alias(type_="azure-native:netapp/v20191101:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20191101:Account"), pulumi.Alias(type_="azure-native:netapp/v20200201:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20200201:Account"), pulumi.Alias(type_="azure-native:netapp/v20200301:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20200301:Account"), pulumi.Alias(type_="azure-native:netapp/v20200501:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20200501:Account"), pulumi.Alias(type_="azure-native:netapp/v20200601:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20200601:Account"), pulumi.Alias(type_="azure-native:netapp/v20200701:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20200701:Account"), pulumi.Alias(type_="azure-native:netapp/v20200801:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20200801:Account"), pulumi.Alias(type_="azure-native:netapp/v20200901:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20200901:Account"), pulumi.Alias(type_="azure-native:netapp/v20201101:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20201101:Account"), pulumi.Alias(type_="azure-native:netapp/v20201201:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20201201:Account"), pulumi.Alias(type_="azure-native:netapp/v20210201:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20210201:Account"), pulumi.Alias(type_="azure-native:netapp/v20210401:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20210401:Account"), pulumi.Alias(type_="azure-native:netapp/v20210401preview:Account"), pulumi.Alias(type_="azure-nextgen:netapp/v20210401preview:Account")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Account, __self__).__init__(
            'azure-native:netapp/v20170815:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccountArgs.__new__(AccountArgs)

        __props__.__dict__["active_directories"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activeDirectories")
    def active_directories(self) -> pulumi.Output[Optional[Sequence['outputs.ActiveDirectoryResponse']]]:
        """
        Active Directories
        """
        return pulumi.get(self, "active_directories")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

