# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetScheduledSynchronizationSettingResult',
    'AwaitableGetScheduledSynchronizationSettingResult',
    'get_scheduled_synchronization_setting',
]

@pulumi.output_type
class GetScheduledSynchronizationSettingResult:
    """
    A type of synchronization setting based on schedule
    """
    def __init__(__self__, created_at=None, id=None, kind=None, name=None, provisioning_state=None, recurrence_interval=None, synchronization_time=None, type=None, user_name=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if recurrence_interval and not isinstance(recurrence_interval, str):
            raise TypeError("Expected argument 'recurrence_interval' to be a str")
        pulumi.set(__self__, "recurrence_interval", recurrence_interval)
        if synchronization_time and not isinstance(synchronization_time, str):
            raise TypeError("Expected argument 'synchronization_time' to be a str")
        pulumi.set(__self__, "synchronization_time", synchronization_time)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Time at which the synchronization setting was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of synchronization setting.
        Expected value is 'ScheduleBased'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets or sets the provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="recurrenceInterval")
    def recurrence_interval(self) -> str:
        """
        Recurrence Interval
        """
        return pulumi.get(self, "recurrence_interval")

    @property
    @pulumi.getter(name="synchronizationTime")
    def synchronization_time(self) -> str:
        """
        Synchronization time
        """
        return pulumi.get(self, "synchronization_time")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        """
        Name of the user who created the synchronization setting.
        """
        return pulumi.get(self, "user_name")


class AwaitableGetScheduledSynchronizationSettingResult(GetScheduledSynchronizationSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduledSynchronizationSettingResult(
            created_at=self.created_at,
            id=self.id,
            kind=self.kind,
            name=self.name,
            provisioning_state=self.provisioning_state,
            recurrence_interval=self.recurrence_interval,
            synchronization_time=self.synchronization_time,
            type=self.type,
            user_name=self.user_name)


def get_scheduled_synchronization_setting(account_name: Optional[str] = None,
                                          resource_group_name: Optional[str] = None,
                                          share_name: Optional[str] = None,
                                          synchronization_setting_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduledSynchronizationSettingResult:
    """
    A type of synchronization setting based on schedule


    :param str account_name: The name of the share account.
    :param str resource_group_name: The resource group name.
    :param str share_name: The name of the share.
    :param str synchronization_setting_name: The name of the synchronizationSetting.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    __args__['synchronizationSettingName'] = synchronization_setting_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:datashare/v20181101preview:getScheduledSynchronizationSetting', __args__, opts=opts, typ=GetScheduledSynchronizationSettingResult).value

    return AwaitableGetScheduledSynchronizationSettingResult(
        created_at=__ret__.created_at,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        recurrence_interval=__ret__.recurrence_interval,
        synchronization_time=__ret__.synchronization_time,
        type=__ret__.type,
        user_name=__ret__.user_name)
