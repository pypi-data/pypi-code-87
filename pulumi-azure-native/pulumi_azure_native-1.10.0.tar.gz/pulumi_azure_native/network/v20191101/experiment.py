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

__all__ = ['ExperimentArgs', 'Experiment']

@pulumi.input_type
class ExperimentArgs:
    def __init__(__self__, *,
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'State']]] = None,
                 endpoint_a: Optional[pulumi.Input['ExperimentEndpointArgs']] = None,
                 endpoint_b: Optional[pulumi.Input['ExperimentEndpointArgs']] = None,
                 experiment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Experiment resource.
        :param pulumi.Input[str] profile_name: The Profile identifier associated with the Tenant and Partner
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] description: The description of the details or intents of the Experiment
        :param pulumi.Input[Union[str, 'State']] enabled_state: The state of the Experiment
        :param pulumi.Input['ExperimentEndpointArgs'] endpoint_a: The endpoint A of an experiment
        :param pulumi.Input['ExperimentEndpointArgs'] endpoint_b: The endpoint B of an experiment
        :param pulumi.Input[str] experiment_name: The Experiment identifier associated with the Experiment
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled_state is not None:
            pulumi.set(__self__, "enabled_state", enabled_state)
        if endpoint_a is not None:
            pulumi.set(__self__, "endpoint_a", endpoint_a)
        if endpoint_b is not None:
            pulumi.set(__self__, "endpoint_b", endpoint_b)
        if experiment_name is not None:
            pulumi.set(__self__, "experiment_name", experiment_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        The Profile identifier associated with the Tenant and Partner
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the details or intents of the Experiment
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[str, 'State']]]:
        """
        The state of the Experiment
        """
        return pulumi.get(self, "enabled_state")

    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[str, 'State']]]):
        pulumi.set(self, "enabled_state", value)

    @property
    @pulumi.getter(name="endpointA")
    def endpoint_a(self) -> Optional[pulumi.Input['ExperimentEndpointArgs']]:
        """
        The endpoint A of an experiment
        """
        return pulumi.get(self, "endpoint_a")

    @endpoint_a.setter
    def endpoint_a(self, value: Optional[pulumi.Input['ExperimentEndpointArgs']]):
        pulumi.set(self, "endpoint_a", value)

    @property
    @pulumi.getter(name="endpointB")
    def endpoint_b(self) -> Optional[pulumi.Input['ExperimentEndpointArgs']]:
        """
        The endpoint B of an experiment
        """
        return pulumi.get(self, "endpoint_b")

    @endpoint_b.setter
    def endpoint_b(self, value: Optional[pulumi.Input['ExperimentEndpointArgs']]):
        pulumi.set(self, "endpoint_b", value)

    @property
    @pulumi.getter(name="experimentName")
    def experiment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Experiment identifier associated with the Experiment
        """
        return pulumi.get(self, "experiment_name")

    @experiment_name.setter
    def experiment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "experiment_name", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Experiment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'State']]] = None,
                 endpoint_a: Optional[pulumi.Input[pulumi.InputType['ExperimentEndpointArgs']]] = None,
                 endpoint_b: Optional[pulumi.Input[pulumi.InputType['ExperimentEndpointArgs']]] = None,
                 experiment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Defines the properties of an Experiment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the details or intents of the Experiment
        :param pulumi.Input[Union[str, 'State']] enabled_state: The state of the Experiment
        :param pulumi.Input[pulumi.InputType['ExperimentEndpointArgs']] endpoint_a: The endpoint A of an experiment
        :param pulumi.Input[pulumi.InputType['ExperimentEndpointArgs']] endpoint_b: The endpoint B of an experiment
        :param pulumi.Input[str] experiment_name: The Experiment identifier associated with the Experiment
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] profile_name: The Profile identifier associated with the Tenant and Partner
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExperimentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the properties of an Experiment

        :param str resource_name: The name of the resource.
        :param ExperimentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExperimentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'State']]] = None,
                 endpoint_a: Optional[pulumi.Input[pulumi.InputType['ExperimentEndpointArgs']]] = None,
                 endpoint_b: Optional[pulumi.Input[pulumi.InputType['ExperimentEndpointArgs']]] = None,
                 experiment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ExperimentArgs.__new__(ExperimentArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["enabled_state"] = enabled_state
            __props__.__dict__["endpoint_a"] = endpoint_a
            __props__.__dict__["endpoint_b"] = endpoint_b
            __props__.__dict__["experiment_name"] = experiment_name
            __props__.__dict__["location"] = location
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["resource_state"] = None
            __props__.__dict__["script_file_uri"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20191101:Experiment"), pulumi.Alias(type_="azure-native:network:Experiment"), pulumi.Alias(type_="azure-nextgen:network:Experiment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Experiment, __self__).__init__(
            'azure-native:network/v20191101:Experiment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Experiment':
        """
        Get an existing Experiment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExperimentArgs.__new__(ExperimentArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["enabled_state"] = None
        __props__.__dict__["endpoint_a"] = None
        __props__.__dict__["endpoint_b"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["script_file_uri"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Experiment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the details or intents of the Experiment
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> pulumi.Output[Optional[str]]:
        """
        The state of the Experiment
        """
        return pulumi.get(self, "enabled_state")

    @property
    @pulumi.getter(name="endpointA")
    def endpoint_a(self) -> pulumi.Output[Optional['outputs.ExperimentEndpointResponse']]:
        """
        The endpoint A of an experiment
        """
        return pulumi.get(self, "endpoint_a")

    @property
    @pulumi.getter(name="endpointB")
    def endpoint_b(self) -> pulumi.Output[Optional['outputs.ExperimentEndpointResponse']]:
        """
        The endpoint B of an experiment
        """
        return pulumi.get(self, "endpoint_b")

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
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        Resource status.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="scriptFileUri")
    def script_file_uri(self) -> pulumi.Output[str]:
        """
        The uri to the Script used in the Experiment
        """
        return pulumi.get(self, "script_file_uri")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The description of Experiment status from the server side
        """
        return pulumi.get(self, "status")

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

