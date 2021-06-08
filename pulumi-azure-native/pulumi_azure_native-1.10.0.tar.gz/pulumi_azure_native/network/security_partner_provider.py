# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['SecurityPartnerProviderArgs', 'SecurityPartnerProvider']

@pulumi.input_type
class SecurityPartnerProviderArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 security_partner_provider_name: Optional[pulumi.Input[str]] = None,
                 security_provider_name: Optional[pulumi.Input[Union[str, 'SecurityProviderName']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input['SubResourceArgs']] = None):
        """
        The set of arguments for constructing a SecurityPartnerProvider resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] security_partner_provider_name: The name of the Security Partner Provider.
        :param pulumi.Input[Union[str, 'SecurityProviderName']] security_provider_name: The security provider name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input['SubResourceArgs'] virtual_hub: The virtualHub to which the Security Partner Provider belongs.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if security_partner_provider_name is not None:
            pulumi.set(__self__, "security_partner_provider_name", security_partner_provider_name)
        if security_provider_name is not None:
            pulumi.set(__self__, "security_provider_name", security_provider_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_hub is not None:
            pulumi.set(__self__, "virtual_hub", virtual_hub)

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
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="securityPartnerProviderName")
    def security_partner_provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Security Partner Provider.
        """
        return pulumi.get(self, "security_partner_provider_name")

    @security_partner_provider_name.setter
    def security_partner_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_partner_provider_name", value)

    @property
    @pulumi.getter(name="securityProviderName")
    def security_provider_name(self) -> Optional[pulumi.Input[Union[str, 'SecurityProviderName']]]:
        """
        The security provider name.
        """
        return pulumi.get(self, "security_provider_name")

    @security_provider_name.setter
    def security_provider_name(self, value: Optional[pulumi.Input[Union[str, 'SecurityProviderName']]]):
        pulumi.set(self, "security_provider_name", value)

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

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The virtualHub to which the Security Partner Provider belongs.
        """
        return pulumi.get(self, "virtual_hub")

    @virtual_hub.setter
    def virtual_hub(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "virtual_hub", value)


class SecurityPartnerProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_partner_provider_name: Optional[pulumi.Input[str]] = None,
                 security_provider_name: Optional[pulumi.Input[Union[str, 'SecurityProviderName']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 __props__=None):
        """
        Security Partner Provider resource.
        API Version: 2020-11-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] security_partner_provider_name: The name of the Security Partner Provider.
        :param pulumi.Input[Union[str, 'SecurityProviderName']] security_provider_name: The security provider name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] virtual_hub: The virtualHub to which the Security Partner Provider belongs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityPartnerProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Security Partner Provider resource.
        API Version: 2020-11-01.

        :param str resource_name: The name of the resource.
        :param SecurityPartnerProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityPartnerProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_partner_provider_name: Optional[pulumi.Input[str]] = None,
                 security_provider_name: Optional[pulumi.Input[Union[str, 'SecurityProviderName']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
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
            __props__ = SecurityPartnerProviderArgs.__new__(SecurityPartnerProviderArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["security_partner_provider_name"] = security_partner_provider_name
            __props__.__dict__["security_provider_name"] = security_provider_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_hub"] = virtual_hub
            __props__.__dict__["connection_status"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network:SecurityPartnerProvider"), pulumi.Alias(type_="azure-native:network/v20200301:SecurityPartnerProvider"), pulumi.Alias(type_="azure-nextgen:network/v20200301:SecurityPartnerProvider"), pulumi.Alias(type_="azure-native:network/v20200401:SecurityPartnerProvider"), pulumi.Alias(type_="azure-nextgen:network/v20200401:SecurityPartnerProvider"), pulumi.Alias(type_="azure-native:network/v20200501:SecurityPartnerProvider"), pulumi.Alias(type_="azure-nextgen:network/v20200501:SecurityPartnerProvider"), pulumi.Alias(type_="azure-native:network/v20200601:SecurityPartnerProvider"), pulumi.Alias(type_="azure-nextgen:network/v20200601:SecurityPartnerProvider"), pulumi.Alias(type_="azure-native:network/v20200701:SecurityPartnerProvider"), pulumi.Alias(type_="azure-nextgen:network/v20200701:SecurityPartnerProvider"), pulumi.Alias(type_="azure-native:network/v20200801:SecurityPartnerProvider"), pulumi.Alias(type_="azure-nextgen:network/v20200801:SecurityPartnerProvider"), pulumi.Alias(type_="azure-native:network/v20201101:SecurityPartnerProvider"), pulumi.Alias(type_="azure-nextgen:network/v20201101:SecurityPartnerProvider"), pulumi.Alias(type_="azure-native:network/v20210201:SecurityPartnerProvider"), pulumi.Alias(type_="azure-nextgen:network/v20210201:SecurityPartnerProvider")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SecurityPartnerProvider, __self__).__init__(
            'azure-native:network:SecurityPartnerProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityPartnerProvider':
        """
        Get an existing SecurityPartnerProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityPartnerProviderArgs.__new__(SecurityPartnerProviderArgs)

        __props__.__dict__["connection_status"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["security_provider_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_hub"] = None
        return SecurityPartnerProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> pulumi.Output[str]:
        """
        The connection status with the Security Partner Provider.
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the Security Partner Provider resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="securityProviderName")
    def security_provider_name(self) -> pulumi.Output[Optional[str]]:
        """
        The security provider name.
        """
        return pulumi.get(self, "security_provider_name")

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
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The virtualHub to which the Security Partner Provider belongs.
        """
        return pulumi.get(self, "virtual_hub")

