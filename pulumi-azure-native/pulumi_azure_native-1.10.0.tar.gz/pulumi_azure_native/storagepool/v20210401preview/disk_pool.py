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

__all__ = ['DiskPoolArgs', 'DiskPool']

@pulumi.input_type
class DiskPoolArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['SkuArgs'],
                 subnet_id: pulumi.Input[str],
                 additional_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 disk_pool_name: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DiskPool resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['SkuArgs'] sku: Determines the SKU of the Disk Pool
        :param pulumi.Input[str] subnet_id: Azure Resource ID of a Subnet for the Disk Pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_capabilities: List of additional capabilities for a Disk Pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: Logical zone for Disk Pool resource; example: ["1"].
        :param pulumi.Input[str] disk_pool_name: The name of the Disk Pool.
        :param pulumi.Input[Sequence[pulumi.Input['DiskArgs']]] disks: List of Azure Managed Disks to attach to a Disk Pool.
        :param pulumi.Input[str] location: The geo-location where the resource lives.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        pulumi.set(__self__, "subnet_id", subnet_id)
        if additional_capabilities is not None:
            pulumi.set(__self__, "additional_capabilities", additional_capabilities)
        if availability_zones is not None:
            pulumi.set(__self__, "availability_zones", availability_zones)
        if disk_pool_name is not None:
            pulumi.set(__self__, "disk_pool_name", disk_pool_name)
        if disks is not None:
            pulumi.set(__self__, "disks", disks)
        if location is not None:
            pulumi.set(__self__, "location", location)
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
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        Determines the SKU of the Disk Pool
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        Azure Resource ID of a Subnet for the Disk Pool.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of additional capabilities for a Disk Pool.
        """
        return pulumi.get(self, "additional_capabilities")

    @additional_capabilities.setter
    def additional_capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "additional_capabilities", value)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Logical zone for Disk Pool resource; example: ["1"].
        """
        return pulumi.get(self, "availability_zones")

    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "availability_zones", value)

    @property
    @pulumi.getter(name="diskPoolName")
    def disk_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Disk Pool.
        """
        return pulumi.get(self, "disk_pool_name")

    @disk_pool_name.setter
    def disk_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_pool_name", value)

    @property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]]:
        """
        List of Azure Managed Disks to attach to a Disk Pool.
        """
        return pulumi.get(self, "disks")

    @disks.setter
    def disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]]):
        pulumi.set(self, "disks", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class DiskPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 disk_pool_name: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiskArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Response for Disk Pool request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_capabilities: List of additional capabilities for a Disk Pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zones: Logical zone for Disk Pool resource; example: ["1"].
        :param pulumi.Input[str] disk_pool_name: The name of the Disk Pool.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiskArgs']]]] disks: List of Azure Managed Disks to attach to a Disk Pool.
        :param pulumi.Input[str] location: The geo-location where the resource lives.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: Determines the SKU of the Disk Pool
        :param pulumi.Input[str] subnet_id: Azure Resource ID of a Subnet for the Disk Pool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DiskPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Response for Disk Pool request.

        :param str resource_name: The name of the resource.
        :param DiskPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DiskPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 disk_pool_name: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiskArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = DiskPoolArgs.__new__(DiskPoolArgs)

            __props__.__dict__["additional_capabilities"] = additional_capabilities
            __props__.__dict__["availability_zones"] = availability_zones
            __props__.__dict__["disk_pool_name"] = disk_pool_name
            __props__.__dict__["disks"] = disks
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["tier"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:storagepool/v20210401preview:DiskPool"), pulumi.Alias(type_="azure-native:storagepool:DiskPool"), pulumi.Alias(type_="azure-nextgen:storagepool:DiskPool"), pulumi.Alias(type_="azure-native:storagepool/v20200315preview:DiskPool"), pulumi.Alias(type_="azure-nextgen:storagepool/v20200315preview:DiskPool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DiskPool, __self__).__init__(
            'azure-native:storagepool/v20210401preview:DiskPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DiskPool':
        """
        Get an existing DiskPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DiskPoolArgs.__new__(DiskPoolArgs)

        __props__.__dict__["additional_capabilities"] = None
        __props__.__dict__["availability_zones"] = None
        __props__.__dict__["disks"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tier"] = None
        __props__.__dict__["type"] = None
        return DiskPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of additional capabilities for Disk Pool.
        """
        return pulumi.get(self, "additional_capabilities")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Sequence[str]]:
        """
        Logical zone for Disk Pool resource; example: ["1"].
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter
    def disks(self) -> pulumi.Output[Optional[Sequence['outputs.DiskResponse']]]:
        """
        List of Azure Managed Disks to attach to a Disk Pool.
        """
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Operational status of the Disk Pool.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        Azure Resource ID of a Subnet for the Disk Pool.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemMetadataResponse']:
        """
        Resource metadata required by ARM RPC
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
    def tier(self) -> pulumi.Output[Optional[str]]:
        """
        Sku tier
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

