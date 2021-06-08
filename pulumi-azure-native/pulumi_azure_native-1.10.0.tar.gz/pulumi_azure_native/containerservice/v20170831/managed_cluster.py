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

__all__ = ['ManagedClusterArgs', 'ManagedCluster']

@pulumi.input_type
class ManagedClusterArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 agent_pool_profiles: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerServiceAgentPoolProfileArgs']]]] = None,
                 dns_prefix: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 linux_profile: Optional[pulumi.Input['ContainerServiceLinuxProfileArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 service_principal_profile: Optional[pulumi.Input['ContainerServiceServicePrincipalProfileArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ManagedCluster resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input['ContainerServiceAgentPoolProfileArgs']]] agent_pool_profiles: Properties of the agent pool.
        :param pulumi.Input[str] dns_prefix: DNS prefix specified when creating the managed cluster.
        :param pulumi.Input[str] kubernetes_version: Version of Kubernetes specified when creating the managed cluster.
        :param pulumi.Input['ContainerServiceLinuxProfileArgs'] linux_profile: Profile for Linux VMs in the container service cluster.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_name: The name of the managed cluster resource.
        :param pulumi.Input['ContainerServiceServicePrincipalProfileArgs'] service_principal_profile: Information about a service principal identity for the cluster to use for manipulating Azure APIs. Either secret or keyVaultSecretRef must be specified.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if agent_pool_profiles is not None:
            pulumi.set(__self__, "agent_pool_profiles", agent_pool_profiles)
        if dns_prefix is not None:
            pulumi.set(__self__, "dns_prefix", dns_prefix)
        if kubernetes_version is not None:
            pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if linux_profile is not None:
            pulumi.set(__self__, "linux_profile", linux_profile)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if service_principal_profile is not None:
            pulumi.set(__self__, "service_principal_profile", service_principal_profile)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerServiceAgentPoolProfileArgs']]]]:
        """
        Properties of the agent pool.
        """
        return pulumi.get(self, "agent_pool_profiles")

    @agent_pool_profiles.setter
    def agent_pool_profiles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerServiceAgentPoolProfileArgs']]]]):
        pulumi.set(self, "agent_pool_profiles", value)

    @property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        DNS prefix specified when creating the managed cluster.
        """
        return pulumi.get(self, "dns_prefix")

    @dns_prefix.setter
    def dns_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_prefix", value)

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[pulumi.Input[str]]:
        """
        Version of Kubernetes specified when creating the managed cluster.
        """
        return pulumi.get(self, "kubernetes_version")

    @kubernetes_version.setter
    def kubernetes_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_version", value)

    @property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> Optional[pulumi.Input['ContainerServiceLinuxProfileArgs']]:
        """
        Profile for Linux VMs in the container service cluster.
        """
        return pulumi.get(self, "linux_profile")

    @linux_profile.setter
    def linux_profile(self, value: Optional[pulumi.Input['ContainerServiceLinuxProfileArgs']]):
        pulumi.set(self, "linux_profile", value)

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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the managed cluster resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="servicePrincipalProfile")
    def service_principal_profile(self) -> Optional[pulumi.Input['ContainerServiceServicePrincipalProfileArgs']]:
        """
        Information about a service principal identity for the cluster to use for manipulating Azure APIs. Either secret or keyVaultSecretRef must be specified.
        """
        return pulumi.get(self, "service_principal_profile")

    @service_principal_profile.setter
    def service_principal_profile(self, value: Optional[pulumi.Input['ContainerServiceServicePrincipalProfileArgs']]):
        pulumi.set(self, "service_principal_profile", value)

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


class ManagedCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_pool_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerServiceAgentPoolProfileArgs']]]]] = None,
                 dns_prefix: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 linux_profile: Optional[pulumi.Input[pulumi.InputType['ContainerServiceLinuxProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 service_principal_profile: Optional[pulumi.Input[pulumi.InputType['ContainerServiceServicePrincipalProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Managed cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerServiceAgentPoolProfileArgs']]]] agent_pool_profiles: Properties of the agent pool.
        :param pulumi.Input[str] dns_prefix: DNS prefix specified when creating the managed cluster.
        :param pulumi.Input[str] kubernetes_version: Version of Kubernetes specified when creating the managed cluster.
        :param pulumi.Input[pulumi.InputType['ContainerServiceLinuxProfileArgs']] linux_profile: Profile for Linux VMs in the container service cluster.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_name_: The name of the managed cluster resource.
        :param pulumi.Input[pulumi.InputType['ContainerServiceServicePrincipalProfileArgs']] service_principal_profile: Information about a service principal identity for the cluster to use for manipulating Azure APIs. Either secret or keyVaultSecretRef must be specified.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Managed cluster.

        :param str resource_name: The name of the resource.
        :param ManagedClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_pool_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerServiceAgentPoolProfileArgs']]]]] = None,
                 dns_prefix: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 linux_profile: Optional[pulumi.Input[pulumi.InputType['ContainerServiceLinuxProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 service_principal_profile: Optional[pulumi.Input[pulumi.InputType['ContainerServiceServicePrincipalProfileArgs']]] = None,
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
            __props__ = ManagedClusterArgs.__new__(ManagedClusterArgs)

            __props__.__dict__["agent_pool_profiles"] = agent_pool_profiles
            __props__.__dict__["dns_prefix"] = dns_prefix
            __props__.__dict__["kubernetes_version"] = kubernetes_version
            __props__.__dict__["linux_profile"] = linux_profile
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["service_principal_profile"] = service_principal_profile
            __props__.__dict__["tags"] = tags
            __props__.__dict__["fqdn"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:containerservice/v20170831:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20180331:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20180331:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20180801preview:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20180801preview:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20190201:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20190201:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20190401:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20190401:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20190601:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20190601:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20190801:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20190801:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20191001:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20191001:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20191101:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20191101:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200101:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20200101:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200201:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20200201:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200301:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20200301:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200401:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20200401:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200601:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20200601:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200701:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20200701:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20200901:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20200901:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20201101:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20201101:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20201201:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20201201:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20210201:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20210201:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20210301:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20210301:ManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20210501:ManagedCluster"), pulumi.Alias(type_="azure-nextgen:containerservice/v20210501:ManagedCluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedCluster, __self__).__init__(
            'azure-native:containerservice/v20170831:ManagedCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedCluster':
        """
        Get an existing ManagedCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedClusterArgs.__new__(ManagedClusterArgs)

        __props__.__dict__["agent_pool_profiles"] = None
        __props__.__dict__["dns_prefix"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["kubernetes_version"] = None
        __props__.__dict__["linux_profile"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_principal_profile"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ManagedCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(self) -> pulumi.Output[Optional[Sequence['outputs.ContainerServiceAgentPoolProfileResponse']]]:
        """
        Properties of the agent pool.
        """
        return pulumi.get(self, "agent_pool_profiles")

    @property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        DNS prefix specified when creating the managed cluster.
        """
        return pulumi.get(self, "dns_prefix")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        FQDN for the master pool.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[Optional[str]]:
        """
        Version of Kubernetes specified when creating the managed cluster.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter(name="linuxProfile")
    def linux_profile(self) -> pulumi.Output[Optional['outputs.ContainerServiceLinuxProfileResponse']]:
        """
        Profile for Linux VMs in the container service cluster.
        """
        return pulumi.get(self, "linux_profile")

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
        The current deployment or provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="servicePrincipalProfile")
    def service_principal_profile(self) -> pulumi.Output[Optional['outputs.ContainerServiceServicePrincipalProfileResponse']]:
        """
        Information about a service principal identity for the cluster to use for manipulating Azure APIs. Either secret or keyVaultSecretRef must be specified.
        """
        return pulumi.get(self, "service_principal_profile")

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

