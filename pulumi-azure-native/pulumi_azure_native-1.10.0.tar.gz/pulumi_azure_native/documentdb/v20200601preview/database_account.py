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

__all__ = ['DatabaseAccountArgs', 'DatabaseAccount']

@pulumi.input_type
class DatabaseAccountArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input[Union['DefaultRequestDatabaseAccountCreateUpdatePropertiesArgs', 'RestoreReqeustDatabaseAccountCreateUpdatePropertiesArgs']],
                 resource_group_name: pulumi.Input[str],
                 account_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 kind: Optional[pulumi.Input[Union[str, 'DatabaseAccountKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DatabaseAccount resource.
        :param pulumi.Input[Union['DefaultRequestDatabaseAccountCreateUpdatePropertiesArgs', 'RestoreReqeustDatabaseAccountCreateUpdatePropertiesArgs']] properties: Properties to create and update Azure Cosmos DB database accounts.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: Identity for the resource.
        :param pulumi.Input[Union[str, 'DatabaseAccountKind']] kind: Indicates the type of database account. This can only be set at database account creation.
        :param pulumi.Input[str] location: The location of the resource group to which the resource belongs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if kind is None:
            kind = 'GlobalDocumentDB'
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union['DefaultRequestDatabaseAccountCreateUpdatePropertiesArgs', 'RestoreReqeustDatabaseAccountCreateUpdatePropertiesArgs']]:
        """
        Properties to create and update Azure Cosmos DB database accounts.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input[Union['DefaultRequestDatabaseAccountCreateUpdatePropertiesArgs', 'RestoreReqeustDatabaseAccountCreateUpdatePropertiesArgs']]):
        pulumi.set(self, "properties", value)

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
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Cosmos DB database account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'DatabaseAccountKind']]]:
        """
        Indicates the type of database account. This can only be set at database account creation.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'DatabaseAccountKind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class DatabaseAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'DatabaseAccountKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['DefaultRequestDatabaseAccountCreateUpdatePropertiesArgs'], pulumi.InputType['RestoreReqeustDatabaseAccountCreateUpdatePropertiesArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        An Azure Cosmos DB database account.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']] identity: Identity for the resource.
        :param pulumi.Input[Union[str, 'DatabaseAccountKind']] kind: Indicates the type of database account. This can only be set at database account creation.
        :param pulumi.Input[str] location: The location of the resource group to which the resource belongs.
        :param pulumi.Input[Union[pulumi.InputType['DefaultRequestDatabaseAccountCreateUpdatePropertiesArgs'], pulumi.InputType['RestoreReqeustDatabaseAccountCreateUpdatePropertiesArgs']]] properties: Properties to create and update Azure Cosmos DB database accounts.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure Cosmos DB database account.

        :param str resource_name: The name of the resource.
        :param DatabaseAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'DatabaseAccountKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['DefaultRequestDatabaseAccountCreateUpdatePropertiesArgs'], pulumi.InputType['RestoreReqeustDatabaseAccountCreateUpdatePropertiesArgs']]]] = None,
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
            __props__ = DatabaseAccountArgs.__new__(DatabaseAccountArgs)

            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["identity"] = identity
            if kind is None:
                kind = 'GlobalDocumentDB'
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["api_properties"] = None
            __props__.__dict__["backup_policy"] = None
            __props__.__dict__["capabilities"] = None
            __props__.__dict__["connector_offer"] = None
            __props__.__dict__["consistency_policy"] = None
            __props__.__dict__["cors"] = None
            __props__.__dict__["create_mode"] = None
            __props__.__dict__["database_account_offer_type"] = None
            __props__.__dict__["disable_key_based_metadata_write_access"] = None
            __props__.__dict__["document_endpoint"] = None
            __props__.__dict__["enable_analytical_storage"] = None
            __props__.__dict__["enable_automatic_failover"] = None
            __props__.__dict__["enable_cassandra_connector"] = None
            __props__.__dict__["enable_free_tier"] = None
            __props__.__dict__["enable_multiple_write_locations"] = None
            __props__.__dict__["failover_policies"] = None
            __props__.__dict__["instance_id"] = None
            __props__.__dict__["ip_rules"] = None
            __props__.__dict__["is_virtual_network_filter_enabled"] = None
            __props__.__dict__["key_vault_key_uri"] = None
            __props__.__dict__["locations"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["public_network_access"] = None
            __props__.__dict__["read_locations"] = None
            __props__.__dict__["restore_parameters"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["virtual_network_rules"] = None
            __props__.__dict__["write_locations"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:documentdb/v20200601preview:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20150401:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20150401:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20150408:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20150408:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20151106:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20151106:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20160319:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20160319:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20160331:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20160331:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20190801:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20190801:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20191212:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20191212:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20200301:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20200301:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20200401:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20200401:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20200901:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20200901:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20210115:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210115:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20210301preview:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210301preview:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20210315:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210315:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20210401preview:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210401preview:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20210415:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210415:DatabaseAccount"), pulumi.Alias(type_="azure-native:documentdb/v20210515:DatabaseAccount"), pulumi.Alias(type_="azure-nextgen:documentdb/v20210515:DatabaseAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DatabaseAccount, __self__).__init__(
            'azure-native:documentdb/v20200601preview:DatabaseAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DatabaseAccount':
        """
        Get an existing DatabaseAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatabaseAccountArgs.__new__(DatabaseAccountArgs)

        __props__.__dict__["api_properties"] = None
        __props__.__dict__["backup_policy"] = None
        __props__.__dict__["capabilities"] = None
        __props__.__dict__["connector_offer"] = None
        __props__.__dict__["consistency_policy"] = None
        __props__.__dict__["cors"] = None
        __props__.__dict__["create_mode"] = None
        __props__.__dict__["database_account_offer_type"] = None
        __props__.__dict__["disable_key_based_metadata_write_access"] = None
        __props__.__dict__["document_endpoint"] = None
        __props__.__dict__["enable_analytical_storage"] = None
        __props__.__dict__["enable_automatic_failover"] = None
        __props__.__dict__["enable_cassandra_connector"] = None
        __props__.__dict__["enable_free_tier"] = None
        __props__.__dict__["enable_multiple_write_locations"] = None
        __props__.__dict__["failover_policies"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["instance_id"] = None
        __props__.__dict__["ip_rules"] = None
        __props__.__dict__["is_virtual_network_filter_enabled"] = None
        __props__.__dict__["key_vault_key_uri"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["locations"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["read_locations"] = None
        __props__.__dict__["restore_parameters"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_network_rules"] = None
        __props__.__dict__["write_locations"] = None
        return DatabaseAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiProperties")
    def api_properties(self) -> pulumi.Output[Optional['outputs.ApiPropertiesResponse']]:
        """
        API specific properties.
        """
        return pulumi.get(self, "api_properties")

    @property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> pulumi.Output[Optional[Any]]:
        """
        The object representing the policy for taking backups on an account.
        """
        return pulumi.get(self, "backup_policy")

    @property
    @pulumi.getter
    def capabilities(self) -> pulumi.Output[Optional[Sequence['outputs.CapabilityResponse']]]:
        """
        List of Cosmos DB capabilities for the account
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter(name="connectorOffer")
    def connector_offer(self) -> pulumi.Output[Optional[str]]:
        """
        The cassandra connector offer type for the Cosmos DB database C* account.
        """
        return pulumi.get(self, "connector_offer")

    @property
    @pulumi.getter(name="consistencyPolicy")
    def consistency_policy(self) -> pulumi.Output[Optional['outputs.ConsistencyPolicyResponse']]:
        """
        The consistency policy for the Cosmos DB database account.
        """
        return pulumi.get(self, "consistency_policy")

    @property
    @pulumi.getter
    def cors(self) -> pulumi.Output[Optional[Sequence['outputs.CorsPolicyResponse']]]:
        """
        The CORS policy for the Cosmos DB database account.
        """
        return pulumi.get(self, "cors")

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Enum to indicate the mode of account creation.
        """
        return pulumi.get(self, "create_mode")

    @property
    @pulumi.getter(name="databaseAccountOfferType")
    def database_account_offer_type(self) -> pulumi.Output[str]:
        """
        The offer type for the Cosmos DB database account. Default value: Standard.
        """
        return pulumi.get(self, "database_account_offer_type")

    @property
    @pulumi.getter(name="disableKeyBasedMetadataWriteAccess")
    def disable_key_based_metadata_write_access(self) -> pulumi.Output[Optional[bool]]:
        """
        Disable write operations on metadata resources (databases, containers, throughput) via account keys
        """
        return pulumi.get(self, "disable_key_based_metadata_write_access")

    @property
    @pulumi.getter(name="documentEndpoint")
    def document_endpoint(self) -> pulumi.Output[str]:
        """
        The connection endpoint for the Cosmos DB database account.
        """
        return pulumi.get(self, "document_endpoint")

    @property
    @pulumi.getter(name="enableAnalyticalStorage")
    def enable_analytical_storage(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag to indicate whether to enable storage analytics.
        """
        return pulumi.get(self, "enable_analytical_storage")

    @property
    @pulumi.getter(name="enableAutomaticFailover")
    def enable_automatic_failover(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.
        """
        return pulumi.get(self, "enable_automatic_failover")

    @property
    @pulumi.getter(name="enableCassandraConnector")
    def enable_cassandra_connector(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables the cassandra connector on the Cosmos DB C* account
        """
        return pulumi.get(self, "enable_cassandra_connector")

    @property
    @pulumi.getter(name="enableFreeTier")
    def enable_free_tier(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag to indicate whether Free Tier is enabled.
        """
        return pulumi.get(self, "enable_free_tier")

    @property
    @pulumi.getter(name="enableMultipleWriteLocations")
    def enable_multiple_write_locations(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables the account to write in multiple locations
        """
        return pulumi.get(self, "enable_multiple_write_locations")

    @property
    @pulumi.getter(name="failoverPolicies")
    def failover_policies(self) -> pulumi.Output[Sequence['outputs.FailoverPolicyResponse']]:
        """
        An array that contains the regions ordered by their failover priorities.
        """
        return pulumi.get(self, "failover_policies")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        A unique identifier assigned to the database account
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> pulumi.Output[Optional[Sequence['outputs.IpAddressOrRangeResponse']]]:
        """
        List of IpRules.
        """
        return pulumi.get(self, "ip_rules")

    @property
    @pulumi.getter(name="isVirtualNetworkFilterEnabled")
    def is_virtual_network_filter_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag to indicate whether to enable/disable Virtual Network ACL rules.
        """
        return pulumi.get(self, "is_virtual_network_filter_enabled")

    @property
    @pulumi.getter(name="keyVaultKeyUri")
    def key_vault_key_uri(self) -> pulumi.Output[Optional[str]]:
        """
        The URI of the key vault
        """
        return pulumi.get(self, "key_vault_key_uri")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates the type of database account. This can only be set at database account creation.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def locations(self) -> pulumi.Output[Sequence['outputs.LocationResponse']]:
        """
        An array that contains all of the locations enabled for the Cosmos DB account.
        """
        return pulumi.get(self, "locations")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the ARM resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        List of Private Endpoint Connections configured for the Cosmos DB account.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the Cosmos DB account at the time the operation was called. The status can be one of following. 'Creating' – the Cosmos DB account is being created. When an account is in Creating state, only properties that are specified as input for the Create Cosmos DB account operation are returned. 'Succeeded' – the Cosmos DB account is active for use. 'Updating' – the Cosmos DB account is being updated. 'Deleting' – the Cosmos DB account is being deleted. 'Failed' – the Cosmos DB account failed creation. 'DeletionFailed' – the Cosmos DB account deletion failed.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[str]:
        """
        Whether requests from Public Network are allowed
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="readLocations")
    def read_locations(self) -> pulumi.Output[Sequence['outputs.LocationResponse']]:
        """
        An array that contains of the read locations enabled for the Cosmos DB account.
        """
        return pulumi.get(self, "read_locations")

    @property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> pulumi.Output[Optional['outputs.RestoreParametersResponse']]:
        """
        Parameters to indicate the information about the restore.
        """
        return pulumi.get(self, "restore_parameters")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> pulumi.Output[Optional[Sequence['outputs.VirtualNetworkRuleResponse']]]:
        """
        List of Virtual Network ACL rules configured for the Cosmos DB account.
        """
        return pulumi.get(self, "virtual_network_rules")

    @property
    @pulumi.getter(name="writeLocations")
    def write_locations(self) -> pulumi.Output[Sequence['outputs.LocationResponse']]:
        """
        An array that contains the write location for the Cosmos DB account.
        """
        return pulumi.get(self, "write_locations")

