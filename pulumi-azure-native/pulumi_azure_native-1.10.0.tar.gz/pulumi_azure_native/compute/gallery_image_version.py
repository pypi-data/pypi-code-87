# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['GalleryImageVersionArgs', 'GalleryImageVersion']

@pulumi.input_type
class GalleryImageVersionArgs:
    def __init__(__self__, *,
                 gallery_image_name: pulumi.Input[str],
                 gallery_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_profile: pulumi.Input['GalleryImageVersionStorageProfileArgs'],
                 gallery_image_version_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 publishing_profile: Optional[pulumi.Input['GalleryImageVersionPublishingProfileArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a GalleryImageVersion resource.
        :param pulumi.Input[str] gallery_image_name: The name of the gallery image definition in which the Image Version is to be created.
        :param pulumi.Input[str] gallery_name: The name of the Shared Image Gallery in which the Image Definition resides.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['GalleryImageVersionStorageProfileArgs'] storage_profile: This is the storage profile of a Gallery Image Version.
        :param pulumi.Input[str] gallery_image_version_name: The name of the gallery image version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['GalleryImageVersionPublishingProfileArgs'] publishing_profile: The publishing profile of a gallery image Version.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "gallery_image_name", gallery_image_name)
        pulumi.set(__self__, "gallery_name", gallery_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_profile", storage_profile)
        if gallery_image_version_name is not None:
            pulumi.set(__self__, "gallery_image_version_name", gallery_image_version_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if publishing_profile is not None:
            pulumi.set(__self__, "publishing_profile", publishing_profile)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="galleryImageName")
    def gallery_image_name(self) -> pulumi.Input[str]:
        """
        The name of the gallery image definition in which the Image Version is to be created.
        """
        return pulumi.get(self, "gallery_image_name")

    @gallery_image_name.setter
    def gallery_image_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "gallery_image_name", value)

    @property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> pulumi.Input[str]:
        """
        The name of the Shared Image Gallery in which the Image Definition resides.
        """
        return pulumi.get(self, "gallery_name")

    @gallery_name.setter
    def gallery_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "gallery_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Input['GalleryImageVersionStorageProfileArgs']:
        """
        This is the storage profile of a Gallery Image Version.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: pulumi.Input['GalleryImageVersionStorageProfileArgs']):
        pulumi.set(self, "storage_profile", value)

    @property
    @pulumi.getter(name="galleryImageVersionName")
    def gallery_image_version_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the gallery image version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
        """
        return pulumi.get(self, "gallery_image_version_name")

    @gallery_image_version_name.setter
    def gallery_image_version_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gallery_image_version_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="publishingProfile")
    def publishing_profile(self) -> Optional[pulumi.Input['GalleryImageVersionPublishingProfileArgs']]:
        """
        The publishing profile of a gallery image Version.
        """
        return pulumi.get(self, "publishing_profile")

    @publishing_profile.setter
    def publishing_profile(self, value: Optional[pulumi.Input['GalleryImageVersionPublishingProfileArgs']]):
        pulumi.set(self, "publishing_profile", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class GalleryImageVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gallery_image_name: Optional[pulumi.Input[str]] = None,
                 gallery_image_version_name: Optional[pulumi.Input[str]] = None,
                 gallery_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 publishing_profile: Optional[pulumi.Input[pulumi.InputType['GalleryImageVersionPublishingProfileArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['GalleryImageVersionStorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Specifies information about the gallery image version that you want to create or update.
        API Version: 2020-09-30.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] gallery_image_name: The name of the gallery image definition in which the Image Version is to be created.
        :param pulumi.Input[str] gallery_image_version_name: The name of the gallery image version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
        :param pulumi.Input[str] gallery_name: The name of the Shared Image Gallery in which the Image Definition resides.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[pulumi.InputType['GalleryImageVersionPublishingProfileArgs']] publishing_profile: The publishing profile of a gallery image Version.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['GalleryImageVersionStorageProfileArgs']] storage_profile: This is the storage profile of a Gallery Image Version.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GalleryImageVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Specifies information about the gallery image version that you want to create or update.
        API Version: 2020-09-30.

        :param str resource_name: The name of the resource.
        :param GalleryImageVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GalleryImageVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gallery_image_name: Optional[pulumi.Input[str]] = None,
                 gallery_image_version_name: Optional[pulumi.Input[str]] = None,
                 gallery_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 publishing_profile: Optional[pulumi.Input[pulumi.InputType['GalleryImageVersionPublishingProfileArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['GalleryImageVersionStorageProfileArgs']]] = None,
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
            __props__ = GalleryImageVersionArgs.__new__(GalleryImageVersionArgs)

            if gallery_image_name is None and not opts.urn:
                raise TypeError("Missing required property 'gallery_image_name'")
            __props__.__dict__["gallery_image_name"] = gallery_image_name
            __props__.__dict__["gallery_image_version_name"] = gallery_image_version_name
            if gallery_name is None and not opts.urn:
                raise TypeError("Missing required property 'gallery_name'")
            __props__.__dict__["gallery_name"] = gallery_name
            __props__.__dict__["location"] = location
            __props__.__dict__["publishing_profile"] = publishing_profile
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_profile is None and not opts.urn:
                raise TypeError("Missing required property 'storage_profile'")
            __props__.__dict__["storage_profile"] = storage_profile
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["replication_status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:compute:GalleryImageVersion"), pulumi.Alias(type_="azure-native:compute/v20180601:GalleryImageVersion"), pulumi.Alias(type_="azure-nextgen:compute/v20180601:GalleryImageVersion"), pulumi.Alias(type_="azure-native:compute/v20190301:GalleryImageVersion"), pulumi.Alias(type_="azure-nextgen:compute/v20190301:GalleryImageVersion"), pulumi.Alias(type_="azure-native:compute/v20190701:GalleryImageVersion"), pulumi.Alias(type_="azure-nextgen:compute/v20190701:GalleryImageVersion"), pulumi.Alias(type_="azure-native:compute/v20191201:GalleryImageVersion"), pulumi.Alias(type_="azure-nextgen:compute/v20191201:GalleryImageVersion"), pulumi.Alias(type_="azure-native:compute/v20200930:GalleryImageVersion"), pulumi.Alias(type_="azure-nextgen:compute/v20200930:GalleryImageVersion")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GalleryImageVersion, __self__).__init__(
            'azure-native:compute:GalleryImageVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GalleryImageVersion':
        """
        Get an existing GalleryImageVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GalleryImageVersionArgs.__new__(GalleryImageVersionArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["publishing_profile"] = None
        __props__.__dict__["replication_status"] = None
        __props__.__dict__["storage_profile"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return GalleryImageVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publishingProfile")
    def publishing_profile(self) -> pulumi.Output[Optional['outputs.GalleryImageVersionPublishingProfileResponse']]:
        """
        The publishing profile of a gallery image Version.
        """
        return pulumi.get(self, "publishing_profile")

    @property
    @pulumi.getter(name="replicationStatus")
    def replication_status(self) -> pulumi.Output['outputs.ReplicationStatusResponse']:
        """
        This is the replication status of the gallery image version.
        """
        return pulumi.get(self, "replication_status")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output['outputs.GalleryImageVersionStorageProfileResponse']:
        """
        This is the storage profile of a Gallery Image Version.
        """
        return pulumi.get(self, "storage_profile")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

