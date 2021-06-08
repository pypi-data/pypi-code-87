# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['WebAppSourceControlSlotArgs', 'WebAppSourceControlSlot']

@pulumi.input_type
class WebAppSourceControlSlotArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 slot: pulumi.Input[str],
                 branch: Optional[pulumi.Input[str]] = None,
                 deployment_rollback_enabled: Optional[pulumi.Input[bool]] = None,
                 is_git_hub_action: Optional[pulumi.Input[bool]] = None,
                 is_manual_integration: Optional[pulumi.Input[bool]] = None,
                 is_mercurial: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 repo_url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebAppSourceControlSlot resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] slot: Name of the deployment slot. If a slot is not specified, the API will update the source control configuration for the production slot.
        :param pulumi.Input[str] branch: Name of branch to use for deployment.
        :param pulumi.Input[bool] deployment_rollback_enabled: <code>true</code> to enable deployment rollback; otherwise, <code>false</code>.
        :param pulumi.Input[bool] is_git_hub_action: <code>true</code> if this is deployed via GitHub action.
        :param pulumi.Input[bool] is_manual_integration: <code>true</code> to limit to manual integration; <code>false</code> to enable continuous integration (which configures webhooks into online repos like GitHub).
        :param pulumi.Input[bool] is_mercurial: <code>true</code> for a Mercurial repository; <code>false</code> for a Git repository.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] repo_url: Repository or source control URL.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "slot", slot)
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if deployment_rollback_enabled is not None:
            pulumi.set(__self__, "deployment_rollback_enabled", deployment_rollback_enabled)
        if is_git_hub_action is not None:
            pulumi.set(__self__, "is_git_hub_action", is_git_hub_action)
        if is_manual_integration is not None:
            pulumi.set(__self__, "is_manual_integration", is_manual_integration)
        if is_mercurial is not None:
            pulumi.set(__self__, "is_mercurial", is_mercurial)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if repo_url is not None:
            pulumi.set(__self__, "repo_url", repo_url)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the app.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def slot(self) -> pulumi.Input[str]:
        """
        Name of the deployment slot. If a slot is not specified, the API will update the source control configuration for the production slot.
        """
        return pulumi.get(self, "slot")

    @slot.setter
    def slot(self, value: pulumi.Input[str]):
        pulumi.set(self, "slot", value)

    @property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[str]]:
        """
        Name of branch to use for deployment.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter(name="deploymentRollbackEnabled")
    def deployment_rollback_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        <code>true</code> to enable deployment rollback; otherwise, <code>false</code>.
        """
        return pulumi.get(self, "deployment_rollback_enabled")

    @deployment_rollback_enabled.setter
    def deployment_rollback_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deployment_rollback_enabled", value)

    @property
    @pulumi.getter(name="isGitHubAction")
    def is_git_hub_action(self) -> Optional[pulumi.Input[bool]]:
        """
        <code>true</code> if this is deployed via GitHub action.
        """
        return pulumi.get(self, "is_git_hub_action")

    @is_git_hub_action.setter
    def is_git_hub_action(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_git_hub_action", value)

    @property
    @pulumi.getter(name="isManualIntegration")
    def is_manual_integration(self) -> Optional[pulumi.Input[bool]]:
        """
        <code>true</code> to limit to manual integration; <code>false</code> to enable continuous integration (which configures webhooks into online repos like GitHub).
        """
        return pulumi.get(self, "is_manual_integration")

    @is_manual_integration.setter
    def is_manual_integration(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_manual_integration", value)

    @property
    @pulumi.getter(name="isMercurial")
    def is_mercurial(self) -> Optional[pulumi.Input[bool]]:
        """
        <code>true</code> for a Mercurial repository; <code>false</code> for a Git repository.
        """
        return pulumi.get(self, "is_mercurial")

    @is_mercurial.setter
    def is_mercurial(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_mercurial", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> Optional[pulumi.Input[str]]:
        """
        Repository or source control URL.
        """
        return pulumi.get(self, "repo_url")

    @repo_url.setter
    def repo_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_url", value)


class WebAppSourceControlSlot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 deployment_rollback_enabled: Optional[pulumi.Input[bool]] = None,
                 is_git_hub_action: Optional[pulumi.Input[bool]] = None,
                 is_manual_integration: Optional[pulumi.Input[bool]] = None,
                 is_mercurial: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 repo_url: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 slot: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Source control configuration for an app.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch: Name of branch to use for deployment.
        :param pulumi.Input[bool] deployment_rollback_enabled: <code>true</code> to enable deployment rollback; otherwise, <code>false</code>.
        :param pulumi.Input[bool] is_git_hub_action: <code>true</code> if this is deployed via GitHub action.
        :param pulumi.Input[bool] is_manual_integration: <code>true</code> to limit to manual integration; <code>false</code> to enable continuous integration (which configures webhooks into online repos like GitHub).
        :param pulumi.Input[bool] is_mercurial: <code>true</code> for a Mercurial repository; <code>false</code> for a Git repository.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] repo_url: Repository or source control URL.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] slot: Name of the deployment slot. If a slot is not specified, the API will update the source control configuration for the production slot.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAppSourceControlSlotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Source control configuration for an app.

        :param str resource_name: The name of the resource.
        :param WebAppSourceControlSlotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAppSourceControlSlotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 deployment_rollback_enabled: Optional[pulumi.Input[bool]] = None,
                 is_git_hub_action: Optional[pulumi.Input[bool]] = None,
                 is_manual_integration: Optional[pulumi.Input[bool]] = None,
                 is_mercurial: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 repo_url: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 slot: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebAppSourceControlSlotArgs.__new__(WebAppSourceControlSlotArgs)

            __props__.__dict__["branch"] = branch
            __props__.__dict__["deployment_rollback_enabled"] = deployment_rollback_enabled
            __props__.__dict__["is_git_hub_action"] = is_git_hub_action
            __props__.__dict__["is_manual_integration"] = is_manual_integration
            __props__.__dict__["is_mercurial"] = is_mercurial
            __props__.__dict__["kind"] = kind
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["repo_url"] = repo_url
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if slot is None and not opts.urn:
                raise TypeError("Missing required property 'slot'")
            __props__.__dict__["slot"] = slot
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:web/v20200901:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-native:web:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-nextgen:web:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-native:web/v20150801:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-nextgen:web/v20150801:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-native:web/v20160801:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-nextgen:web/v20160801:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-native:web/v20180201:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-nextgen:web/v20180201:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-native:web/v20181101:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-nextgen:web/v20181101:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-native:web/v20190801:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-nextgen:web/v20190801:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-native:web/v20200601:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-nextgen:web/v20200601:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-native:web/v20201001:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-nextgen:web/v20201001:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-native:web/v20201201:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-nextgen:web/v20201201:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-native:web/v20210101:WebAppSourceControlSlot"), pulumi.Alias(type_="azure-nextgen:web/v20210101:WebAppSourceControlSlot")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WebAppSourceControlSlot, __self__).__init__(
            'azure-native:web/v20200901:WebAppSourceControlSlot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebAppSourceControlSlot':
        """
        Get an existing WebAppSourceControlSlot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebAppSourceControlSlotArgs.__new__(WebAppSourceControlSlotArgs)

        __props__.__dict__["branch"] = None
        __props__.__dict__["deployment_rollback_enabled"] = None
        __props__.__dict__["is_git_hub_action"] = None
        __props__.__dict__["is_manual_integration"] = None
        __props__.__dict__["is_mercurial"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["repo_url"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return WebAppSourceControlSlot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Output[Optional[str]]:
        """
        Name of branch to use for deployment.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="deploymentRollbackEnabled")
    def deployment_rollback_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        <code>true</code> to enable deployment rollback; otherwise, <code>false</code>.
        """
        return pulumi.get(self, "deployment_rollback_enabled")

    @property
    @pulumi.getter(name="isGitHubAction")
    def is_git_hub_action(self) -> pulumi.Output[Optional[bool]]:
        """
        <code>true</code> if this is deployed via GitHub action.
        """
        return pulumi.get(self, "is_git_hub_action")

    @property
    @pulumi.getter(name="isManualIntegration")
    def is_manual_integration(self) -> pulumi.Output[Optional[bool]]:
        """
        <code>true</code> to limit to manual integration; <code>false</code> to enable continuous integration (which configures webhooks into online repos like GitHub).
        """
        return pulumi.get(self, "is_manual_integration")

    @property
    @pulumi.getter(name="isMercurial")
    def is_mercurial(self) -> pulumi.Output[Optional[bool]]:
        """
        <code>true</code> for a Mercurial repository; <code>false</code> for a Git repository.
        """
        return pulumi.get(self, "is_mercurial")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> pulumi.Output[Optional[str]]:
        """
        Repository or source control URL.
        """
        return pulumi.get(self, "repo_url")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

