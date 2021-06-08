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

__all__ = ['InputArgs', 'Input']

@pulumi.input_type
class InputArgs:
    def __init__(__self__, *,
                 job_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 input_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['ReferenceInputPropertiesArgs', 'StreamInputPropertiesArgs']]] = None):
        """
        The set of arguments for constructing a Input resource.
        :param pulumi.Input[str] job_name: The name of the streaming job.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] input_name: The name of the input.
        :param pulumi.Input[str] name: Resource name
        :param pulumi.Input[Union['ReferenceInputPropertiesArgs', 'StreamInputPropertiesArgs']] properties: The properties that are associated with an input. Required on PUT (CreateOrReplace) requests.
        """
        pulumi.set(__self__, "job_name", job_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if input_name is not None:
            pulumi.set(__self__, "input_name", input_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[str]:
        """
        The name of the streaming job.
        """
        return pulumi.get(self, "job_name")

    @job_name.setter
    def job_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "job_name", value)

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
    @pulumi.getter(name="inputName")
    def input_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the input.
        """
        return pulumi.get(self, "input_name")

    @input_name.setter
    def input_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Union['ReferenceInputPropertiesArgs', 'StreamInputPropertiesArgs']]]:
        """
        The properties that are associated with an input. Required on PUT (CreateOrReplace) requests.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Union['ReferenceInputPropertiesArgs', 'StreamInputPropertiesArgs']]]):
        pulumi.set(self, "properties", value)


class Input(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 input_name: Optional[pulumi.Input[str]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ReferenceInputPropertiesArgs'], pulumi.InputType['StreamInputPropertiesArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An input object, containing all information associated with the named input. All inputs are contained under a streaming job.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] input_name: The name of the input.
        :param pulumi.Input[str] job_name: The name of the streaming job.
        :param pulumi.Input[str] name: Resource name
        :param pulumi.Input[Union[pulumi.InputType['ReferenceInputPropertiesArgs'], pulumi.InputType['StreamInputPropertiesArgs']]] properties: The properties that are associated with an input. Required on PUT (CreateOrReplace) requests.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InputArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An input object, containing all information associated with the named input. All inputs are contained under a streaming job.

        :param str resource_name: The name of the resource.
        :param InputArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InputArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 input_name: Optional[pulumi.Input[str]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ReferenceInputPropertiesArgs'], pulumi.InputType['StreamInputPropertiesArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = InputArgs.__new__(InputArgs)

            __props__.__dict__["input_name"] = input_name
            if job_name is None and not opts.urn:
                raise TypeError("Missing required property 'job_name'")
            __props__.__dict__["job_name"] = job_name
            __props__.__dict__["name"] = name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:streamanalytics/v20170401preview:Input"), pulumi.Alias(type_="azure-native:streamanalytics:Input"), pulumi.Alias(type_="azure-nextgen:streamanalytics:Input"), pulumi.Alias(type_="azure-native:streamanalytics/v20160301:Input"), pulumi.Alias(type_="azure-nextgen:streamanalytics/v20160301:Input")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Input, __self__).__init__(
            'azure-native:streamanalytics/v20170401preview:Input',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Input':
        """
        Get an existing Input resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InputArgs.__new__(InputArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return Input(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        The properties that are associated with an input. Required on PUT (CreateOrReplace) requests.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

