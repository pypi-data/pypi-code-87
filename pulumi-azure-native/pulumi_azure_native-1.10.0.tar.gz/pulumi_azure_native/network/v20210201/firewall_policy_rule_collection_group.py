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

__all__ = ['FirewallPolicyRuleCollectionGroupArgs', 'FirewallPolicyRuleCollectionGroup']

@pulumi.input_type
class FirewallPolicyRuleCollectionGroupArgs:
    def __init__(__self__, *,
                 firewall_policy_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rule_collection_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[Union['FirewallPolicyFilterRuleCollectionArgs', 'FirewallPolicyNatRuleCollectionArgs']]]]] = None):
        """
        The set of arguments for constructing a FirewallPolicyRuleCollectionGroup resource.
        :param pulumi.Input[str] firewall_policy_name: The name of the Firewall Policy.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[int] priority: Priority of the Firewall Policy Rule Collection Group resource.
        :param pulumi.Input[str] rule_collection_group_name: The name of the FirewallPolicyRuleCollectionGroup.
        :param pulumi.Input[Sequence[pulumi.Input[Union['FirewallPolicyFilterRuleCollectionArgs', 'FirewallPolicyNatRuleCollectionArgs']]]] rule_collections: Group of Firewall Policy rule collections.
        """
        pulumi.set(__self__, "firewall_policy_name", firewall_policy_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if rule_collection_group_name is not None:
            pulumi.set(__self__, "rule_collection_group_name", rule_collection_group_name)
        if rule_collections is not None:
            pulumi.set(__self__, "rule_collections", rule_collections)

    @property
    @pulumi.getter(name="firewallPolicyName")
    def firewall_policy_name(self) -> pulumi.Input[str]:
        """
        The name of the Firewall Policy.
        """
        return pulumi.get(self, "firewall_policy_name")

    @firewall_policy_name.setter
    def firewall_policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "firewall_policy_name", value)

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
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority of the Firewall Policy Rule Collection Group resource.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="ruleCollectionGroupName")
    def rule_collection_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the FirewallPolicyRuleCollectionGroup.
        """
        return pulumi.get(self, "rule_collection_group_name")

    @rule_collection_group_name.setter
    def rule_collection_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_collection_group_name", value)

    @property
    @pulumi.getter(name="ruleCollections")
    def rule_collections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union['FirewallPolicyFilterRuleCollectionArgs', 'FirewallPolicyNatRuleCollectionArgs']]]]]:
        """
        Group of Firewall Policy rule collections.
        """
        return pulumi.get(self, "rule_collections")

    @rule_collections.setter
    def rule_collections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union['FirewallPolicyFilterRuleCollectionArgs', 'FirewallPolicyNatRuleCollectionArgs']]]]]):
        pulumi.set(self, "rule_collections", value)


class FirewallPolicyRuleCollectionGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 firewall_policy_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collection_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['FirewallPolicyFilterRuleCollectionArgs'], pulumi.InputType['FirewallPolicyNatRuleCollectionArgs']]]]]] = None,
                 __props__=None):
        """
        Rule Collection Group resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] firewall_policy_name: The name of the Firewall Policy.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[int] priority: Priority of the Firewall Policy Rule Collection Group resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] rule_collection_group_name: The name of the FirewallPolicyRuleCollectionGroup.
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['FirewallPolicyFilterRuleCollectionArgs'], pulumi.InputType['FirewallPolicyNatRuleCollectionArgs']]]]] rule_collections: Group of Firewall Policy rule collections.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallPolicyRuleCollectionGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Rule Collection Group resource.

        :param str resource_name: The name of the resource.
        :param FirewallPolicyRuleCollectionGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallPolicyRuleCollectionGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 firewall_policy_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collection_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['FirewallPolicyFilterRuleCollectionArgs'], pulumi.InputType['FirewallPolicyNatRuleCollectionArgs']]]]]] = None,
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
            __props__ = FirewallPolicyRuleCollectionGroupArgs.__new__(FirewallPolicyRuleCollectionGroupArgs)

            if firewall_policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'firewall_policy_name'")
            __props__.__dict__["firewall_policy_name"] = firewall_policy_name
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rule_collection_group_name"] = rule_collection_group_name
            __props__.__dict__["rule_collections"] = rule_collections
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20210201:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-native:network:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-nextgen:network:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-native:network/v20200501:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-nextgen:network/v20200501:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-native:network/v20200601:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-nextgen:network/v20200601:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-native:network/v20200701:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-nextgen:network/v20200701:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-native:network/v20200801:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-nextgen:network/v20200801:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-native:network/v20201101:FirewallPolicyRuleCollectionGroup"), pulumi.Alias(type_="azure-nextgen:network/v20201101:FirewallPolicyRuleCollectionGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FirewallPolicyRuleCollectionGroup, __self__).__init__(
            'azure-native:network/v20210201:FirewallPolicyRuleCollectionGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FirewallPolicyRuleCollectionGroup':
        """
        Get an existing FirewallPolicyRuleCollectionGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FirewallPolicyRuleCollectionGroupArgs.__new__(FirewallPolicyRuleCollectionGroupArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rule_collections"] = None
        __props__.__dict__["type"] = None
        return FirewallPolicyRuleCollectionGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Priority of the Firewall Policy Rule Collection Group resource.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the firewall policy rule collection group resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ruleCollections")
    def rule_collections(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        Group of Firewall Policy rule collections.
        """
        return pulumi.get(self, "rule_collections")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Rule Group type.
        """
        return pulumi.get(self, "type")

