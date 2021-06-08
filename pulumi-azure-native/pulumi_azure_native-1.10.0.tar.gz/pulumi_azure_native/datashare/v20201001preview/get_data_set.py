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
    'GetDataSetResult',
    'AwaitableGetDataSetResult',
    'get_data_set',
]

warnings.warn("""Please use one of the variants: ADLSGen1FileDataSet, ADLSGen1FolderDataSet, ADLSGen2FileDataSet, ADLSGen2FileSystemDataSet, ADLSGen2FolderDataSet, ADLSGen2StorageAccountDataSet, BlobContainerDataSet, BlobDataSet, BlobFolderDataSet, BlobStorageAccountDataSet, KustoClusterDataSet, KustoDatabaseDataSet, SqlDBTableDataSet, SqlDWTableDataSet, SynapseWorkspaceSqlPoolTableDataSet.""", DeprecationWarning)

@pulumi.output_type
class GetDataSetResult:
    """
    A DataSet data transfer object.
    """
    def __init__(__self__, id=None, kind=None, name=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of data set.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")


class AwaitableGetDataSetResult(GetDataSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataSetResult(
            id=self.id,
            kind=self.kind,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_data_set(account_name: Optional[str] = None,
                 data_set_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 share_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataSetResult:
    """
    A DataSet data transfer object.


    :param str account_name: The name of the share account.
    :param str data_set_name: The name of the dataSet.
    :param str resource_group_name: The resource group name.
    :param str share_name: The name of the share.
    """
    pulumi.log.warn("""get_data_set is deprecated: Please use one of the variants: ADLSGen1FileDataSet, ADLSGen1FolderDataSet, ADLSGen2FileDataSet, ADLSGen2FileSystemDataSet, ADLSGen2FolderDataSet, ADLSGen2StorageAccountDataSet, BlobContainerDataSet, BlobDataSet, BlobFolderDataSet, BlobStorageAccountDataSet, KustoClusterDataSet, KustoDatabaseDataSet, SqlDBTableDataSet, SqlDWTableDataSet, SynapseWorkspaceSqlPoolTableDataSet.""")
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataSetName'] = data_set_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:datashare/v20201001preview:getDataSet', __args__, opts=opts, typ=GetDataSetResult).value

    return AwaitableGetDataSetResult(
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        system_data=__ret__.system_data,
        type=__ret__.type)
