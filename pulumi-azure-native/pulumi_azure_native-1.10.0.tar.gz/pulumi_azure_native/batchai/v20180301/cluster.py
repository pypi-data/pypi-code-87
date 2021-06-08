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

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 user_account_settings: pulumi.Input['UserAccountSettingsArgs'],
                 vm_size: pulumi.Input[str],
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 node_setup: Optional[pulumi.Input['NodeSetupArgs']] = None,
                 scale_settings: Optional[pulumi.Input['ScaleSettingsArgs']] = None,
                 subnet: Optional[pulumi.Input['ResourceIdArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_machine_configuration: Optional[pulumi.Input['VirtualMachineConfigurationArgs']] = None,
                 vm_priority: Optional[pulumi.Input['VmPriority']] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input['UserAccountSettingsArgs'] user_account_settings: Settings for user account that gets created on each on the nodes of a cluster.
        :param pulumi.Input[str] vm_size: All virtual machines in a cluster are the same size. For information about available VM sizes for clusters using images from the Virtual Machines Marketplace (see Sizes for Virtual Machines (Linux) or Sizes for Virtual Machines (Windows). Batch AI service supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).
        :param pulumi.Input[str] cluster_name: The name of the cluster within the specified resource group. Cluster names can only contain a combination of alphanumeric characters along with dash (-) and underscore (_). The name must be from 1 through 64 characters long.
        :param pulumi.Input[str] location: The region in which to create the cluster.
        :param pulumi.Input['NodeSetupArgs'] node_setup: Use this to prepare the VM. NOTE: The volumes specified in mountVolumes are mounted first and then the setupTask is run. Therefore the setup task can use local mountPaths in its execution.
        :param pulumi.Input['ScaleSettingsArgs'] scale_settings: At least one of manual or autoScale settings must be specified. Only one of manual or autoScale settings can be specified. If autoScale settings are specified, the system automatically scales the cluster up and down (within the supplied limits) based on the pending jobs on the cluster.
        :param pulumi.Input['ResourceIdArgs'] subnet: Represents a resource ID. For example, for a subnet, it is the resource URL for the subnet.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The user specified tags associated with the Cluster.
        :param pulumi.Input['VirtualMachineConfigurationArgs'] virtual_machine_configuration: Settings for OS image.
        :param pulumi.Input['VmPriority'] vm_priority: Default is dedicated.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "user_account_settings", user_account_settings)
        pulumi.set(__self__, "vm_size", vm_size)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if node_setup is not None:
            pulumi.set(__self__, "node_setup", node_setup)
        if scale_settings is not None:
            pulumi.set(__self__, "scale_settings", scale_settings)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_machine_configuration is not None:
            pulumi.set(__self__, "virtual_machine_configuration", virtual_machine_configuration)
        if vm_priority is None:
            vm_priority = 'dedicated'
        if vm_priority is not None:
            pulumi.set(__self__, "vm_priority", vm_priority)

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
    @pulumi.getter(name="userAccountSettings")
    def user_account_settings(self) -> pulumi.Input['UserAccountSettingsArgs']:
        """
        Settings for user account that gets created on each on the nodes of a cluster.
        """
        return pulumi.get(self, "user_account_settings")

    @user_account_settings.setter
    def user_account_settings(self, value: pulumi.Input['UserAccountSettingsArgs']):
        pulumi.set(self, "user_account_settings", value)

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> pulumi.Input[str]:
        """
        All virtual machines in a cluster are the same size. For information about available VM sizes for clusters using images from the Virtual Machines Marketplace (see Sizes for Virtual Machines (Linux) or Sizes for Virtual Machines (Windows). Batch AI service supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).
        """
        return pulumi.get(self, "vm_size")

    @vm_size.setter
    def vm_size(self, value: pulumi.Input[str]):
        pulumi.set(self, "vm_size", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the cluster within the specified resource group. Cluster names can only contain a combination of alphanumeric characters along with dash (-) and underscore (_). The name must be from 1 through 64 characters long.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to create the cluster.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="nodeSetup")
    def node_setup(self) -> Optional[pulumi.Input['NodeSetupArgs']]:
        """
        Use this to prepare the VM. NOTE: The volumes specified in mountVolumes are mounted first and then the setupTask is run. Therefore the setup task can use local mountPaths in its execution.
        """
        return pulumi.get(self, "node_setup")

    @node_setup.setter
    def node_setup(self, value: Optional[pulumi.Input['NodeSetupArgs']]):
        pulumi.set(self, "node_setup", value)

    @property
    @pulumi.getter(name="scaleSettings")
    def scale_settings(self) -> Optional[pulumi.Input['ScaleSettingsArgs']]:
        """
        At least one of manual or autoScale settings must be specified. Only one of manual or autoScale settings can be specified. If autoScale settings are specified, the system automatically scales the cluster up and down (within the supplied limits) based on the pending jobs on the cluster.
        """
        return pulumi.get(self, "scale_settings")

    @scale_settings.setter
    def scale_settings(self, value: Optional[pulumi.Input['ScaleSettingsArgs']]):
        pulumi.set(self, "scale_settings", value)

    @property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input['ResourceIdArgs']]:
        """
        Represents a resource ID. For example, for a subnet, it is the resource URL for the subnet.
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input['ResourceIdArgs']]):
        pulumi.set(self, "subnet", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The user specified tags associated with the Cluster.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="virtualMachineConfiguration")
    def virtual_machine_configuration(self) -> Optional[pulumi.Input['VirtualMachineConfigurationArgs']]:
        """
        Settings for OS image.
        """
        return pulumi.get(self, "virtual_machine_configuration")

    @virtual_machine_configuration.setter
    def virtual_machine_configuration(self, value: Optional[pulumi.Input['VirtualMachineConfigurationArgs']]):
        pulumi.set(self, "virtual_machine_configuration", value)

    @property
    @pulumi.getter(name="vmPriority")
    def vm_priority(self) -> Optional[pulumi.Input['VmPriority']]:
        """
        Default is dedicated.
        """
        return pulumi.get(self, "vm_priority")

    @vm_priority.setter
    def vm_priority(self, value: Optional[pulumi.Input['VmPriority']]):
        pulumi.set(self, "vm_priority", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 node_setup: Optional[pulumi.Input[pulumi.InputType['NodeSetupArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scale_settings: Optional[pulumi.Input[pulumi.InputType['ScaleSettingsArgs']]] = None,
                 subnet: Optional[pulumi.Input[pulumi.InputType['ResourceIdArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_account_settings: Optional[pulumi.Input[pulumi.InputType['UserAccountSettingsArgs']]] = None,
                 virtual_machine_configuration: Optional[pulumi.Input[pulumi.InputType['VirtualMachineConfigurationArgs']]] = None,
                 vm_priority: Optional[pulumi.Input['VmPriority']] = None,
                 vm_size: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Contains information about a Cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster within the specified resource group. Cluster names can only contain a combination of alphanumeric characters along with dash (-) and underscore (_). The name must be from 1 through 64 characters long.
        :param pulumi.Input[str] location: The region in which to create the cluster.
        :param pulumi.Input[pulumi.InputType['NodeSetupArgs']] node_setup: Use this to prepare the VM. NOTE: The volumes specified in mountVolumes are mounted first and then the setupTask is run. Therefore the setup task can use local mountPaths in its execution.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[pulumi.InputType['ScaleSettingsArgs']] scale_settings: At least one of manual or autoScale settings must be specified. Only one of manual or autoScale settings can be specified. If autoScale settings are specified, the system automatically scales the cluster up and down (within the supplied limits) based on the pending jobs on the cluster.
        :param pulumi.Input[pulumi.InputType['ResourceIdArgs']] subnet: Represents a resource ID. For example, for a subnet, it is the resource URL for the subnet.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The user specified tags associated with the Cluster.
        :param pulumi.Input[pulumi.InputType['UserAccountSettingsArgs']] user_account_settings: Settings for user account that gets created on each on the nodes of a cluster.
        :param pulumi.Input[pulumi.InputType['VirtualMachineConfigurationArgs']] virtual_machine_configuration: Settings for OS image.
        :param pulumi.Input['VmPriority'] vm_priority: Default is dedicated.
        :param pulumi.Input[str] vm_size: All virtual machines in a cluster are the same size. For information about available VM sizes for clusters using images from the Virtual Machines Marketplace (see Sizes for Virtual Machines (Linux) or Sizes for Virtual Machines (Windows). Batch AI service supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contains information about a Cluster.

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 node_setup: Optional[pulumi.Input[pulumi.InputType['NodeSetupArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scale_settings: Optional[pulumi.Input[pulumi.InputType['ScaleSettingsArgs']]] = None,
                 subnet: Optional[pulumi.Input[pulumi.InputType['ResourceIdArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_account_settings: Optional[pulumi.Input[pulumi.InputType['UserAccountSettingsArgs']]] = None,
                 virtual_machine_configuration: Optional[pulumi.Input[pulumi.InputType['VirtualMachineConfigurationArgs']]] = None,
                 vm_priority: Optional[pulumi.Input['VmPriority']] = None,
                 vm_size: Optional[pulumi.Input[str]] = None,
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
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["location"] = location
            __props__.__dict__["node_setup"] = node_setup
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scale_settings"] = scale_settings
            __props__.__dict__["subnet"] = subnet
            __props__.__dict__["tags"] = tags
            if user_account_settings is None and not opts.urn:
                raise TypeError("Missing required property 'user_account_settings'")
            __props__.__dict__["user_account_settings"] = user_account_settings
            __props__.__dict__["virtual_machine_configuration"] = virtual_machine_configuration
            if vm_priority is None:
                vm_priority = 'dedicated'
            __props__.__dict__["vm_priority"] = vm_priority
            if vm_size is None and not opts.urn:
                raise TypeError("Missing required property 'vm_size'")
            __props__.__dict__["vm_size"] = vm_size
            __props__.__dict__["allocation_state"] = None
            __props__.__dict__["allocation_state_transition_time"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["current_node_count"] = None
            __props__.__dict__["errors"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["node_state_counts"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["provisioning_state_transition_time"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:batchai/v20180301:Cluster"), pulumi.Alias(type_="azure-native:batchai/v20170901preview:Cluster"), pulumi.Alias(type_="azure-nextgen:batchai/v20170901preview:Cluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Cluster, __self__).__init__(
            'azure-native:batchai/v20180301:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["allocation_state"] = None
        __props__.__dict__["allocation_state_transition_time"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["current_node_count"] = None
        __props__.__dict__["errors"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["node_setup"] = None
        __props__.__dict__["node_state_counts"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["provisioning_state_transition_time"] = None
        __props__.__dict__["scale_settings"] = None
        __props__.__dict__["subnet"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_account_settings"] = None
        __props__.__dict__["virtual_machine_configuration"] = None
        __props__.__dict__["vm_priority"] = None
        __props__.__dict__["vm_size"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocationState")
    def allocation_state(self) -> pulumi.Output[str]:
        """
        Possible values are: steady and resizing. steady state indicates that the cluster is not resizing. There are no changes to the number of compute nodes in the cluster in progress. A cluster enters this state when it is created and when no operations are being performed on the cluster to change the number of compute nodes. resizing state indicates that the cluster is resizing; that is, compute nodes are being added to or removed from the cluster.
        """
        return pulumi.get(self, "allocation_state")

    @property
    @pulumi.getter(name="allocationStateTransitionTime")
    def allocation_state_transition_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "allocation_state_transition_time")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="currentNodeCount")
    def current_node_count(self) -> pulumi.Output[int]:
        return pulumi.get(self, "current_node_count")

    @property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Optional[Sequence['outputs.BatchAIErrorResponse']]]:
        """
        This element contains all the errors encountered by various compute nodes during node setup.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the resource
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
    @pulumi.getter(name="nodeSetup")
    def node_setup(self) -> pulumi.Output[Optional['outputs.NodeSetupResponse']]:
        """
        Use this to prepare the VM. NOTE: The volumes specified in mountVolumes are mounted first and then the setupTask is run. Therefore the setup task can use local mountPaths in its execution.
        """
        return pulumi.get(self, "node_setup")

    @property
    @pulumi.getter(name="nodeStateCounts")
    def node_state_counts(self) -> pulumi.Output['outputs.NodeStateCountsResponse']:
        """
        Counts of various compute node states on the cluster.
        """
        return pulumi.get(self, "node_state_counts")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Possible value are: creating - Specifies that the cluster is being created. succeeded - Specifies that the cluster has been created successfully. failed - Specifies that the cluster creation has failed. deleting - Specifies that the cluster is being deleted.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="provisioningStateTransitionTime")
    def provisioning_state_transition_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "provisioning_state_transition_time")

    @property
    @pulumi.getter(name="scaleSettings")
    def scale_settings(self) -> pulumi.Output[Optional['outputs.ScaleSettingsResponse']]:
        """
        At least one of manual or autoScale settings must be specified. Only one of manual or autoScale settings can be specified. If autoScale settings are specified, the system automatically scales the cluster up and down (within the supplied limits) based on the pending jobs on the cluster.
        """
        return pulumi.get(self, "scale_settings")

    @property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional['outputs.ResourceIdResponse']]:
        """
        Represents a resource ID. For example, for a subnet, it is the resource URL for the subnet.
        """
        return pulumi.get(self, "subnet")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The tags of the resource
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAccountSettings")
    def user_account_settings(self) -> pulumi.Output[Optional['outputs.UserAccountSettingsResponse']]:
        """
        Settings for user account that gets created on each on the nodes of a cluster.
        """
        return pulumi.get(self, "user_account_settings")

    @property
    @pulumi.getter(name="virtualMachineConfiguration")
    def virtual_machine_configuration(self) -> pulumi.Output[Optional['outputs.VirtualMachineConfigurationResponse']]:
        """
        Settings for OS image.
        """
        return pulumi.get(self, "virtual_machine_configuration")

    @property
    @pulumi.getter(name="vmPriority")
    def vm_priority(self) -> pulumi.Output[Optional[str]]:
        """
        The default value is dedicated. The node can get preempted while the task is running if lowpriority is chosen. This is best suited if the workload is checkpointing and can be restarted.
        """
        return pulumi.get(self, "vm_priority")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> pulumi.Output[Optional[str]]:
        """
        All virtual machines in a cluster are the same size. For information about available VM sizes for clusters using images from the Virtual Machines Marketplace (see Sizes for Virtual Machines (Linux) or Sizes for Virtual Machines (Windows). Batch AI service supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).
        """
        return pulumi.get(self, "vm_size")

