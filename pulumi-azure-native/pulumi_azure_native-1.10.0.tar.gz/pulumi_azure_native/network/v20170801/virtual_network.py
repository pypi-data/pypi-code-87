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

__all__ = ['VirtualNetworkArgs', 'VirtualNetwork']

@pulumi.input_type
class VirtualNetworkArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 address_space: Optional[pulumi.Input['AddressSpaceArgs']] = None,
                 dhcp_options: Optional[pulumi.Input['DhcpOptionsArgs']] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_peerings: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkPeeringArgs']]]] = None):
        """
        The set of arguments for constructing a VirtualNetwork resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['AddressSpaceArgs'] address_space: The AddressSpace that contains an array of IP address ranges that can be used by subnets.
        :param pulumi.Input['DhcpOptionsArgs'] dhcp_options: The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network.
        :param pulumi.Input[str] etag: Gets a unique read-only string that changes whenever the resource is updated.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] provisioning_state: The provisioning state of the PublicIP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        :param pulumi.Input[str] resource_guid: The resourceGuid property of the Virtual Network resource.
        :param pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]] subnets: A list of subnets in a Virtual Network.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] virtual_network_name: The name of the virtual network.
        :param pulumi.Input[Sequence[pulumi.Input['VirtualNetworkPeeringArgs']]] virtual_network_peerings: A list of peerings in a Virtual Network.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if address_space is not None:
            pulumi.set(__self__, "address_space", address_space)
        if dhcp_options is not None:
            pulumi.set(__self__, "dhcp_options", dhcp_options)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_guid is not None:
            pulumi.set(__self__, "resource_guid", resource_guid)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_network_name is not None:
            pulumi.set(__self__, "virtual_network_name", virtual_network_name)
        if virtual_network_peerings is not None:
            pulumi.set(__self__, "virtual_network_peerings", virtual_network_peerings)

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
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> Optional[pulumi.Input['AddressSpaceArgs']]:
        """
        The AddressSpace that contains an array of IP address ranges that can be used by subnets.
        """
        return pulumi.get(self, "address_space")

    @address_space.setter
    def address_space(self, value: Optional[pulumi.Input['AddressSpaceArgs']]):
        pulumi.set(self, "address_space", value)

    @property
    @pulumi.getter(name="dhcpOptions")
    def dhcp_options(self) -> Optional[pulumi.Input['DhcpOptionsArgs']]:
        """
        The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network.
        """
        return pulumi.get(self, "dhcp_options")

    @dhcp_options.setter
    def dhcp_options(self, value: Optional[pulumi.Input['DhcpOptionsArgs']]):
        pulumi.set(self, "dhcp_options", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        Gets a unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning state of the PublicIP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> Optional[pulumi.Input[str]]:
        """
        The resourceGuid property of the Virtual Network resource.
        """
        return pulumi.get(self, "resource_guid")

    @resource_guid.setter
    def resource_guid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_guid", value)

    @property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]]]:
        """
        A list of subnets in a Virtual Network.
        """
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubnetArgs']]]]):
        pulumi.set(self, "subnets", value)

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
    @pulumi.getter(name="virtualNetworkName")
    def virtual_network_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the virtual network.
        """
        return pulumi.get(self, "virtual_network_name")

    @virtual_network_name.setter
    def virtual_network_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_network_name", value)

    @property
    @pulumi.getter(name="virtualNetworkPeerings")
    def virtual_network_peerings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkPeeringArgs']]]]:
        """
        A list of peerings in a Virtual Network.
        """
        return pulumi.get(self, "virtual_network_peerings")

    @virtual_network_peerings.setter
    def virtual_network_peerings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkPeeringArgs']]]]):
        pulumi.set(self, "virtual_network_peerings", value)


class VirtualNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_space: Optional[pulumi.Input[pulumi.InputType['AddressSpaceArgs']]] = None,
                 dhcp_options: Optional[pulumi.Input[pulumi.InputType['DhcpOptionsArgs']]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_peerings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualNetworkPeeringArgs']]]]] = None,
                 __props__=None):
        """
        Virtual Network resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AddressSpaceArgs']] address_space: The AddressSpace that contains an array of IP address ranges that can be used by subnets.
        :param pulumi.Input[pulumi.InputType['DhcpOptionsArgs']] dhcp_options: The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network.
        :param pulumi.Input[str] etag: Gets a unique read-only string that changes whenever the resource is updated.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] provisioning_state: The provisioning state of the PublicIP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_guid: The resourceGuid property of the Virtual Network resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetArgs']]]] subnets: A list of subnets in a Virtual Network.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] virtual_network_name: The name of the virtual network.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualNetworkPeeringArgs']]]] virtual_network_peerings: A list of peerings in a Virtual Network.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualNetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Virtual Network resource.

        :param str resource_name: The name of the resource.
        :param VirtualNetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualNetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_space: Optional[pulumi.Input[pulumi.InputType['AddressSpaceArgs']]] = None,
                 dhcp_options: Optional[pulumi.Input[pulumi.InputType['DhcpOptionsArgs']]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubnetArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_peerings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualNetworkPeeringArgs']]]]] = None,
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
            __props__ = VirtualNetworkArgs.__new__(VirtualNetworkArgs)

            __props__.__dict__["address_space"] = address_space
            __props__.__dict__["dhcp_options"] = dhcp_options
            __props__.__dict__["etag"] = etag
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_guid"] = resource_guid
            __props__.__dict__["subnets"] = subnets
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_network_name"] = virtual_network_name
            __props__.__dict__["virtual_network_peerings"] = virtual_network_peerings
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20170801:VirtualNetwork"), pulumi.Alias(type_="azure-native:network:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20150501preview:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20150501preview:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20150615:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20150615:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20160330:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20160330:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20160601:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20160601:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20160901:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20160901:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20161201:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20161201:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20170301:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20170301:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20170601:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20170601:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20170901:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20170901:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20171001:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20171001:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20171101:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20171101:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20180101:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20180101:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20180201:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20180201:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20180401:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20180401:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20180601:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20180601:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20180701:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20180701:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20180801:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20180801:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20181001:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20181001:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20181101:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20181101:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20181201:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20181201:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20190201:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20190201:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20190401:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20190401:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20190601:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20190601:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20190701:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20190701:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20190801:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20190801:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20190901:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20190901:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20191101:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20191101:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20191201:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20191201:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20200301:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20200301:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20200401:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20200401:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20200501:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20200501:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20200601:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20200601:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20200701:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20200701:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20200801:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20200801:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20201101:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20201101:VirtualNetwork"), pulumi.Alias(type_="azure-native:network/v20210201:VirtualNetwork"), pulumi.Alias(type_="azure-nextgen:network/v20210201:VirtualNetwork")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualNetwork, __self__).__init__(
            'azure-native:network/v20170801:VirtualNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualNetwork':
        """
        Get an existing VirtualNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualNetworkArgs.__new__(VirtualNetworkArgs)

        __props__.__dict__["address_space"] = None
        __props__.__dict__["dhcp_options"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["subnets"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_network_peerings"] = None
        return VirtualNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> pulumi.Output[Optional['outputs.AddressSpaceResponse']]:
        """
        The AddressSpace that contains an array of IP address ranges that can be used by subnets.
        """
        return pulumi.get(self, "address_space")

    @property
    @pulumi.getter(name="dhcpOptions")
    def dhcp_options(self) -> pulumi.Output[Optional['outputs.DhcpOptionsResponse']]:
        """
        The dhcpOptions that contains an array of DNS servers available to VMs deployed in the virtual network.
        """
        return pulumi.get(self, "dhcp_options")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets a unique read-only string that changes whenever the resource is updated.
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
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning state of the PublicIP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[Optional[str]]:
        """
        The resourceGuid property of the Virtual Network resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Optional[Sequence['outputs.SubnetResponse']]]:
        """
        A list of subnets in a Virtual Network.
        """
        return pulumi.get(self, "subnets")

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
    @pulumi.getter(name="virtualNetworkPeerings")
    def virtual_network_peerings(self) -> pulumi.Output[Optional[Sequence['outputs.VirtualNetworkPeeringResponse']]]:
        """
        A list of peerings in a Virtual Network.
        """
        return pulumi.get(self, "virtual_network_peerings")

