# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ListSecretValueResult',
    'AwaitableListSecretValueResult',
    'list_secret_value',
]

@pulumi.output_type
class ListSecretValueResult:
    """
    This type represents the unencrypted value of the secret.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The actual value of the secret.
        """
        return pulumi.get(self, "value")


class AwaitableListSecretValueResult(ListSecretValueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListSecretValueResult(
            value=self.value)


def list_secret_value(resource_group_name: Optional[str] = None,
                      secret_resource_name: Optional[str] = None,
                      secret_value_resource_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSecretValueResult:
    """
    This type represents the unencrypted value of the secret.
    API Version: 2018-09-01-preview.


    :param str resource_group_name: Azure resource group name
    :param str secret_resource_name: The name of the secret resource.
    :param str secret_value_resource_name: The name of the secret resource value which is typically the version identifier for the value.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['secretResourceName'] = secret_resource_name
    __args__['secretValueResourceName'] = secret_value_resource_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabricmesh:listSecretValue', __args__, opts=opts, typ=ListSecretValueResult).value

    return AwaitableListSecretValueResult(
        value=__ret__.value)
