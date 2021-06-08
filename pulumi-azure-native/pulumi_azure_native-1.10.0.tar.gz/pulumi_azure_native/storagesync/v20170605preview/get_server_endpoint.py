# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetServerEndpointResult',
    'AwaitableGetServerEndpointResult',
    'get_server_endpoint',
]

@pulumi.output_type
class GetServerEndpointResult:
    """
    Server Endpoint object.
    """
    def __init__(__self__, byte_progress=None, byte_total=None, cloud_tiering=None, current_progress_type=None, friendly_name=None, id=None, item_download_error_count=None, item_progress_count=None, item_total_count=None, item_upload_error_count=None, last_sync_success=None, last_workflow_id=None, name=None, provisioning_state=None, server_local_path=None, server_resource_id=None, sync_error_context=None, sync_error_direction=None, sync_error_state=None, sync_error_state_timestamp=None, total_progress=None, type=None, volume_free_space_percent=None):
        if byte_progress and not isinstance(byte_progress, int):
            raise TypeError("Expected argument 'byte_progress' to be a int")
        pulumi.set(__self__, "byte_progress", byte_progress)
        if byte_total and not isinstance(byte_total, int):
            raise TypeError("Expected argument 'byte_total' to be a int")
        pulumi.set(__self__, "byte_total", byte_total)
        if cloud_tiering and not isinstance(cloud_tiering, str):
            raise TypeError("Expected argument 'cloud_tiering' to be a str")
        pulumi.set(__self__, "cloud_tiering", cloud_tiering)
        if current_progress_type and not isinstance(current_progress_type, str):
            raise TypeError("Expected argument 'current_progress_type' to be a str")
        pulumi.set(__self__, "current_progress_type", current_progress_type)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if item_download_error_count and not isinstance(item_download_error_count, int):
            raise TypeError("Expected argument 'item_download_error_count' to be a int")
        pulumi.set(__self__, "item_download_error_count", item_download_error_count)
        if item_progress_count and not isinstance(item_progress_count, int):
            raise TypeError("Expected argument 'item_progress_count' to be a int")
        pulumi.set(__self__, "item_progress_count", item_progress_count)
        if item_total_count and not isinstance(item_total_count, int):
            raise TypeError("Expected argument 'item_total_count' to be a int")
        pulumi.set(__self__, "item_total_count", item_total_count)
        if item_upload_error_count and not isinstance(item_upload_error_count, int):
            raise TypeError("Expected argument 'item_upload_error_count' to be a int")
        pulumi.set(__self__, "item_upload_error_count", item_upload_error_count)
        if last_sync_success and not isinstance(last_sync_success, str):
            raise TypeError("Expected argument 'last_sync_success' to be a str")
        pulumi.set(__self__, "last_sync_success", last_sync_success)
        if last_workflow_id and not isinstance(last_workflow_id, str):
            raise TypeError("Expected argument 'last_workflow_id' to be a str")
        pulumi.set(__self__, "last_workflow_id", last_workflow_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if server_local_path and not isinstance(server_local_path, str):
            raise TypeError("Expected argument 'server_local_path' to be a str")
        pulumi.set(__self__, "server_local_path", server_local_path)
        if server_resource_id and not isinstance(server_resource_id, str):
            raise TypeError("Expected argument 'server_resource_id' to be a str")
        pulumi.set(__self__, "server_resource_id", server_resource_id)
        if sync_error_context and not isinstance(sync_error_context, str):
            raise TypeError("Expected argument 'sync_error_context' to be a str")
        pulumi.set(__self__, "sync_error_context", sync_error_context)
        if sync_error_direction and not isinstance(sync_error_direction, str):
            raise TypeError("Expected argument 'sync_error_direction' to be a str")
        pulumi.set(__self__, "sync_error_direction", sync_error_direction)
        if sync_error_state and not isinstance(sync_error_state, str):
            raise TypeError("Expected argument 'sync_error_state' to be a str")
        pulumi.set(__self__, "sync_error_state", sync_error_state)
        if sync_error_state_timestamp and not isinstance(sync_error_state_timestamp, str):
            raise TypeError("Expected argument 'sync_error_state_timestamp' to be a str")
        pulumi.set(__self__, "sync_error_state_timestamp", sync_error_state_timestamp)
        if total_progress and not isinstance(total_progress, int):
            raise TypeError("Expected argument 'total_progress' to be a int")
        pulumi.set(__self__, "total_progress", total_progress)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volume_free_space_percent and not isinstance(volume_free_space_percent, int):
            raise TypeError("Expected argument 'volume_free_space_percent' to be a int")
        pulumi.set(__self__, "volume_free_space_percent", volume_free_space_percent)

    @property
    @pulumi.getter(name="byteProgress")
    def byte_progress(self) -> Optional[int]:
        """
        Bytes in progress
        """
        return pulumi.get(self, "byte_progress")

    @property
    @pulumi.getter(name="byteTotal")
    def byte_total(self) -> Optional[int]:
        """
        Bytes total
        """
        return pulumi.get(self, "byte_total")

    @property
    @pulumi.getter(name="cloudTiering")
    def cloud_tiering(self) -> Optional[str]:
        """
        Cloud Tiering.
        """
        return pulumi.get(self, "cloud_tiering")

    @property
    @pulumi.getter(name="currentProgressType")
    def current_progress_type(self) -> Optional[str]:
        """
        current progress type.
        """
        return pulumi.get(self, "current_progress_type")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        Friendly Name
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="itemDownloadErrorCount")
    def item_download_error_count(self) -> Optional[int]:
        """
        Item download error count.
        """
        return pulumi.get(self, "item_download_error_count")

    @property
    @pulumi.getter(name="itemProgressCount")
    def item_progress_count(self) -> Optional[int]:
        """
        Item Progress Count
        """
        return pulumi.get(self, "item_progress_count")

    @property
    @pulumi.getter(name="itemTotalCount")
    def item_total_count(self) -> Optional[int]:
        """
        Item Total Count
        """
        return pulumi.get(self, "item_total_count")

    @property
    @pulumi.getter(name="itemUploadErrorCount")
    def item_upload_error_count(self) -> Optional[int]:
        """
        Item Upload Error Count.
        """
        return pulumi.get(self, "item_upload_error_count")

    @property
    @pulumi.getter(name="lastSyncSuccess")
    def last_sync_success(self) -> Optional[str]:
        """
        Last Sync Success
        """
        return pulumi.get(self, "last_sync_success")

    @property
    @pulumi.getter(name="lastWorkflowId")
    def last_workflow_id(self) -> Optional[str]:
        """
        ServerEndpoint lastWorkflowId
        """
        return pulumi.get(self, "last_workflow_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        ServerEndpoint Provisioning State
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serverLocalPath")
    def server_local_path(self) -> Optional[str]:
        """
        Server Local path.
        """
        return pulumi.get(self, "server_local_path")

    @property
    @pulumi.getter(name="serverResourceId")
    def server_resource_id(self) -> Optional[str]:
        """
        Server Resource Id.
        """
        return pulumi.get(self, "server_resource_id")

    @property
    @pulumi.getter(name="syncErrorContext")
    def sync_error_context(self) -> Optional[str]:
        """
        sync error context.
        """
        return pulumi.get(self, "sync_error_context")

    @property
    @pulumi.getter(name="syncErrorDirection")
    def sync_error_direction(self) -> Optional[str]:
        """
        Sync Error Direction.
        """
        return pulumi.get(self, "sync_error_direction")

    @property
    @pulumi.getter(name="syncErrorState")
    def sync_error_state(self) -> Optional[str]:
        """
        Sync Error State
        """
        return pulumi.get(self, "sync_error_state")

    @property
    @pulumi.getter(name="syncErrorStateTimestamp")
    def sync_error_state_timestamp(self) -> Optional[str]:
        """
        Sync Error State Timestamp
        """
        return pulumi.get(self, "sync_error_state_timestamp")

    @property
    @pulumi.getter(name="totalProgress")
    def total_progress(self) -> Optional[int]:
        """
        Total progress
        """
        return pulumi.get(self, "total_progress")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeFreeSpacePercent")
    def volume_free_space_percent(self) -> Optional[int]:
        """
        Level of free space to be maintained by Cloud Tiering if it is enabled.
        """
        return pulumi.get(self, "volume_free_space_percent")


class AwaitableGetServerEndpointResult(GetServerEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerEndpointResult(
            byte_progress=self.byte_progress,
            byte_total=self.byte_total,
            cloud_tiering=self.cloud_tiering,
            current_progress_type=self.current_progress_type,
            friendly_name=self.friendly_name,
            id=self.id,
            item_download_error_count=self.item_download_error_count,
            item_progress_count=self.item_progress_count,
            item_total_count=self.item_total_count,
            item_upload_error_count=self.item_upload_error_count,
            last_sync_success=self.last_sync_success,
            last_workflow_id=self.last_workflow_id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            server_local_path=self.server_local_path,
            server_resource_id=self.server_resource_id,
            sync_error_context=self.sync_error_context,
            sync_error_direction=self.sync_error_direction,
            sync_error_state=self.sync_error_state,
            sync_error_state_timestamp=self.sync_error_state_timestamp,
            total_progress=self.total_progress,
            type=self.type,
            volume_free_space_percent=self.volume_free_space_percent)


def get_server_endpoint(resource_group_name: Optional[str] = None,
                        server_endpoint_name: Optional[str] = None,
                        storage_sync_service_name: Optional[str] = None,
                        sync_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerEndpointResult:
    """
    Server Endpoint object.


    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str server_endpoint_name: Name of Server Endpoint object.
    :param str storage_sync_service_name: Name of Storage Sync Service resource.
    :param str sync_group_name: Name of Sync Group resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverEndpointName'] = server_endpoint_name
    __args__['storageSyncServiceName'] = storage_sync_service_name
    __args__['syncGroupName'] = sync_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:storagesync/v20170605preview:getServerEndpoint', __args__, opts=opts, typ=GetServerEndpointResult).value

    return AwaitableGetServerEndpointResult(
        byte_progress=__ret__.byte_progress,
        byte_total=__ret__.byte_total,
        cloud_tiering=__ret__.cloud_tiering,
        current_progress_type=__ret__.current_progress_type,
        friendly_name=__ret__.friendly_name,
        id=__ret__.id,
        item_download_error_count=__ret__.item_download_error_count,
        item_progress_count=__ret__.item_progress_count,
        item_total_count=__ret__.item_total_count,
        item_upload_error_count=__ret__.item_upload_error_count,
        last_sync_success=__ret__.last_sync_success,
        last_workflow_id=__ret__.last_workflow_id,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        server_local_path=__ret__.server_local_path,
        server_resource_id=__ret__.server_resource_id,
        sync_error_context=__ret__.sync_error_context,
        sync_error_direction=__ret__.sync_error_direction,
        sync_error_state=__ret__.sync_error_state,
        sync_error_state_timestamp=__ret__.sync_error_state_timestamp,
        total_progress=__ret__.total_progress,
        type=__ret__.type,
        volume_free_space_percent=__ret__.volume_free_space_percent)
