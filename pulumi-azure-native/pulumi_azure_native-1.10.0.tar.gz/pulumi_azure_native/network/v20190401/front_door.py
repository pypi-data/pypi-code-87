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

__all__ = ['FrontDoorArgs', 'FrontDoor']

@pulumi.input_type
class FrontDoorArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 backend_pools: Optional[pulumi.Input[Sequence[pulumi.Input['BackendPoolArgs']]]] = None,
                 backend_pools_settings: Optional[pulumi.Input['BackendPoolsSettingsArgs']] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'FrontDoorEnabledState']]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 front_door_name: Optional[pulumi.Input[str]] = None,
                 frontend_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input['FrontendEndpointArgs']]]] = None,
                 health_probe_settings: Optional[pulumi.Input[Sequence[pulumi.Input['HealthProbeSettingsModelArgs']]]] = None,
                 load_balancing_settings: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancingSettingsModelArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingRuleArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a FrontDoor resource.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[Sequence[pulumi.Input['BackendPoolArgs']]] backend_pools: Backend pools available to routing rules.
        :param pulumi.Input['BackendPoolsSettingsArgs'] backend_pools_settings: Settings for all backendPools
        :param pulumi.Input[Union[str, 'FrontDoorEnabledState']] enabled_state: Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'
        :param pulumi.Input[str] friendly_name: A friendly name for the frontDoor
        :param pulumi.Input[str] front_door_name: Name of the Front Door which is globally unique.
        :param pulumi.Input[Sequence[pulumi.Input['FrontendEndpointArgs']]] frontend_endpoints: Frontend endpoints available to routing rules.
        :param pulumi.Input[Sequence[pulumi.Input['HealthProbeSettingsModelArgs']]] health_probe_settings: Health probe settings associated with this Front Door instance.
        :param pulumi.Input[Sequence[pulumi.Input['LoadBalancingSettingsModelArgs']]] load_balancing_settings: Load balancing settings associated with this Front Door instance.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input['RoutingRuleArgs']]] routing_rules: Routing rules associated with this Front Door.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if backend_pools is not None:
            pulumi.set(__self__, "backend_pools", backend_pools)
        if backend_pools_settings is not None:
            pulumi.set(__self__, "backend_pools_settings", backend_pools_settings)
        if enabled_state is not None:
            pulumi.set(__self__, "enabled_state", enabled_state)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if front_door_name is not None:
            pulumi.set(__self__, "front_door_name", front_door_name)
        if frontend_endpoints is not None:
            pulumi.set(__self__, "frontend_endpoints", frontend_endpoints)
        if health_probe_settings is not None:
            pulumi.set(__self__, "health_probe_settings", health_probe_settings)
        if load_balancing_settings is not None:
            pulumi.set(__self__, "load_balancing_settings", load_balancing_settings)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if routing_rules is not None:
            pulumi.set(__self__, "routing_rules", routing_rules)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="backendPools")
    def backend_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BackendPoolArgs']]]]:
        """
        Backend pools available to routing rules.
        """
        return pulumi.get(self, "backend_pools")

    @backend_pools.setter
    def backend_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BackendPoolArgs']]]]):
        pulumi.set(self, "backend_pools", value)

    @property
    @pulumi.getter(name="backendPoolsSettings")
    def backend_pools_settings(self) -> Optional[pulumi.Input['BackendPoolsSettingsArgs']]:
        """
        Settings for all backendPools
        """
        return pulumi.get(self, "backend_pools_settings")

    @backend_pools_settings.setter
    def backend_pools_settings(self, value: Optional[pulumi.Input['BackendPoolsSettingsArgs']]):
        pulumi.set(self, "backend_pools_settings", value)

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[str, 'FrontDoorEnabledState']]]:
        """
        Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "enabled_state")

    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[str, 'FrontDoorEnabledState']]]):
        pulumi.set(self, "enabled_state", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        A friendly name for the frontDoor
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="frontDoorName")
    def front_door_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Front Door which is globally unique.
        """
        return pulumi.get(self, "front_door_name")

    @front_door_name.setter
    def front_door_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "front_door_name", value)

    @property
    @pulumi.getter(name="frontendEndpoints")
    def frontend_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FrontendEndpointArgs']]]]:
        """
        Frontend endpoints available to routing rules.
        """
        return pulumi.get(self, "frontend_endpoints")

    @frontend_endpoints.setter
    def frontend_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FrontendEndpointArgs']]]]):
        pulumi.set(self, "frontend_endpoints", value)

    @property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HealthProbeSettingsModelArgs']]]]:
        """
        Health probe settings associated with this Front Door instance.
        """
        return pulumi.get(self, "health_probe_settings")

    @health_probe_settings.setter
    def health_probe_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HealthProbeSettingsModelArgs']]]]):
        pulumi.set(self, "health_probe_settings", value)

    @property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancingSettingsModelArgs']]]]:
        """
        Load balancing settings associated with this Front Door instance.
        """
        return pulumi.get(self, "load_balancing_settings")

    @load_balancing_settings.setter
    def load_balancing_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancingSettingsModelArgs']]]]):
        pulumi.set(self, "load_balancing_settings", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RoutingRuleArgs']]]]:
        """
        Routing rules associated with this Front Door.
        """
        return pulumi.get(self, "routing_rules")

    @routing_rules.setter
    def routing_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingRuleArgs']]]]):
        pulumi.set(self, "routing_rules", value)

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


class FrontDoor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BackendPoolArgs']]]]] = None,
                 backend_pools_settings: Optional[pulumi.Input[pulumi.InputType['BackendPoolsSettingsArgs']]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'FrontDoorEnabledState']]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 front_door_name: Optional[pulumi.Input[str]] = None,
                 frontend_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FrontendEndpointArgs']]]]] = None,
                 health_probe_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HealthProbeSettingsModelArgs']]]]] = None,
                 load_balancing_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancingSettingsModelArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Front Door represents a collection of backend endpoints to route traffic to along with rules that specify how traffic is sent there.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BackendPoolArgs']]]] backend_pools: Backend pools available to routing rules.
        :param pulumi.Input[pulumi.InputType['BackendPoolsSettingsArgs']] backend_pools_settings: Settings for all backendPools
        :param pulumi.Input[Union[str, 'FrontDoorEnabledState']] enabled_state: Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'
        :param pulumi.Input[str] friendly_name: A friendly name for the frontDoor
        :param pulumi.Input[str] front_door_name: Name of the Front Door which is globally unique.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FrontendEndpointArgs']]]] frontend_endpoints: Frontend endpoints available to routing rules.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HealthProbeSettingsModelArgs']]]] health_probe_settings: Health probe settings associated with this Front Door instance.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancingSettingsModelArgs']]]] load_balancing_settings: Load balancing settings associated with this Front Door instance.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingRuleArgs']]]] routing_rules: Routing rules associated with this Front Door.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FrontDoorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Front Door represents a collection of backend endpoints to route traffic to along with rules that specify how traffic is sent there.

        :param str resource_name: The name of the resource.
        :param FrontDoorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FrontDoorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BackendPoolArgs']]]]] = None,
                 backend_pools_settings: Optional[pulumi.Input[pulumi.InputType['BackendPoolsSettingsArgs']]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'FrontDoorEnabledState']]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 front_door_name: Optional[pulumi.Input[str]] = None,
                 frontend_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FrontendEndpointArgs']]]]] = None,
                 health_probe_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HealthProbeSettingsModelArgs']]]]] = None,
                 load_balancing_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancingSettingsModelArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingRuleArgs']]]]] = None,
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
            __props__ = FrontDoorArgs.__new__(FrontDoorArgs)

            __props__.__dict__["backend_pools"] = backend_pools
            __props__.__dict__["backend_pools_settings"] = backend_pools_settings
            __props__.__dict__["enabled_state"] = enabled_state
            __props__.__dict__["friendly_name"] = friendly_name
            __props__.__dict__["front_door_name"] = front_door_name
            __props__.__dict__["frontend_endpoints"] = frontend_endpoints
            __props__.__dict__["health_probe_settings"] = health_probe_settings
            __props__.__dict__["load_balancing_settings"] = load_balancing_settings
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["routing_rules"] = routing_rules
            __props__.__dict__["tags"] = tags
            __props__.__dict__["cname"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20190401:FrontDoor"), pulumi.Alias(type_="azure-native:network:FrontDoor"), pulumi.Alias(type_="azure-nextgen:network:FrontDoor"), pulumi.Alias(type_="azure-native:network/v20190501:FrontDoor"), pulumi.Alias(type_="azure-nextgen:network/v20190501:FrontDoor"), pulumi.Alias(type_="azure-native:network/v20200101:FrontDoor"), pulumi.Alias(type_="azure-nextgen:network/v20200101:FrontDoor"), pulumi.Alias(type_="azure-native:network/v20200401:FrontDoor"), pulumi.Alias(type_="azure-nextgen:network/v20200401:FrontDoor"), pulumi.Alias(type_="azure-native:network/v20200501:FrontDoor"), pulumi.Alias(type_="azure-nextgen:network/v20200501:FrontDoor")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FrontDoor, __self__).__init__(
            'azure-native:network/v20190401:FrontDoor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FrontDoor':
        """
        Get an existing FrontDoor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FrontDoorArgs.__new__(FrontDoorArgs)

        __props__.__dict__["backend_pools"] = None
        __props__.__dict__["backend_pools_settings"] = None
        __props__.__dict__["cname"] = None
        __props__.__dict__["enabled_state"] = None
        __props__.__dict__["friendly_name"] = None
        __props__.__dict__["frontend_endpoints"] = None
        __props__.__dict__["health_probe_settings"] = None
        __props__.__dict__["load_balancing_settings"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["routing_rules"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return FrontDoor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendPools")
    def backend_pools(self) -> pulumi.Output[Optional[Sequence['outputs.BackendPoolResponse']]]:
        """
        Backend pools available to routing rules.
        """
        return pulumi.get(self, "backend_pools")

    @property
    @pulumi.getter(name="backendPoolsSettings")
    def backend_pools_settings(self) -> pulumi.Output[Optional['outputs.BackendPoolsSettingsResponse']]:
        """
        Settings for all backendPools
        """
        return pulumi.get(self, "backend_pools_settings")

    @property
    @pulumi.getter
    def cname(self) -> pulumi.Output[str]:
        """
        The host that each frontendEndpoint must CNAME to.
        """
        return pulumi.get(self, "cname")

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> pulumi.Output[Optional[str]]:
        """
        Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "enabled_state")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        A friendly name for the frontDoor
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="frontendEndpoints")
    def frontend_endpoints(self) -> pulumi.Output[Optional[Sequence['outputs.FrontendEndpointResponse']]]:
        """
        Frontend endpoints available to routing rules.
        """
        return pulumi.get(self, "frontend_endpoints")

    @property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> pulumi.Output[Optional[Sequence['outputs.HealthProbeSettingsModelResponse']]]:
        """
        Health probe settings associated with this Front Door instance.
        """
        return pulumi.get(self, "health_probe_settings")

    @property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(self) -> pulumi.Output[Optional[Sequence['outputs.LoadBalancingSettingsModelResponse']]]:
        """
        Load balancing settings associated with this Front Door instance.
        """
        return pulumi.get(self, "load_balancing_settings")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the Front Door.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        Resource status of the Front Door.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> pulumi.Output[Optional[Sequence['outputs.RoutingRuleResponse']]]:
        """
        Routing rules associated with this Front Door.
        """
        return pulumi.get(self, "routing_rules")

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
        Resource type.
        """
        return pulumi.get(self, "type")

