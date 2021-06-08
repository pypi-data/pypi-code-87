# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['NotificationRegistrationArgs', 'NotificationRegistration']

@pulumi.input_type
class NotificationRegistrationArgs:
    def __init__(__self__, *,
                 provider_namespace: pulumi.Input[str],
                 notification_registration_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['NotificationRegistrationPropertiesArgs']] = None):
        """
        The set of arguments for constructing a NotificationRegistration resource.
        :param pulumi.Input[str] provider_namespace: The name of the resource provider hosted within ProviderHub.
        :param pulumi.Input[str] notification_registration_name: The notification registration.
        """
        pulumi.set(__self__, "provider_namespace", provider_namespace)
        if notification_registration_name is not None:
            pulumi.set(__self__, "notification_registration_name", notification_registration_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="providerNamespace")
    def provider_namespace(self) -> pulumi.Input[str]:
        """
        The name of the resource provider hosted within ProviderHub.
        """
        return pulumi.get(self, "provider_namespace")

    @provider_namespace.setter
    def provider_namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_namespace", value)

    @property
    @pulumi.getter(name="notificationRegistrationName")
    def notification_registration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The notification registration.
        """
        return pulumi.get(self, "notification_registration_name")

    @notification_registration_name.setter
    def notification_registration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notification_registration_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['NotificationRegistrationPropertiesArgs']]:
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['NotificationRegistrationPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class NotificationRegistration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 notification_registration_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['NotificationRegistrationPropertiesArgs']]] = None,
                 provider_namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The notification registration definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] notification_registration_name: The notification registration.
        :param pulumi.Input[str] provider_namespace: The name of the resource provider hosted within ProviderHub.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationRegistrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The notification registration definition.

        :param str resource_name: The name of the resource.
        :param NotificationRegistrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotificationRegistrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 notification_registration_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['NotificationRegistrationPropertiesArgs']]] = None,
                 provider_namespace: Optional[pulumi.Input[str]] = None,
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
            __props__ = NotificationRegistrationArgs.__new__(NotificationRegistrationArgs)

            __props__.__dict__["notification_registration_name"] = notification_registration_name
            __props__.__dict__["properties"] = properties
            if provider_namespace is None and not opts.urn:
                raise TypeError("Missing required property 'provider_namespace'")
            __props__.__dict__["provider_namespace"] = provider_namespace
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:providerhub/v20201120:NotificationRegistration"), pulumi.Alias(type_="azure-native:providerhub:NotificationRegistration"), pulumi.Alias(type_="azure-nextgen:providerhub:NotificationRegistration"), pulumi.Alias(type_="azure-native:providerhub/v20210501preview:NotificationRegistration"), pulumi.Alias(type_="azure-nextgen:providerhub/v20210501preview:NotificationRegistration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NotificationRegistration, __self__).__init__(
            'azure-native:providerhub/v20201120:NotificationRegistration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NotificationRegistration':
        """
        Get an existing NotificationRegistration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NotificationRegistrationArgs.__new__(NotificationRegistrationArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return NotificationRegistration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.NotificationRegistrationResponseProperties']:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

