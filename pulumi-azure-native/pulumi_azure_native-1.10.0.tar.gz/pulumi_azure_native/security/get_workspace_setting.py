# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetWorkspaceSettingResult',
    'AwaitableGetWorkspaceSettingResult',
    'get_workspace_setting',
]

@pulumi.output_type
class GetWorkspaceSettingResult:
    """
    Configures where to store the OMS agent data for workspaces under a scope
    """
    def __init__(__self__, id=None, name=None, scope=None, type=None, workspace_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if workspace_id and not isinstance(workspace_id, str):
            raise TypeError("Expected argument 'workspace_id' to be a str")
        pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scope(self) -> str:
        """
        All the VMs in this scope will send their security data to the mentioned workspace unless overridden by a setting with more specific scope
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> str:
        """
        The full Azure ID of the workspace to save the data in
        """
        return pulumi.get(self, "workspace_id")


class AwaitableGetWorkspaceSettingResult(GetWorkspaceSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceSettingResult(
            id=self.id,
            name=self.name,
            scope=self.scope,
            type=self.type,
            workspace_id=self.workspace_id)


def get_workspace_setting(workspace_setting_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceSettingResult:
    """
    Configures where to store the OMS agent data for workspaces under a scope
    API Version: 2017-08-01-preview.


    :param str workspace_setting_name: Name of the security setting
    """
    __args__ = dict()
    __args__['workspaceSettingName'] = workspace_setting_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:security:getWorkspaceSetting', __args__, opts=opts, typ=GetWorkspaceSettingResult).value

    return AwaitableGetWorkspaceSettingResult(
        id=__ret__.id,
        name=__ret__.name,
        scope=__ret__.scope,
        type=__ret__.type,
        workspace_id=__ret__.workspace_id)
