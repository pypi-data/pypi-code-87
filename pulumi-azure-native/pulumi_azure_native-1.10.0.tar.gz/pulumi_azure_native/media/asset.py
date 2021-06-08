# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = ['AssetArgs', 'Asset']

@pulumi.input_type
class AssetArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 alternate_id: Optional[pulumi.Input[str]] = None,
                 asset_name: Optional[pulumi.Input[str]] = None,
                 container: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Asset resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[str] alternate_id: The alternate ID of the Asset.
        :param pulumi.Input[str] asset_name: The Asset name.
        :param pulumi.Input[str] container: The name of the asset blob container.
        :param pulumi.Input[str] description: The Asset description.
        :param pulumi.Input[str] storage_account_name: The name of the storage account.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if alternate_id is not None:
            pulumi.set(__self__, "alternate_id", alternate_id)
        if asset_name is not None:
            pulumi.set(__self__, "asset_name", asset_name)
        if container is not None:
            pulumi.set(__self__, "container", container)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if storage_account_name is not None:
            pulumi.set(__self__, "storage_account_name", storage_account_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The Media Services account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="alternateId")
    def alternate_id(self) -> Optional[pulumi.Input[str]]:
        """
        The alternate ID of the Asset.
        """
        return pulumi.get(self, "alternate_id")

    @alternate_id.setter
    def alternate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alternate_id", value)

    @property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Asset name.
        """
        return pulumi.get(self, "asset_name")

    @asset_name.setter
    def asset_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "asset_name", value)

    @property
    @pulumi.getter
    def container(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the asset blob container.
        """
        return pulumi.get(self, "container")

    @container.setter
    def container(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The Asset description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the storage account.
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_name", value)


class Asset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 alternate_id: Optional[pulumi.Input[str]] = None,
                 asset_name: Optional[pulumi.Input[str]] = None,
                 container: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Asset.
        API Version: 2020-05-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[str] alternate_id: The alternate ID of the Asset.
        :param pulumi.Input[str] asset_name: The Asset name.
        :param pulumi.Input[str] container: The name of the asset blob container.
        :param pulumi.Input[str] description: The Asset description.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[str] storage_account_name: The name of the storage account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Asset.
        API Version: 2020-05-01.

        :param str resource_name: The name of the resource.
        :param AssetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 alternate_id: Optional[pulumi.Input[str]] = None,
                 asset_name: Optional[pulumi.Input[str]] = None,
                 container: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = AssetArgs.__new__(AssetArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["alternate_id"] = alternate_id
            __props__.__dict__["asset_name"] = asset_name
            __props__.__dict__["container"] = container
            __props__.__dict__["description"] = description
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["storage_account_name"] = storage_account_name
            __props__.__dict__["asset_id"] = None
            __props__.__dict__["created"] = None
            __props__.__dict__["last_modified"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["storage_encryption_format"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:media:Asset"), pulumi.Alias(type_="azure-native:media/v20180330preview:Asset"), pulumi.Alias(type_="azure-nextgen:media/v20180330preview:Asset"), pulumi.Alias(type_="azure-native:media/v20180601preview:Asset"), pulumi.Alias(type_="azure-nextgen:media/v20180601preview:Asset"), pulumi.Alias(type_="azure-native:media/v20180701:Asset"), pulumi.Alias(type_="azure-nextgen:media/v20180701:Asset"), pulumi.Alias(type_="azure-native:media/v20200501:Asset"), pulumi.Alias(type_="azure-nextgen:media/v20200501:Asset")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Asset, __self__).__init__(
            'azure-native:media:Asset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Asset':
        """
        Get an existing Asset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssetArgs.__new__(AssetArgs)

        __props__.__dict__["alternate_id"] = None
        __props__.__dict__["asset_id"] = None
        __props__.__dict__["container"] = None
        __props__.__dict__["created"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["last_modified"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["storage_account_name"] = None
        __props__.__dict__["storage_encryption_format"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Asset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alternateId")
    def alternate_id(self) -> pulumi.Output[Optional[str]]:
        """
        The alternate ID of the Asset.
        """
        return pulumi.get(self, "alternate_id")

    @property
    @pulumi.getter(name="assetId")
    def asset_id(self) -> pulumi.Output[str]:
        """
        The Asset ID.
        """
        return pulumi.get(self, "asset_id")

    @property
    @pulumi.getter
    def container(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the asset blob container.
        """
        return pulumi.get(self, "container")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        The creation date of the Asset.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The Asset description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        """
        The last modified date of the Asset.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the storage account.
        """
        return pulumi.get(self, "storage_account_name")

    @property
    @pulumi.getter(name="storageEncryptionFormat")
    def storage_encryption_format(self) -> pulumi.Output[str]:
        """
        The Asset encryption format. One of None or MediaStorageEncryption.
        """
        return pulumi.get(self, "storage_encryption_format")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

