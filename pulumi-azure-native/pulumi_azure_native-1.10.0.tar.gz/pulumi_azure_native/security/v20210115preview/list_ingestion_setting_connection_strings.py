# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'ListIngestionSettingConnectionStringsResult',
    'AwaitableListIngestionSettingConnectionStringsResult',
    'list_ingestion_setting_connection_strings',
]

@pulumi.output_type
class ListIngestionSettingConnectionStringsResult:
    """
    Connection string for ingesting security data and logs
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.IngestionConnectionStringResponse']:
        """
        Connection strings
        """
        return pulumi.get(self, "value")


class AwaitableListIngestionSettingConnectionStringsResult(ListIngestionSettingConnectionStringsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListIngestionSettingConnectionStringsResult(
            value=self.value)


def list_ingestion_setting_connection_strings(ingestion_setting_name: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListIngestionSettingConnectionStringsResult:
    """
    Connection string for ingesting security data and logs


    :param str ingestion_setting_name: Name of the ingestion setting
    """
    __args__ = dict()
    __args__['ingestionSettingName'] = ingestion_setting_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:security/v20210115preview:listIngestionSettingConnectionStrings', __args__, opts=opts, typ=ListIngestionSettingConnectionStringsResult).value

    return AwaitableListIngestionSettingConnectionStringsResult(
        value=__ret__.value)
