# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ApplicationGroupArgs', 'ApplicationGroup']

@pulumi.input_type
class ApplicationGroupArgs:
    def __init__(__self__, *,
                 application_group_type: pulumi.Input[Union[str, 'ApplicationGroupType']],
                 host_pool_arm_path: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 application_group_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ApplicationGroup resource.
        :param pulumi.Input[Union[str, 'ApplicationGroupType']] application_group_type: Resource Type of ApplicationGroup.
        :param pulumi.Input[str] host_pool_arm_path: HostPool arm path of ApplicationGroup.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] application_group_name: The name of the application group
        :param pulumi.Input[str] description: Description of ApplicationGroup.
        :param pulumi.Input[str] friendly_name: Friendly name of ApplicationGroup.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "application_group_type", application_group_type)
        pulumi.set(__self__, "host_pool_arm_path", host_pool_arm_path)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if application_group_name is not None:
            pulumi.set(__self__, "application_group_name", application_group_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="applicationGroupType")
    def application_group_type(self) -> pulumi.Input[Union[str, 'ApplicationGroupType']]:
        """
        Resource Type of ApplicationGroup.
        """
        return pulumi.get(self, "application_group_type")

    @application_group_type.setter
    def application_group_type(self, value: pulumi.Input[Union[str, 'ApplicationGroupType']]):
        pulumi.set(self, "application_group_type", value)

    @property
    @pulumi.getter(name="hostPoolArmPath")
    def host_pool_arm_path(self) -> pulumi.Input[str]:
        """
        HostPool arm path of ApplicationGroup.
        """
        return pulumi.get(self, "host_pool_arm_path")

    @host_pool_arm_path.setter
    def host_pool_arm_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_pool_arm_path", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="applicationGroupName")
    def application_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the application group
        """
        return pulumi.get(self, "application_group_name")

    @application_group_name.setter
    def application_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_group_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of ApplicationGroup.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name of ApplicationGroup.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ApplicationGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_group_name: Optional[pulumi.Input[str]] = None,
                 application_group_type: Optional[pulumi.Input[Union[str, 'ApplicationGroupType']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_pool_arm_path: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents a ApplicationGroup definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_group_name: The name of the application group
        :param pulumi.Input[Union[str, 'ApplicationGroupType']] application_group_type: Resource Type of ApplicationGroup.
        :param pulumi.Input[str] description: Description of ApplicationGroup.
        :param pulumi.Input[str] friendly_name: Friendly name of ApplicationGroup.
        :param pulumi.Input[str] host_pool_arm_path: HostPool arm path of ApplicationGroup.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a ApplicationGroup definition.

        :param str resource_name: The name of the resource.
        :param ApplicationGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_group_name: Optional[pulumi.Input[str]] = None,
                 application_group_type: Optional[pulumi.Input[Union[str, 'ApplicationGroupType']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_pool_arm_path: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = ApplicationGroupArgs.__new__(ApplicationGroupArgs)

            __props__.__dict__["application_group_name"] = application_group_name
            if application_group_type is None and not opts.urn:
                raise TypeError("Missing required property 'application_group_type'")
            __props__.__dict__["application_group_type"] = application_group_type
            __props__.__dict__["description"] = description
            __props__.__dict__["friendly_name"] = friendly_name
            if host_pool_arm_path is None and not opts.urn:
                raise TypeError("Missing required property 'host_pool_arm_path'")
            __props__.__dict__["host_pool_arm_path"] = host_pool_arm_path
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["workspace_arm_path"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20201110preview:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20190123preview:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20190123preview:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20190924preview:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20190924preview:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20191210preview:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20191210preview:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20200921preview:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20200921preview:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20201019preview:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20201019preview:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20201102preview:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20201102preview:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210114preview:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20210114preview:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210201preview:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20210201preview:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210309preview:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20210309preview:ApplicationGroup"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210401preview:ApplicationGroup"), pulumi.Alias(type_="azure-nextgen:desktopvirtualization/v20210401preview:ApplicationGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApplicationGroup, __self__).__init__(
            'azure-native:desktopvirtualization/v20201110preview:ApplicationGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationGroup':
        """
        Get an existing ApplicationGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationGroupArgs.__new__(ApplicationGroupArgs)

        __props__.__dict__["application_group_type"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["friendly_name"] = None
        __props__.__dict__["host_pool_arm_path"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["workspace_arm_path"] = None
        return ApplicationGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationGroupType")
    def application_group_type(self) -> pulumi.Output[str]:
        """
        Resource Type of ApplicationGroup.
        """
        return pulumi.get(self, "application_group_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of ApplicationGroup.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        Friendly name of ApplicationGroup.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hostPoolArmPath")
    def host_pool_arm_path(self) -> pulumi.Output[str]:
        """
        HostPool arm path of ApplicationGroup.
        """
        return pulumi.get(self, "host_pool_arm_path")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceArmPath")
    def workspace_arm_path(self) -> pulumi.Output[str]:
        """
        Workspace arm path of ApplicationGroup.
        """
        return pulumi.get(self, "workspace_arm_path")

