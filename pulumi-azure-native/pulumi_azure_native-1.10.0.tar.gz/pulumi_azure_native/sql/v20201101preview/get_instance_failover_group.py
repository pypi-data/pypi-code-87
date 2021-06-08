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
    'GetInstanceFailoverGroupResult',
    'AwaitableGetInstanceFailoverGroupResult',
    'get_instance_failover_group',
]

@pulumi.output_type
class GetInstanceFailoverGroupResult:
    """
    An instance failover group.
    """
    def __init__(__self__, id=None, managed_instance_pairs=None, name=None, partner_regions=None, read_only_endpoint=None, read_write_endpoint=None, replication_role=None, replication_state=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_instance_pairs and not isinstance(managed_instance_pairs, list):
            raise TypeError("Expected argument 'managed_instance_pairs' to be a list")
        pulumi.set(__self__, "managed_instance_pairs", managed_instance_pairs)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partner_regions and not isinstance(partner_regions, list):
            raise TypeError("Expected argument 'partner_regions' to be a list")
        pulumi.set(__self__, "partner_regions", partner_regions)
        if read_only_endpoint and not isinstance(read_only_endpoint, dict):
            raise TypeError("Expected argument 'read_only_endpoint' to be a dict")
        pulumi.set(__self__, "read_only_endpoint", read_only_endpoint)
        if read_write_endpoint and not isinstance(read_write_endpoint, dict):
            raise TypeError("Expected argument 'read_write_endpoint' to be a dict")
        pulumi.set(__self__, "read_write_endpoint", read_write_endpoint)
        if replication_role and not isinstance(replication_role, str):
            raise TypeError("Expected argument 'replication_role' to be a str")
        pulumi.set(__self__, "replication_role", replication_role)
        if replication_state and not isinstance(replication_state, str):
            raise TypeError("Expected argument 'replication_state' to be a str")
        pulumi.set(__self__, "replication_state", replication_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedInstancePairs")
    def managed_instance_pairs(self) -> Sequence['outputs.ManagedInstancePairInfoResponse']:
        """
        List of managed instance pairs in the failover group.
        """
        return pulumi.get(self, "managed_instance_pairs")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerRegions")
    def partner_regions(self) -> Sequence['outputs.PartnerRegionInfoResponse']:
        """
        Partner region information for the failover group.
        """
        return pulumi.get(self, "partner_regions")

    @property
    @pulumi.getter(name="readOnlyEndpoint")
    def read_only_endpoint(self) -> Optional['outputs.InstanceFailoverGroupReadOnlyEndpointResponse']:
        """
        Read-only endpoint of the failover group instance.
        """
        return pulumi.get(self, "read_only_endpoint")

    @property
    @pulumi.getter(name="readWriteEndpoint")
    def read_write_endpoint(self) -> 'outputs.InstanceFailoverGroupReadWriteEndpointResponse':
        """
        Read-write endpoint of the failover group instance.
        """
        return pulumi.get(self, "read_write_endpoint")

    @property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> str:
        """
        Local replication role of the failover group instance.
        """
        return pulumi.get(self, "replication_role")

    @property
    @pulumi.getter(name="replicationState")
    def replication_state(self) -> str:
        """
        Replication state of the failover group instance.
        """
        return pulumi.get(self, "replication_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetInstanceFailoverGroupResult(GetInstanceFailoverGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceFailoverGroupResult(
            id=self.id,
            managed_instance_pairs=self.managed_instance_pairs,
            name=self.name,
            partner_regions=self.partner_regions,
            read_only_endpoint=self.read_only_endpoint,
            read_write_endpoint=self.read_write_endpoint,
            replication_role=self.replication_role,
            replication_state=self.replication_state,
            type=self.type)


def get_instance_failover_group(failover_group_name: Optional[str] = None,
                                location_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceFailoverGroupResult:
    """
    An instance failover group.


    :param str failover_group_name: The name of the failover group.
    :param str location_name: The name of the region where the resource is located.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['failoverGroupName'] = failover_group_name
    __args__['locationName'] = location_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20201101preview:getInstanceFailoverGroup', __args__, opts=opts, typ=GetInstanceFailoverGroupResult).value

    return AwaitableGetInstanceFailoverGroupResult(
        id=__ret__.id,
        managed_instance_pairs=__ret__.managed_instance_pairs,
        name=__ret__.name,
        partner_regions=__ret__.partner_regions,
        read_only_endpoint=__ret__.read_only_endpoint,
        read_write_endpoint=__ret__.read_write_endpoint,
        replication_role=__ret__.replication_role,
        replication_state=__ret__.replication_state,
        type=__ret__.type)
