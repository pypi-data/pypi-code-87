# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['WebAppFunctionArgs', 'WebAppFunction']

@pulumi.input_type
class WebAppFunctionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 config: Optional[Any] = None,
                 config_href: Optional[pulumi.Input[str]] = None,
                 files: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 href: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 script_href: Optional[pulumi.Input[str]] = None,
                 script_root_path_href: Optional[pulumi.Input[str]] = None,
                 secrets_file_href: Optional[pulumi.Input[str]] = None,
                 test_data: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebAppFunction resource.
        :param pulumi.Input[str] name: Site name.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param Any config: Config information.
        :param pulumi.Input[str] config_href: Config URI.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] files: File list.
        :param pulumi.Input[str] function_name: Function name.
        :param pulumi.Input[str] href: Function URI.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] script_href: Script URI.
        :param pulumi.Input[str] script_root_path_href: Script root path URI.
        :param pulumi.Input[str] secrets_file_href: Secrets file URI.
        :param pulumi.Input[str] test_data: Test data used when testing via the Azure Portal.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if config_href is not None:
            pulumi.set(__self__, "config_href", config_href)
        if files is not None:
            pulumi.set(__self__, "files", files)
        if function_name is not None:
            pulumi.set(__self__, "function_name", function_name)
        if href is not None:
            pulumi.set(__self__, "href", href)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if script_href is not None:
            pulumi.set(__self__, "script_href", script_href)
        if script_root_path_href is not None:
            pulumi.set(__self__, "script_root_path_href", script_root_path_href)
        if secrets_file_href is not None:
            pulumi.set(__self__, "secrets_file_href", secrets_file_href)
        if test_data is not None:
            pulumi.set(__self__, "test_data", test_data)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Site name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter
    def config(self) -> Optional[Any]:
        """
        Config information.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[Any]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="configHref")
    def config_href(self) -> Optional[pulumi.Input[str]]:
        """
        Config URI.
        """
        return pulumi.get(self, "config_href")

    @config_href.setter
    def config_href(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_href", value)

    @property
    @pulumi.getter
    def files(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        File list.
        """
        return pulumi.get(self, "files")

    @files.setter
    def files(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "files", value)

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[pulumi.Input[str]]:
        """
        Function name.
        """
        return pulumi.get(self, "function_name")

    @function_name.setter
    def function_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "function_name", value)

    @property
    @pulumi.getter
    def href(self) -> Optional[pulumi.Input[str]]:
        """
        Function URI.
        """
        return pulumi.get(self, "href")

    @href.setter
    def href(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "href", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="scriptHref")
    def script_href(self) -> Optional[pulumi.Input[str]]:
        """
        Script URI.
        """
        return pulumi.get(self, "script_href")

    @script_href.setter
    def script_href(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script_href", value)

    @property
    @pulumi.getter(name="scriptRootPathHref")
    def script_root_path_href(self) -> Optional[pulumi.Input[str]]:
        """
        Script root path URI.
        """
        return pulumi.get(self, "script_root_path_href")

    @script_root_path_href.setter
    def script_root_path_href(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script_root_path_href", value)

    @property
    @pulumi.getter(name="secretsFileHref")
    def secrets_file_href(self) -> Optional[pulumi.Input[str]]:
        """
        Secrets file URI.
        """
        return pulumi.get(self, "secrets_file_href")

    @secrets_file_href.setter
    def secrets_file_href(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secrets_file_href", value)

    @property
    @pulumi.getter(name="testData")
    def test_data(self) -> Optional[pulumi.Input[str]]:
        """
        Test data used when testing via the Azure Portal.
        """
        return pulumi.get(self, "test_data")

    @test_data.setter
    def test_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "test_data", value)


class WebAppFunction(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[Any] = None,
                 config_href: Optional[pulumi.Input[str]] = None,
                 files: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 href: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 script_href: Optional[pulumi.Input[str]] = None,
                 script_root_path_href: Optional[pulumi.Input[str]] = None,
                 secrets_file_href: Optional[pulumi.Input[str]] = None,
                 test_data: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Web Job Information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any config: Config information.
        :param pulumi.Input[str] config_href: Config URI.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] files: File list.
        :param pulumi.Input[str] function_name: Function name.
        :param pulumi.Input[str] href: Function URI.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] name: Site name.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] script_href: Script URI.
        :param pulumi.Input[str] script_root_path_href: Script root path URI.
        :param pulumi.Input[str] secrets_file_href: Secrets file URI.
        :param pulumi.Input[str] test_data: Test data used when testing via the Azure Portal.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAppFunctionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Web Job Information.

        :param str resource_name: The name of the resource.
        :param WebAppFunctionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAppFunctionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[Any] = None,
                 config_href: Optional[pulumi.Input[str]] = None,
                 files: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 href: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 script_href: Optional[pulumi.Input[str]] = None,
                 script_root_path_href: Optional[pulumi.Input[str]] = None,
                 secrets_file_href: Optional[pulumi.Input[str]] = None,
                 test_data: Optional[pulumi.Input[str]] = None,
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
            __props__ = WebAppFunctionArgs.__new__(WebAppFunctionArgs)

            __props__.__dict__["config"] = config
            __props__.__dict__["config_href"] = config_href
            __props__.__dict__["files"] = files
            __props__.__dict__["function_name"] = function_name
            __props__.__dict__["href"] = href
            __props__.__dict__["kind"] = kind
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["script_href"] = script_href
            __props__.__dict__["script_root_path_href"] = script_root_path_href
            __props__.__dict__["secrets_file_href"] = secrets_file_href
            __props__.__dict__["test_data"] = test_data
            __props__.__dict__["function_app_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:web/v20160801:WebAppFunction"), pulumi.Alias(type_="azure-native:web:WebAppFunction"), pulumi.Alias(type_="azure-nextgen:web:WebAppFunction"), pulumi.Alias(type_="azure-native:web/v20180201:WebAppFunction"), pulumi.Alias(type_="azure-nextgen:web/v20180201:WebAppFunction"), pulumi.Alias(type_="azure-native:web/v20181101:WebAppFunction"), pulumi.Alias(type_="azure-nextgen:web/v20181101:WebAppFunction"), pulumi.Alias(type_="azure-native:web/v20190801:WebAppFunction"), pulumi.Alias(type_="azure-nextgen:web/v20190801:WebAppFunction"), pulumi.Alias(type_="azure-native:web/v20200601:WebAppFunction"), pulumi.Alias(type_="azure-nextgen:web/v20200601:WebAppFunction"), pulumi.Alias(type_="azure-native:web/v20200901:WebAppFunction"), pulumi.Alias(type_="azure-nextgen:web/v20200901:WebAppFunction"), pulumi.Alias(type_="azure-native:web/v20201001:WebAppFunction"), pulumi.Alias(type_="azure-nextgen:web/v20201001:WebAppFunction"), pulumi.Alias(type_="azure-native:web/v20201201:WebAppFunction"), pulumi.Alias(type_="azure-nextgen:web/v20201201:WebAppFunction"), pulumi.Alias(type_="azure-native:web/v20210101:WebAppFunction"), pulumi.Alias(type_="azure-nextgen:web/v20210101:WebAppFunction")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WebAppFunction, __self__).__init__(
            'azure-native:web/v20160801:WebAppFunction',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebAppFunction':
        """
        Get an existing WebAppFunction resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebAppFunctionArgs.__new__(WebAppFunctionArgs)

        __props__.__dict__["config"] = None
        __props__.__dict__["config_href"] = None
        __props__.__dict__["files"] = None
        __props__.__dict__["function_app_id"] = None
        __props__.__dict__["href"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["script_href"] = None
        __props__.__dict__["script_root_path_href"] = None
        __props__.__dict__["secrets_file_href"] = None
        __props__.__dict__["test_data"] = None
        __props__.__dict__["type"] = None
        return WebAppFunction(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[Any]]:
        """
        Config information.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="configHref")
    def config_href(self) -> pulumi.Output[Optional[str]]:
        """
        Config URI.
        """
        return pulumi.get(self, "config_href")

    @property
    @pulumi.getter
    def files(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        File list.
        """
        return pulumi.get(self, "files")

    @property
    @pulumi.getter(name="functionAppId")
    def function_app_id(self) -> pulumi.Output[str]:
        """
        Function App ID.
        """
        return pulumi.get(self, "function_app_id")

    @property
    @pulumi.getter
    def href(self) -> pulumi.Output[Optional[str]]:
        """
        Function URI.
        """
        return pulumi.get(self, "href")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="scriptHref")
    def script_href(self) -> pulumi.Output[Optional[str]]:
        """
        Script URI.
        """
        return pulumi.get(self, "script_href")

    @property
    @pulumi.getter(name="scriptRootPathHref")
    def script_root_path_href(self) -> pulumi.Output[Optional[str]]:
        """
        Script root path URI.
        """
        return pulumi.get(self, "script_root_path_href")

    @property
    @pulumi.getter(name="secretsFileHref")
    def secrets_file_href(self) -> pulumi.Output[Optional[str]]:
        """
        Secrets file URI.
        """
        return pulumi.get(self, "secrets_file_href")

    @property
    @pulumi.getter(name="testData")
    def test_data(self) -> pulumi.Output[Optional[str]]:
        """
        Test data used when testing via the Azure Portal.
        """
        return pulumi.get(self, "test_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

