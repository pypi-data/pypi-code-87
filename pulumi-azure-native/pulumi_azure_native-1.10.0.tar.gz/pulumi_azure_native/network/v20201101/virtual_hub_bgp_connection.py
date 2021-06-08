# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['VirtualHubBgpConnectionArgs', 'VirtualHubBgpConnection']

@pulumi.input_type
class VirtualHubBgpConnectionArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 virtual_hub_name: pulumi.Input[str],
                 connection_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_asn: Optional[pulumi.Input[float]] = None,
                 peer_ip: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualHubBgpConnection resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VirtualHub.
        :param pulumi.Input[str] virtual_hub_name: The name of the VirtualHub.
        :param pulumi.Input[str] connection_name: The name of the connection.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Name of the connection.
        :param pulumi.Input[float] peer_asn: Peer ASN.
        :param pulumi.Input[str] peer_ip: Peer IP.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_hub_name", virtual_hub_name)
        if connection_name is not None:
            pulumi.set(__self__, "connection_name", connection_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if peer_asn is not None:
            pulumi.set(__self__, "peer_asn", peer_asn)
        if peer_ip is not None:
            pulumi.set(__self__, "peer_ip", peer_ip)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the VirtualHub.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> pulumi.Input[str]:
        """
        The name of the VirtualHub.
        """
        return pulumi.get(self, "virtual_hub_name")

    @virtual_hub_name.setter
    def virtual_hub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_hub_name", value)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the connection.
        """
        return pulumi.get(self, "connection_name")

    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_name", value)

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
        Name of the connection.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input[float]]:
        """
        Peer ASN.
        """
        return pulumi.get(self, "peer_asn")

    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "peer_asn", value)

    @property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Peer IP.
        """
        return pulumi.get(self, "peer_ip")

    @peer_ip.setter
    def peer_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_ip", value)


class VirtualHubBgpConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_asn: Optional[pulumi.Input[float]] = None,
                 peer_ip: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_hub_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Virtual Appliance Site resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_name: The name of the connection.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Name of the connection.
        :param pulumi.Input[float] peer_asn: Peer ASN.
        :param pulumi.Input[str] peer_ip: Peer IP.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VirtualHub.
        :param pulumi.Input[str] virtual_hub_name: The name of the VirtualHub.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualHubBgpConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Virtual Appliance Site resource.

        :param str resource_name: The name of the resource.
        :param VirtualHubBgpConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualHubBgpConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_asn: Optional[pulumi.Input[float]] = None,
                 peer_ip: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_hub_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = VirtualHubBgpConnectionArgs.__new__(VirtualHubBgpConnectionArgs)

            __props__.__dict__["connection_name"] = connection_name
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            __props__.__dict__["peer_asn"] = peer_asn
            __props__.__dict__["peer_ip"] = peer_ip
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if virtual_hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_hub_name'")
            __props__.__dict__["virtual_hub_name"] = virtual_hub_name
            __props__.__dict__["connection_state"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20201101:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-nextgen:network:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20200501:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-nextgen:network/v20200501:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20200601:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-nextgen:network/v20200601:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20200701:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-nextgen:network/v20200701:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20200801:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-nextgen:network/v20200801:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-native:network/v20210201:VirtualHubBgpConnection"), pulumi.Alias(type_="azure-nextgen:network/v20210201:VirtualHubBgpConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualHubBgpConnection, __self__).__init__(
            'azure-native:network/v20201101:VirtualHubBgpConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualHubBgpConnection':
        """
        Get an existing VirtualHubBgpConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualHubBgpConnectionArgs.__new__(VirtualHubBgpConnectionArgs)

        __props__.__dict__["connection_state"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peer_asn"] = None
        __props__.__dict__["peer_ip"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return VirtualHubBgpConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> pulumi.Output[str]:
        """
        The current state of the VirtualHub to Peer.
        """
        return pulumi.get(self, "connection_state")

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
        Name of the connection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> pulumi.Output[Optional[float]]:
        """
        Peer ASN.
        """
        return pulumi.get(self, "peer_asn")

    @property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> pulumi.Output[Optional[str]]:
        """
        Peer IP.
        """
        return pulumi.get(self, "peer_ip")

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
        Connection type.
        """
        return pulumi.get(self, "type")

