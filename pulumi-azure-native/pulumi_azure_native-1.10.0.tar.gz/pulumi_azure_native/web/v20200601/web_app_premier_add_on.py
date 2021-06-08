# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['WebAppPremierAddOnArgs', 'WebAppPremierAddOn']

@pulumi.input_type
class WebAppPremierAddOnArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 marketplace_offer: Optional[pulumi.Input[str]] = None,
                 marketplace_publisher: Optional[pulumi.Input[str]] = None,
                 premier_add_on_name: Optional[pulumi.Input[str]] = None,
                 product: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vendor: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebAppPremierAddOn resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] location: Resource Location.
        :param pulumi.Input[str] marketplace_offer: Premier add on Marketplace offer.
        :param pulumi.Input[str] marketplace_publisher: Premier add on Marketplace publisher.
        :param pulumi.Input[str] premier_add_on_name: Add-on name.
        :param pulumi.Input[str] product: Premier add on Product.
        :param pulumi.Input[str] sku: Premier add on SKU.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] vendor: Premier add on Vendor.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if marketplace_offer is not None:
            pulumi.set(__self__, "marketplace_offer", marketplace_offer)
        if marketplace_publisher is not None:
            pulumi.set(__self__, "marketplace_publisher", marketplace_publisher)
        if premier_add_on_name is not None:
            pulumi.set(__self__, "premier_add_on_name", premier_add_on_name)
        if product is not None:
            pulumi.set(__self__, "product", product)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vendor is not None:
            pulumi.set(__self__, "vendor", vendor)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the app.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="marketplaceOffer")
    def marketplace_offer(self) -> Optional[pulumi.Input[str]]:
        """
        Premier add on Marketplace offer.
        """
        return pulumi.get(self, "marketplace_offer")

    @marketplace_offer.setter
    def marketplace_offer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "marketplace_offer", value)

    @property
    @pulumi.getter(name="marketplacePublisher")
    def marketplace_publisher(self) -> Optional[pulumi.Input[str]]:
        """
        Premier add on Marketplace publisher.
        """
        return pulumi.get(self, "marketplace_publisher")

    @marketplace_publisher.setter
    def marketplace_publisher(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "marketplace_publisher", value)

    @property
    @pulumi.getter(name="premierAddOnName")
    def premier_add_on_name(self) -> Optional[pulumi.Input[str]]:
        """
        Add-on name.
        """
        return pulumi.get(self, "premier_add_on_name")

    @premier_add_on_name.setter
    def premier_add_on_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "premier_add_on_name", value)

    @property
    @pulumi.getter
    def product(self) -> Optional[pulumi.Input[str]]:
        """
        Premier add on Product.
        """
        return pulumi.get(self, "product")

    @product.setter
    def product(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[str]]:
        """
        Premier add on SKU.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku", value)

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
    @pulumi.getter
    def vendor(self) -> Optional[pulumi.Input[str]]:
        """
        Premier add on Vendor.
        """
        return pulumi.get(self, "vendor")

    @vendor.setter
    def vendor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vendor", value)


class WebAppPremierAddOn(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 marketplace_offer: Optional[pulumi.Input[str]] = None,
                 marketplace_publisher: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 premier_add_on_name: Optional[pulumi.Input[str]] = None,
                 product: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vendor: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Premier add-on.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] location: Resource Location.
        :param pulumi.Input[str] marketplace_offer: Premier add on Marketplace offer.
        :param pulumi.Input[str] marketplace_publisher: Premier add on Marketplace publisher.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] premier_add_on_name: Add-on name.
        :param pulumi.Input[str] product: Premier add on Product.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] sku: Premier add on SKU.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] vendor: Premier add on Vendor.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAppPremierAddOnArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Premier add-on.

        :param str resource_name: The name of the resource.
        :param WebAppPremierAddOnArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAppPremierAddOnArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 marketplace_offer: Optional[pulumi.Input[str]] = None,
                 marketplace_publisher: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 premier_add_on_name: Optional[pulumi.Input[str]] = None,
                 product: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vendor: Optional[pulumi.Input[str]] = None,
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
            __props__ = WebAppPremierAddOnArgs.__new__(WebAppPremierAddOnArgs)

            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["marketplace_offer"] = marketplace_offer
            __props__.__dict__["marketplace_publisher"] = marketplace_publisher
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["premier_add_on_name"] = premier_add_on_name
            __props__.__dict__["product"] = product
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vendor"] = vendor
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:web/v20200601:WebAppPremierAddOn"), pulumi.Alias(type_="azure-native:web:WebAppPremierAddOn"), pulumi.Alias(type_="azure-nextgen:web:WebAppPremierAddOn"), pulumi.Alias(type_="azure-native:web/v20150801:WebAppPremierAddOn"), pulumi.Alias(type_="azure-nextgen:web/v20150801:WebAppPremierAddOn"), pulumi.Alias(type_="azure-native:web/v20160801:WebAppPremierAddOn"), pulumi.Alias(type_="azure-nextgen:web/v20160801:WebAppPremierAddOn"), pulumi.Alias(type_="azure-native:web/v20180201:WebAppPremierAddOn"), pulumi.Alias(type_="azure-nextgen:web/v20180201:WebAppPremierAddOn"), pulumi.Alias(type_="azure-native:web/v20181101:WebAppPremierAddOn"), pulumi.Alias(type_="azure-nextgen:web/v20181101:WebAppPremierAddOn"), pulumi.Alias(type_="azure-native:web/v20190801:WebAppPremierAddOn"), pulumi.Alias(type_="azure-nextgen:web/v20190801:WebAppPremierAddOn"), pulumi.Alias(type_="azure-native:web/v20200901:WebAppPremierAddOn"), pulumi.Alias(type_="azure-nextgen:web/v20200901:WebAppPremierAddOn"), pulumi.Alias(type_="azure-native:web/v20201001:WebAppPremierAddOn"), pulumi.Alias(type_="azure-nextgen:web/v20201001:WebAppPremierAddOn"), pulumi.Alias(type_="azure-native:web/v20201201:WebAppPremierAddOn"), pulumi.Alias(type_="azure-nextgen:web/v20201201:WebAppPremierAddOn"), pulumi.Alias(type_="azure-native:web/v20210101:WebAppPremierAddOn"), pulumi.Alias(type_="azure-nextgen:web/v20210101:WebAppPremierAddOn")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WebAppPremierAddOn, __self__).__init__(
            'azure-native:web/v20200601:WebAppPremierAddOn',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebAppPremierAddOn':
        """
        Get an existing WebAppPremierAddOn resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebAppPremierAddOnArgs.__new__(WebAppPremierAddOnArgs)

        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["marketplace_offer"] = None
        __props__.__dict__["marketplace_publisher"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["product"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vendor"] = None
        return WebAppPremierAddOn(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource Location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="marketplaceOffer")
    def marketplace_offer(self) -> pulumi.Output[Optional[str]]:
        """
        Premier add on Marketplace offer.
        """
        return pulumi.get(self, "marketplace_offer")

    @property
    @pulumi.getter(name="marketplacePublisher")
    def marketplace_publisher(self) -> pulumi.Output[Optional[str]]:
        """
        Premier add on Marketplace publisher.
        """
        return pulumi.get(self, "marketplace_publisher")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def product(self) -> pulumi.Output[Optional[str]]:
        """
        Premier add on Product.
        """
        return pulumi.get(self, "product")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[str]]:
        """
        Premier add on SKU.
        """
        return pulumi.get(self, "sku")

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
    @pulumi.getter
    def vendor(self) -> pulumi.Output[Optional[str]]:
        """
        Premier add on Vendor.
        """
        return pulumi.get(self, "vendor")

