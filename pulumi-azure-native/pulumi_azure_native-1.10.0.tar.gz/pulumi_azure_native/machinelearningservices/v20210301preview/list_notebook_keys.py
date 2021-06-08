# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListNotebookKeysResult',
    'AwaitableListNotebookKeysResult',
    'list_notebook_keys',
]

@pulumi.output_type
class ListNotebookKeysResult:
    def __init__(__self__, primary_access_key=None, secondary_access_key=None):
        if primary_access_key and not isinstance(primary_access_key, str):
            raise TypeError("Expected argument 'primary_access_key' to be a str")
        pulumi.set(__self__, "primary_access_key", primary_access_key)
        if secondary_access_key and not isinstance(secondary_access_key, str):
            raise TypeError("Expected argument 'secondary_access_key' to be a str")
        pulumi.set(__self__, "secondary_access_key", secondary_access_key)

    @property
    @pulumi.getter(name="primaryAccessKey")
    def primary_access_key(self) -> str:
        return pulumi.get(self, "primary_access_key")

    @property
    @pulumi.getter(name="secondaryAccessKey")
    def secondary_access_key(self) -> str:
        return pulumi.get(self, "secondary_access_key")


class AwaitableListNotebookKeysResult(ListNotebookKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListNotebookKeysResult(
            primary_access_key=self.primary_access_key,
            secondary_access_key=self.secondary_access_key)


def list_notebook_keys(resource_group_name: Optional[str] = None,
                       workspace_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListNotebookKeysResult:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20210301preview:listNotebookKeys', __args__, opts=opts, typ=ListNotebookKeysResult).value

    return AwaitableListNotebookKeysResult(
        primary_access_key=__ret__.primary_access_key,
        secondary_access_key=__ret__.secondary_access_key)
