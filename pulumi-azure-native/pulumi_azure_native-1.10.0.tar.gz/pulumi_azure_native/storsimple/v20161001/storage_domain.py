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

__all__ = ['StorageDomainArgs', 'StorageDomain']

@pulumi.input_type
class StorageDomainArgs:
    def __init__(__self__, *,
                 encryption_status: pulumi.Input['EncryptionStatus'],
                 manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_account_credential_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 encryption_key: Optional[pulumi.Input['AsymmetricEncryptedSecretArgs']] = None,
                 storage_domain_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StorageDomain resource.
        :param pulumi.Input['EncryptionStatus'] encryption_status: The encryption status "Enabled | Disabled".
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_account_credential_ids: The storage account credentials.
        :param pulumi.Input['AsymmetricEncryptedSecretArgs'] encryption_key: The encryption key used to encrypt the data. This is a user secret.
        :param pulumi.Input[str] storage_domain_name: The storage domain name.
        """
        pulumi.set(__self__, "encryption_status", encryption_status)
        pulumi.set(__self__, "manager_name", manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_account_credential_ids", storage_account_credential_ids)
        if encryption_key is not None:
            pulumi.set(__self__, "encryption_key", encryption_key)
        if storage_domain_name is not None:
            pulumi.set(__self__, "storage_domain_name", storage_domain_name)

    @property
    @pulumi.getter(name="encryptionStatus")
    def encryption_status(self) -> pulumi.Input['EncryptionStatus']:
        """
        The encryption status "Enabled | Disabled".
        """
        return pulumi.get(self, "encryption_status")

    @encryption_status.setter
    def encryption_status(self, value: pulumi.Input['EncryptionStatus']):
        pulumi.set(self, "encryption_status", value)

    @property
    @pulumi.getter(name="managerName")
    def manager_name(self) -> pulumi.Input[str]:
        """
        The manager name
        """
        return pulumi.get(self, "manager_name")

    @manager_name.setter
    def manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "manager_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccountCredentialIds")
    def storage_account_credential_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The storage account credentials.
        """
        return pulumi.get(self, "storage_account_credential_ids")

    @storage_account_credential_ids.setter
    def storage_account_credential_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "storage_account_credential_ids", value)

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input['AsymmetricEncryptedSecretArgs']]:
        """
        The encryption key used to encrypt the data. This is a user secret.
        """
        return pulumi.get(self, "encryption_key")

    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input['AsymmetricEncryptedSecretArgs']]):
        pulumi.set(self, "encryption_key", value)

    @property
    @pulumi.getter(name="storageDomainName")
    def storage_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The storage domain name.
        """
        return pulumi.get(self, "storage_domain_name")

    @storage_domain_name.setter
    def storage_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_domain_name", value)


class StorageDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption_key: Optional[pulumi.Input[pulumi.InputType['AsymmetricEncryptedSecretArgs']]] = None,
                 encryption_status: Optional[pulumi.Input['EncryptionStatus']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_credential_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_domain_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The storage domain.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AsymmetricEncryptedSecretArgs']] encryption_key: The encryption key used to encrypt the data. This is a user secret.
        :param pulumi.Input['EncryptionStatus'] encryption_status: The encryption status "Enabled | Disabled".
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] storage_account_credential_ids: The storage account credentials.
        :param pulumi.Input[str] storage_domain_name: The storage domain name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The storage domain.

        :param str resource_name: The name of the resource.
        :param StorageDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption_key: Optional[pulumi.Input[pulumi.InputType['AsymmetricEncryptedSecretArgs']]] = None,
                 encryption_status: Optional[pulumi.Input['EncryptionStatus']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_credential_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_domain_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = StorageDomainArgs.__new__(StorageDomainArgs)

            __props__.__dict__["encryption_key"] = encryption_key
            if encryption_status is None and not opts.urn:
                raise TypeError("Missing required property 'encryption_status'")
            __props__.__dict__["encryption_status"] = encryption_status
            if manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'manager_name'")
            __props__.__dict__["manager_name"] = manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_account_credential_ids is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_credential_ids'")
            __props__.__dict__["storage_account_credential_ids"] = storage_account_credential_ids
            __props__.__dict__["storage_domain_name"] = storage_domain_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:storsimple/v20161001:StorageDomain")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StorageDomain, __self__).__init__(
            'azure-native:storsimple/v20161001:StorageDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StorageDomain':
        """
        Get an existing StorageDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StorageDomainArgs.__new__(StorageDomainArgs)

        __props__.__dict__["encryption_key"] = None
        __props__.__dict__["encryption_status"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["storage_account_credential_ids"] = None
        __props__.__dict__["type"] = None
        return StorageDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> pulumi.Output[Optional['outputs.AsymmetricEncryptedSecretResponse']]:
        """
        The encryption key used to encrypt the data. This is a user secret.
        """
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter(name="encryptionStatus")
    def encryption_status(self) -> pulumi.Output[str]:
        """
        The encryption status "Enabled | Disabled".
        """
        return pulumi.get(self, "encryption_status")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageAccountCredentialIds")
    def storage_account_credential_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The storage account credentials.
        """
        return pulumi.get(self, "storage_account_credential_ids")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type.
        """
        return pulumi.get(self, "type")

