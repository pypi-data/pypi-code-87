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
    'GetSentinelOnboardingStateResult',
    'AwaitableGetSentinelOnboardingStateResult',
    'get_sentinel_onboarding_state',
]

@pulumi.output_type
class GetSentinelOnboardingStateResult:
    """
    Sentinel onboarding state
    """
    def __init__(__self__, customer_managed_key=None, etag=None, id=None, name=None, system_data=None, type=None):
        if customer_managed_key and not isinstance(customer_managed_key, bool):
            raise TypeError("Expected argument 'customer_managed_key' to be a bool")
        pulumi.set(__self__, "customer_managed_key", customer_managed_key)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> Optional[bool]:
        """
        Flag that indicates the status of the CMK setting
        """
        return pulumi.get(self, "customer_managed_key")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetSentinelOnboardingStateResult(GetSentinelOnboardingStateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSentinelOnboardingStateResult(
            customer_managed_key=self.customer_managed_key,
            etag=self.etag,
            id=self.id,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_sentinel_onboarding_state(operational_insights_resource_provider: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  sentinel_onboarding_state_name: Optional[str] = None,
                                  workspace_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSentinelOnboardingStateResult:
    """
    Sentinel onboarding state


    :param str operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sentinel_onboarding_state_name: The Sentinel onboarding state name. Supports - default
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['operationalInsightsResourceProvider'] = operational_insights_resource_provider
    __args__['resourceGroupName'] = resource_group_name
    __args__['sentinelOnboardingStateName'] = sentinel_onboarding_state_name
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20210301preview:getSentinelOnboardingState', __args__, opts=opts, typ=GetSentinelOnboardingStateResult).value

    return AwaitableGetSentinelOnboardingStateResult(
        customer_managed_key=__ret__.customer_managed_key,
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        system_data=__ret__.system_data,
        type=__ret__.type)
