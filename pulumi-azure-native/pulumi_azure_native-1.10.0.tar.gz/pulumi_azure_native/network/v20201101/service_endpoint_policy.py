# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ServiceEndpointPolicyArgs', 'ServiceEndpointPolicy']

@pulumi.input_type
class ServiceEndpointPolicyArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 service_endpoint_policy_definitions: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPolicyDefinitionArgs']]]] = None,
                 service_endpoint_policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ServiceEndpointPolicy resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPolicyDefinitionArgs']]] service_endpoint_policy_definitions: A collection of service endpoint policy definitions of the service endpoint policy.
        :param pulumi.Input[str] service_endpoint_policy_name: The name of the service endpoint policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if service_endpoint_policy_definitions is not None:
            pulumi.set(__self__, "service_endpoint_policy_definitions", service_endpoint_policy_definitions)
        if service_endpoint_policy_name is not None:
            pulumi.set(__self__, "service_endpoint_policy_name", service_endpoint_policy_name)
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
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="serviceEndpointPolicyDefinitions")
    def service_endpoint_policy_definitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPolicyDefinitionArgs']]]]:
        """
        A collection of service endpoint policy definitions of the service endpoint policy.
        """
        return pulumi.get(self, "service_endpoint_policy_definitions")

    @service_endpoint_policy_definitions.setter
    def service_endpoint_policy_definitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPolicyDefinitionArgs']]]]):
        pulumi.set(self, "service_endpoint_policy_definitions", value)

    @property
    @pulumi.getter(name="serviceEndpointPolicyName")
    def service_endpoint_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service endpoint policy.
        """
        return pulumi.get(self, "service_endpoint_policy_name")

    @service_endpoint_policy_name.setter
    def service_endpoint_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_endpoint_policy_name", value)

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


class ServiceEndpointPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_endpoint_policy_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceEndpointPolicyDefinitionArgs']]]]] = None,
                 service_endpoint_policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Service End point policy resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceEndpointPolicyDefinitionArgs']]]] service_endpoint_policy_definitions: A collection of service endpoint policy definitions of the service endpoint policy.
        :param pulumi.Input[str] service_endpoint_policy_name: The name of the service endpoint policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceEndpointPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Service End point policy resource.

        :param str resource_name: The name of the resource.
        :param ServiceEndpointPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceEndpointPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_endpoint_policy_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceEndpointPolicyDefinitionArgs']]]]] = None,
                 service_endpoint_policy_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ServiceEndpointPolicyArgs.__new__(ServiceEndpointPolicyArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["service_endpoint_policy_definitions"] = service_endpoint_policy_definitions
            __props__.__dict__["service_endpoint_policy_name"] = service_endpoint_policy_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_guid"] = None
            __props__.__dict__["subnets"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:network/v20201101:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20180701:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20180701:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20180801:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20180801:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20181001:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20181001:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20181101:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20181101:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20181201:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20181201:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20190201:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20190201:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20190401:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20190401:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20190601:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20190601:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20190701:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20190701:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20190801:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20190801:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20190901:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20190901:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20191101:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20191101:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20191201:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20191201:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20200301:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200301:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20200401:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200401:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20200501:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200501:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20200601:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200601:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20200701:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200701:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20200801:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20200801:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-native:network/v20210201:ServiceEndpointPolicy"), pulumi.Alias(type_="azure-nextgen:network/v20210201:ServiceEndpointPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServiceEndpointPolicy, __self__).__init__(
            'azure-native:network/v20201101:ServiceEndpointPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceEndpointPolicy':
        """
        Get an existing ServiceEndpointPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceEndpointPolicyArgs.__new__(ServiceEndpointPolicyArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["service_endpoint_policy_definitions"] = None
        __props__.__dict__["subnets"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ServiceEndpointPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of service endpoint policy. This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

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
        The provisioning state of the service endpoint policy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        The resource GUID property of the service endpoint policy resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="serviceEndpointPolicyDefinitions")
    def service_endpoint_policy_definitions(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceEndpointPolicyDefinitionResponse']]]:
        """
        A collection of service endpoint policy definitions of the service endpoint policy.
        """
        return pulumi.get(self, "service_endpoint_policy_definitions")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Sequence['outputs.SubnetResponse']]:
        """
        A collection of references to subnets.
        """
        return pulumi.get(self, "subnets")

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

