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

__all__ = ['AppArgs', 'App']

@pulumi.input_type
class AppArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['AppSkuInfoArgs'],
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a App resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the IoT Central application.
        :param pulumi.Input['AppSkuInfoArgs'] sku: A valid instance SKU.
        :param pulumi.Input[str] display_name: The display name of the application.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] resource_name: The ARM resource name of the IoT Central application.
        :param pulumi.Input[str] subdomain: The subdomain of the application.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        :param pulumi.Input[str] template: The ID of the application template, which is a blueprint that defines the characteristics and behaviors of an application. Optional; if not specified, defaults to a blank blueprint and allows the application to be defined from scratch.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if subdomain is not None:
            pulumi.set(__self__, "subdomain", subdomain)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if template is not None:
            pulumi.set(__self__, "template", template)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the IoT Central application.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['AppSkuInfoArgs']:
        """
        A valid instance SKU.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['AppSkuInfoArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the application.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The ARM resource name of the IoT Central application.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def subdomain(self) -> Optional[pulumi.Input[str]]:
        """
        The subdomain of the application.
        """
        return pulumi.get(self, "subdomain")

    @subdomain.setter
    def subdomain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdomain", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the application template, which is a blueprint that defines the characteristics and behaviors of an application. Optional; if not specified, defaults to a blank blueprint and allows the application to be defined from scratch.
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template", value)


class App(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['AppSkuInfoArgs']]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The IoT Central application.
        API Version: 2018-09-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: The display name of the application.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the IoT Central application.
        :param pulumi.Input[str] resource_name_: The ARM resource name of the IoT Central application.
        :param pulumi.Input[pulumi.InputType['AppSkuInfoArgs']] sku: A valid instance SKU.
        :param pulumi.Input[str] subdomain: The subdomain of the application.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        :param pulumi.Input[str] template: The ID of the application template, which is a blueprint that defines the characteristics and behaviors of an application. Optional; if not specified, defaults to a blank blueprint and allows the application to be defined from scratch.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The IoT Central application.
        API Version: 2018-09-01.

        :param str resource_name: The name of the resource.
        :param AppArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['AppSkuInfoArgs']]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template: Optional[pulumi.Input[str]] = None,
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
            __props__ = AppArgs.__new__(AppArgs)

            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["subdomain"] = subdomain
            __props__.__dict__["tags"] = tags
            __props__.__dict__["template"] = template
            __props__.__dict__["application_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:iotcentral:App"), pulumi.Alias(type_="azure-native:iotcentral/v20170701privatepreview:App"), pulumi.Alias(type_="azure-nextgen:iotcentral/v20170701privatepreview:App"), pulumi.Alias(type_="azure-native:iotcentral/v20180901:App"), pulumi.Alias(type_="azure-nextgen:iotcentral/v20180901:App")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(App, __self__).__init__(
            'azure-native:iotcentral:App',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'App':
        """
        Get an existing App resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AppArgs.__new__(AppArgs)

        __props__.__dict__["application_id"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["subdomain"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["template"] = None
        __props__.__dict__["type"] = None
        return App(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The ID of the application.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the application.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The ARM resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.AppSkuInfoResponse']:
        """
        A valid instance SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def subdomain(self) -> pulumi.Output[Optional[str]]:
        """
        The subdomain of the application.
        """
        return pulumi.get(self, "subdomain")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def template(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the application template, which is a blueprint that defines the characteristics and behaviors of an application. Optional; if not specified, defaults to a blank blueprint and allows the application to be defined from scratch.
        """
        return pulumi.get(self, "template")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

