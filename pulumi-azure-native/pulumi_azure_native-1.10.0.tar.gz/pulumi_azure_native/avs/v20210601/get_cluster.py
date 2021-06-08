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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
]

@pulumi.output_type
class GetClusterResult:
    """
    A cluster resource
    """
    def __init__(__self__, cluster_id=None, cluster_size=None, hosts=None, id=None, name=None, provisioning_state=None, sku=None, type=None):
        if cluster_id and not isinstance(cluster_id, int):
            raise TypeError("Expected argument 'cluster_id' to be a int")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if cluster_size and not isinstance(cluster_size, int):
            raise TypeError("Expected argument 'cluster_size' to be a int")
        pulumi.set(__self__, "cluster_size", cluster_size)
        if hosts and not isinstance(hosts, list):
            raise TypeError("Expected argument 'hosts' to be a list")
        pulumi.set(__self__, "hosts", hosts)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> int:
        """
        The identity
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="clusterSize")
    def cluster_size(self) -> Optional[int]:
        """
        The cluster size
        """
        return pulumi.get(self, "cluster_size")

    @property
    @pulumi.getter
    def hosts(self) -> Sequence[str]:
        """
        The hosts
        """
        return pulumi.get(self, "hosts")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The state of the cluster provisioning
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        The cluster SKU
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            cluster_id=self.cluster_id,
            cluster_size=self.cluster_size,
            hosts=self.hosts,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            type=self.type)


def get_cluster(cluster_name: Optional[str] = None,
                private_cloud_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    A cluster resource


    :param str cluster_name: Name of the cluster in the private cloud
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['privateCloudName'] = private_cloud_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:avs/v20210601:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        cluster_id=__ret__.cluster_id,
        cluster_size=__ret__.cluster_size,
        hosts=__ret__.hosts,
        id=__ret__.id,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        sku=__ret__.sku,
        type=__ret__.type)
