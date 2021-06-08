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

__all__ = ['VirtualApplianceSiteArgs', 'VirtualApplianceSite']

@pulumi.input_type
class VirtualApplianceSiteArgs:
    def __init__(__self__, *,
                 network_virtual_appliance_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 o365_policy: Optional[pulumi.Input['Office365PolicyPropertiesArgs']] = None,
                 site_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualApplianceSite resource.
        :param pulumi.Input[str] network_virtual_appliance_name: The name of the Network Virtual Appliance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] address_prefix: Address Prefix.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Name of the virtual appliance site.
        :param pulumi.Input['Office365PolicyPropertiesArgs'] o365_policy: Office 365 Policy.
        :param pulumi.Input[str] site_name: The name of the site.
        """
        pulumi.set(__self__, "network_virtual_appliance_name", network_virtual_appliance_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if address_prefix is not None:
            pulumi.set(__self__, "address_prefix", address_prefix)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if o365_policy is not None:
            pulumi.set(__self__, "o365_policy", o365_policy)
        if site_name is not None:
            pulumi.set(__self__, "site_name", site_name)

    @property
    @pulumi.getter(name="networkVirtualApplianceName")
    def network_virtual_appliance_name(self) -> pulumi.Input[str]:
        """
        The name of the Network Virtual Appliance.
        """
        return pulumi.get(self, "network_virtual_appliance_name")

    @network_virtual_appliance_name.setter
    def network_virtual_appliance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_virtual_appliance_name", value)

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
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Address Prefix.
        """
        return pulumi.get(self, "address_prefix")

    @address_prefix.setter
    def address_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_prefix", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the virtual appliance site.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="o365Policy")
    def o365_policy(self) -> Optional[pulumi.Input['Office365PolicyPropertiesArgs']]:
        """
        Office 365 Policy.
        """
        return pulumi.get(self, "o365_policy")

    @o365_policy.setter
    def o365_policy(self, value: Optional[pulumi.Input['Office365PolicyPropertiesArgs']]):
        pulumi.set(self, "o365_policy", value)

    @property
    @pulumi.getter(name="siteName")
    def site_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the site.
        """
        return pulumi.get(self, "site_name")

    @site_name.setter
    def site_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_name", value)


class VirtualApplianceSite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_virtual_appliance_name: Optional[pulumi.Input[str]] = None,
                 o365_policy: Optional[pulumi.Input[pulumi.InputType['Office365PolicyPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Virtual Appliance Site resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_prefix: Address Prefix.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Name of the virtual appliance site.
        :param pulumi.Input[str] network_virtual_appliance_name: The name of the Network Virtual Appliance.
        :param pulumi.Input[pulumi.InputType['Office365PolicyPropertiesArgs']] o365_policy: Office 365 Policy.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] site_name: The name of the site.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualApplianceSiteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Virtual Appliance Site resource.

        :param str resource_name: The name of the resource.
        :param VirtualApplianceSiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualApplianceSiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_virtual_appliance_name: Optional[pulumi.Input[str]] = None,
                 o365_policy: Optional[pulumi.Input[pulumi.InputType['Office365PolicyPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = VirtualApplianceSiteArgs.__new__(VirtualApplianceSiteArgs)

            __props__.__dict__["address_prefix"] = address_prefix
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            if network_virtual_appliance_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_virtual_appliance_name'")
            __props__.__dict__["network_virtual_appliance_name"] = network_virtual_appliance_name
            __props__.__dict__["o365_policy"] = o365_policy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["site_name"] = site_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20201101:VirtualApplianceSite"), pulumi.Alias(type_="azure-native:network:VirtualApplianceSite"), pulumi.Alias(type_="azure-nextgen:network:VirtualApplianceSite"), pulumi.Alias(type_="azure-native:network/v20200501:VirtualApplianceSite"), pulumi.Alias(type_="azure-nextgen:network/v20200501:VirtualApplianceSite"), pulumi.Alias(type_="azure-native:network/v20200601:VirtualApplianceSite"), pulumi.Alias(type_="azure-nextgen:network/v20200601:VirtualApplianceSite"), pulumi.Alias(type_="azure-native:network/v20200701:VirtualApplianceSite"), pulumi.Alias(type_="azure-nextgen:network/v20200701:VirtualApplianceSite"), pulumi.Alias(type_="azure-native:network/v20200801:VirtualApplianceSite"), pulumi.Alias(type_="azure-nextgen:network/v20200801:VirtualApplianceSite"), pulumi.Alias(type_="azure-native:network/v20210201:VirtualApplianceSite"), pulumi.Alias(type_="azure-nextgen:network/v20210201:VirtualApplianceSite")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualApplianceSite, __self__).__init__(
            'azure-native:network/v20201101:VirtualApplianceSite',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualApplianceSite':
        """
        Get an existing VirtualApplianceSite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualApplianceSiteArgs.__new__(VirtualApplianceSiteArgs)

        __props__.__dict__["address_prefix"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["o365_policy"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return VirtualApplianceSite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        Address Prefix.
        """
        return pulumi.get(self, "address_prefix")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the virtual appliance site.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="o365Policy")
    def o365_policy(self) -> pulumi.Output[Optional['outputs.Office365PolicyPropertiesResponse']]:
        """
        Office 365 Policy.
        """
        return pulumi.get(self, "o365_policy")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Site type.
        """
        return pulumi.get(self, "type")

