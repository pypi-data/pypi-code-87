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
    'GetExpressRouteCircuitConnectionResult',
    'AwaitableGetExpressRouteCircuitConnectionResult',
    'get_express_route_circuit_connection',
]

@pulumi.output_type
class GetExpressRouteCircuitConnectionResult:
    """
    Express Route Circuit Connection in an ExpressRouteCircuitPeering resource.
    """
    def __init__(__self__, address_prefix=None, authorization_key=None, circuit_connection_status=None, etag=None, express_route_circuit_peering=None, id=None, name=None, peer_express_route_circuit_peering=None, provisioning_state=None, type=None):
        if address_prefix and not isinstance(address_prefix, str):
            raise TypeError("Expected argument 'address_prefix' to be a str")
        pulumi.set(__self__, "address_prefix", address_prefix)
        if authorization_key and not isinstance(authorization_key, str):
            raise TypeError("Expected argument 'authorization_key' to be a str")
        pulumi.set(__self__, "authorization_key", authorization_key)
        if circuit_connection_status and not isinstance(circuit_connection_status, str):
            raise TypeError("Expected argument 'circuit_connection_status' to be a str")
        pulumi.set(__self__, "circuit_connection_status", circuit_connection_status)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if express_route_circuit_peering and not isinstance(express_route_circuit_peering, dict):
            raise TypeError("Expected argument 'express_route_circuit_peering' to be a dict")
        pulumi.set(__self__, "express_route_circuit_peering", express_route_circuit_peering)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peer_express_route_circuit_peering and not isinstance(peer_express_route_circuit_peering, dict):
            raise TypeError("Expected argument 'peer_express_route_circuit_peering' to be a dict")
        pulumi.set(__self__, "peer_express_route_circuit_peering", peer_express_route_circuit_peering)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[str]:
        """
        /29 IP address space to carve out Customer addresses for tunnels.
        """
        return pulumi.get(self, "address_prefix")

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[str]:
        """
        The authorization key.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="circuitConnectionStatus")
    def circuit_connection_status(self) -> str:
        """
        Express Route Circuit connection state.
        """
        return pulumi.get(self, "circuit_connection_status")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> Optional['outputs.SubResourceResponse']:
        """
        Reference to Express Route Circuit Private Peering Resource of the circuit initiating connection.
        """
        return pulumi.get(self, "express_route_circuit_peering")

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
        Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerExpressRouteCircuitPeering")
    def peer_express_route_circuit_peering(self) -> Optional['outputs.SubResourceResponse']:
        """
        Reference to Express Route Circuit Private Peering Resource of the peered circuit.
        """
        return pulumi.get(self, "peer_express_route_circuit_peering")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the circuit connection resource. Possible values are: 'Succeeded', 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetExpressRouteCircuitConnectionResult(GetExpressRouteCircuitConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExpressRouteCircuitConnectionResult(
            address_prefix=self.address_prefix,
            authorization_key=self.authorization_key,
            circuit_connection_status=self.circuit_connection_status,
            etag=self.etag,
            express_route_circuit_peering=self.express_route_circuit_peering,
            id=self.id,
            name=self.name,
            peer_express_route_circuit_peering=self.peer_express_route_circuit_peering,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_express_route_circuit_connection(circuit_name: Optional[str] = None,
                                         connection_name: Optional[str] = None,
                                         peering_name: Optional[str] = None,
                                         resource_group_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExpressRouteCircuitConnectionResult:
    """
    Express Route Circuit Connection in an ExpressRouteCircuitPeering resource.


    :param str circuit_name: The name of the express route circuit.
    :param str connection_name: The name of the express route circuit connection.
    :param str peering_name: The name of the peering.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['circuitName'] = circuit_name
    __args__['connectionName'] = connection_name
    __args__['peeringName'] = peering_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20190401:getExpressRouteCircuitConnection', __args__, opts=opts, typ=GetExpressRouteCircuitConnectionResult).value

    return AwaitableGetExpressRouteCircuitConnectionResult(
        address_prefix=__ret__.address_prefix,
        authorization_key=__ret__.authorization_key,
        circuit_connection_status=__ret__.circuit_connection_status,
        etag=__ret__.etag,
        express_route_circuit_peering=__ret__.express_route_circuit_peering,
        id=__ret__.id,
        name=__ret__.name,
        peer_express_route_circuit_peering=__ret__.peer_express_route_circuit_peering,
        provisioning_state=__ret__.provisioning_state,
        type=__ret__.type)
