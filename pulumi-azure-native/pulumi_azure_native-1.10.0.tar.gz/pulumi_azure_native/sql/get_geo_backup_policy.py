# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetGeoBackupPolicyResult',
    'AwaitableGetGeoBackupPolicyResult',
    'get_geo_backup_policy',
]

@pulumi.output_type
class GetGeoBackupPolicyResult:
    """
    A database geo backup policy.
    """
    def __init__(__self__, id=None, kind=None, location=None, name=None, state=None, storage_type=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)
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
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of geo backup policy.  This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Backup policy location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the geo backup policy.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> str:
        """
        The storage type of the geo backup policy.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetGeoBackupPolicyResult(GetGeoBackupPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGeoBackupPolicyResult(
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            state=self.state,
            storage_type=self.storage_type,
            type=self.type)


def get_geo_backup_policy(database_name: Optional[str] = None,
                          geo_backup_policy_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          server_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGeoBackupPolicyResult:
    """
    A database geo backup policy.
    API Version: 2014-04-01.


    :param str database_name: The name of the database.
    :param str geo_backup_policy_name: The name of the geo backup policy.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['geoBackupPolicyName'] = geo_backup_policy_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:sql:getGeoBackupPolicy', __args__, opts=opts, typ=GetGeoBackupPolicyResult).value

    return AwaitableGetGeoBackupPolicyResult(
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        state=__ret__.state,
        storage_type=__ret__.storage_type,
        type=__ret__.type)
