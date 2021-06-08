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

__all__ = ['ServerArgs', 'Server']

@pulumi.input_type
class ServerArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input[Union['ServerPropertiesForDefaultCreateArgs', 'ServerPropertiesForGeoRestoreArgs', 'ServerPropertiesForReplicaArgs', 'ServerPropertiesForRestoreArgs']],
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Server resource.
        :param pulumi.Input[Union['ServerPropertiesForDefaultCreateArgs', 'ServerPropertiesForGeoRestoreArgs', 'ServerPropertiesForReplicaArgs', 'ServerPropertiesForRestoreArgs']] properties: Properties of the server.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] location: The location the resource resides in.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input['SkuArgs'] sku: The SKU (pricing tier) of the server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Application-specific metadata in the form of key-value pairs.
        """
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if server_name is not None:
            pulumi.set(__self__, "server_name", server_name)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union['ServerPropertiesForDefaultCreateArgs', 'ServerPropertiesForGeoRestoreArgs', 'ServerPropertiesForReplicaArgs', 'ServerPropertiesForRestoreArgs']]:
        """
        Properties of the server.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input[Union['ServerPropertiesForDefaultCreateArgs', 'ServerPropertiesForGeoRestoreArgs', 'ServerPropertiesForReplicaArgs', 'ServerPropertiesForRestoreArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location the resource resides in.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The SKU (pricing tier) of the server.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Application-specific metadata in the form of key-value pairs.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Server(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ServerPropertiesForDefaultCreateArgs'], pulumi.InputType['ServerPropertiesForGeoRestoreArgs'], pulumi.InputType['ServerPropertiesForReplicaArgs'], pulumi.InputType['ServerPropertiesForRestoreArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents a server.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The location the resource resides in.
        :param pulumi.Input[Union[pulumi.InputType['ServerPropertiesForDefaultCreateArgs'], pulumi.InputType['ServerPropertiesForGeoRestoreArgs'], pulumi.InputType['ServerPropertiesForReplicaArgs'], pulumi.InputType['ServerPropertiesForRestoreArgs']]] properties: Properties of the server.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The SKU (pricing tier) of the server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Application-specific metadata in the form of key-value pairs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a server.

        :param str resource_name: The name of the resource.
        :param ServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ServerPropertiesForDefaultCreateArgs'], pulumi.InputType['ServerPropertiesForGeoRestoreArgs'], pulumi.InputType['ServerPropertiesForReplicaArgs'], pulumi.InputType['ServerPropertiesForRestoreArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
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
            __props__ = ServerArgs.__new__(ServerArgs)

            __props__.__dict__["location"] = location
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["administrator_login"] = None
            __props__.__dict__["earliest_restore_date"] = None
            __props__.__dict__["fully_qualified_domain_name"] = None
            __props__.__dict__["identity"] = None
            __props__.__dict__["master_server_id"] = None
            __props__.__dict__["minimal_tls_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["replica_capacity"] = None
            __props__.__dict__["replication_role"] = None
            __props__.__dict__["ssl_enforcement"] = None
            __props__.__dict__["storage_profile"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["user_visible_state"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:dbformariadb/v20180601preview:Server"), pulumi.Alias(type_="azure-native:dbformariadb:Server"), pulumi.Alias(type_="azure-nextgen:dbformariadb:Server"), pulumi.Alias(type_="azure-native:dbformariadb/v20180601:Server"), pulumi.Alias(type_="azure-nextgen:dbformariadb/v20180601:Server")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Server, __self__).__init__(
            'azure-native:dbformariadb/v20180601preview:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Server':
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerArgs.__new__(ServerArgs)

        __props__.__dict__["administrator_login"] = None
        __props__.__dict__["earliest_restore_date"] = None
        __props__.__dict__["fully_qualified_domain_name"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["master_server_id"] = None
        __props__.__dict__["minimal_tls_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["replica_capacity"] = None
        __props__.__dict__["replication_role"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["ssl_enforcement"] = None
        __props__.__dict__["storage_profile"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_visible_state"] = None
        __props__.__dict__["version"] = None
        return Server(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Output[Optional[str]]:
        """
        The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="earliestRestoreDate")
    def earliest_restore_date(self) -> pulumi.Output[Optional[str]]:
        """
        Earliest restore point creation time (ISO8601 format)
        """
        return pulumi.get(self, "earliest_restore_date")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        The fully qualified domain name of a server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ResourceIdentityResponse']]:
        """
        The Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="masterServerId")
    def master_server_id(self) -> pulumi.Output[Optional[str]]:
        """
        The master server id of a replica server.
        """
        return pulumi.get(self, "master_server_id")

    @property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> pulumi.Output[Optional[str]]:
        """
        Enforce a minimal Tls version for the server.
        """
        return pulumi.get(self, "minimal_tls_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="replicaCapacity")
    def replica_capacity(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum number of replicas that a master server can have.
        """
        return pulumi.get(self, "replica_capacity")

    @property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> pulumi.Output[Optional[str]]:
        """
        The replication role of the server.
        """
        return pulumi.get(self, "replication_role")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The SKU (pricing tier) of the server.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> pulumi.Output[Optional[str]]:
        """
        Enable ssl enforcement or not when connect to server.
        """
        return pulumi.get(self, "ssl_enforcement")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional['outputs.StorageProfileResponse']]:
        """
        Storage profile of a server.
        """
        return pulumi.get(self, "storage_profile")

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
    @pulumi.getter(name="userVisibleState")
    def user_visible_state(self) -> pulumi.Output[Optional[str]]:
        """
        A state of a server that is visible to user.
        """
        return pulumi.get(self, "user_visible_state")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Server version.
        """
        return pulumi.get(self, "version")

