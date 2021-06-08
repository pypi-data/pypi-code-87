# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetVirtualNetworkPeeringResult',
    'AwaitableGetVirtualNetworkPeeringResult',
    'get_virtual_network_peering',
]

@pulumi.output_type
class GetVirtualNetworkPeeringResult:
    """
    Peerings in a virtual network resource.
    """
    def __init__(__self__, allow_forwarded_traffic=None, allow_gateway_transit=None, allow_virtual_network_access=None, etag=None, id=None, name=None, peering_state=None, provisioning_state=None, remote_address_space=None, remote_virtual_network=None, use_remote_gateways=None):
        if allow_forwarded_traffic and not isinstance(allow_forwarded_traffic, bool):
            raise TypeError("Expected argument 'allow_forwarded_traffic' to be a bool")
        pulumi.set(__self__, "allow_forwarded_traffic", allow_forwarded_traffic)
        if allow_gateway_transit and not isinstance(allow_gateway_transit, bool):
            raise TypeError("Expected argument 'allow_gateway_transit' to be a bool")
        pulumi.set(__self__, "allow_gateway_transit", allow_gateway_transit)
        if allow_virtual_network_access and not isinstance(allow_virtual_network_access, bool):
            raise TypeError("Expected argument 'allow_virtual_network_access' to be a bool")
        pulumi.set(__self__, "allow_virtual_network_access", allow_virtual_network_access)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peering_state and not isinstance(peering_state, str):
            raise TypeError("Expected argument 'peering_state' to be a str")
        pulumi.set(__self__, "peering_state", peering_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if remote_address_space and not isinstance(remote_address_space, dict):
            raise TypeError("Expected argument 'remote_address_space' to be a dict")
        pulumi.set(__self__, "remote_address_space", remote_address_space)
        if remote_virtual_network and not isinstance(remote_virtual_network, dict):
            raise TypeError("Expected argument 'remote_virtual_network' to be a dict")
        pulumi.set(__self__, "remote_virtual_network", remote_virtual_network)
        if use_remote_gateways and not isinstance(use_remote_gateways, bool):
            raise TypeError("Expected argument 'use_remote_gateways' to be a bool")
        pulumi.set(__self__, "use_remote_gateways", use_remote_gateways)

    @property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> Optional[bool]:
        """
        Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.
        """
        return pulumi.get(self, "allow_forwarded_traffic")

    @property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> Optional[bool]:
        """
        If gateway links can be used in remote virtual networking to link to this virtual network.
        """
        return pulumi.get(self, "allow_gateway_transit")

    @property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(self) -> Optional[bool]:
        """
        Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.
        """
        return pulumi.get(self, "allow_virtual_network_access")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peeringState")
    def peering_state(self) -> Optional[str]:
        """
        The status of the virtual network peering.
        """
        return pulumi.get(self, "peering_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the virtual network peering resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="remoteAddressSpace")
    def remote_address_space(self) -> Optional['outputs.AddressSpaceResponse']:
        """
        The reference to the remote virtual network address space.
        """
        return pulumi.get(self, "remote_address_space")

    @property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(self) -> Optional['outputs.SubResourceResponse']:
        """
        The reference to the remote virtual network. The remote virtual network can be in the same or different region (preview). See here to register for the preview and learn more (https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-create-peering).
        """
        return pulumi.get(self, "remote_virtual_network")

    @property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> Optional[bool]:
        """
        If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
        """
        return pulumi.get(self, "use_remote_gateways")


class AwaitableGetVirtualNetworkPeeringResult(GetVirtualNetworkPeeringResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNetworkPeeringResult(
            allow_forwarded_traffic=self.allow_forwarded_traffic,
            allow_gateway_transit=self.allow_gateway_transit,
            allow_virtual_network_access=self.allow_virtual_network_access,
            etag=self.etag,
            id=self.id,
            name=self.name,
            peering_state=self.peering_state,
            provisioning_state=self.provisioning_state,
            remote_address_space=self.remote_address_space,
            remote_virtual_network=self.remote_virtual_network,
            use_remote_gateways=self.use_remote_gateways)


def get_virtual_network_peering(resource_group_name: Optional[str] = None,
                                virtual_network_name: Optional[str] = None,
                                virtual_network_peering_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNetworkPeeringResult:
    """
    Peerings in a virtual network resource.


    :param str resource_group_name: The name of the resource group.
    :param str virtual_network_name: The name of the virtual network.
    :param str virtual_network_peering_name: The name of the virtual network peering.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualNetworkName'] = virtual_network_name
    __args__['virtualNetworkPeeringName'] = virtual_network_peering_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20191201:getVirtualNetworkPeering', __args__, opts=opts, typ=GetVirtualNetworkPeeringResult).value

    return AwaitableGetVirtualNetworkPeeringResult(
        allow_forwarded_traffic=__ret__.allow_forwarded_traffic,
        allow_gateway_transit=__ret__.allow_gateway_transit,
        allow_virtual_network_access=__ret__.allow_virtual_network_access,
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        peering_state=__ret__.peering_state,
        provisioning_state=__ret__.provisioning_state,
        remote_address_space=__ret__.remote_address_space,
        remote_virtual_network=__ret__.remote_virtual_network,
        use_remote_gateways=__ret__.use_remote_gateways)
