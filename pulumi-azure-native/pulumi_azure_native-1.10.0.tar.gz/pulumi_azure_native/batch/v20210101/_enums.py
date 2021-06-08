# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AutoUserScope',
    'CachingType',
    'CertificateFormat',
    'CertificateStoreLocation',
    'CertificateVisibility',
    'ComputeNodeDeallocationOption',
    'ComputeNodeFillType',
    'ContainerType',
    'ContainerWorkingDirectory',
    'DiskEncryptionTarget',
    'ElevationLevel',
    'IPAddressProvisioningType',
    'InboundEndpointProtocol',
    'InterNodeCommunicationState',
    'KeySource',
    'LoginMode',
    'NetworkSecurityGroupRuleAccess',
    'NodePlacementPolicyType',
    'PoolAllocationMode',
    'PoolIdentityType',
    'PublicNetworkAccessType',
    'ResourceIdentityType',
    'StorageAccountType',
]


class AutoUserScope(str, Enum):
    """
    The default value is Pool. If the pool is running Windows a value of Task should be specified if stricter isolation between tasks is required. For example, if the task mutates the registry in a way which could impact other tasks, or if certificates have been specified on the pool which should not be accessible by normal tasks but should be accessible by start tasks.
    """
    TASK = "Task"
    POOL = "Pool"


class CachingType(str, Enum):
    """
    Values are:

     none - The caching mode for the disk is not enabled.
     readOnly - The caching mode for the disk is read only.
     readWrite - The caching mode for the disk is read and write.

     The default value for caching is none. For information about the caching options see: https://blogs.msdn.microsoft.com/windowsazurestorage/2012/06/27/exploring-windows-azure-drives-disks-and-images/.
    """
    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class CertificateFormat(str, Enum):
    """
    The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx.
    """
    PFX = "Pfx"
    CER = "Cer"


class CertificateStoreLocation(str, Enum):
    """
    The default value is currentUser. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of 'remoteUser', a 'certs' directory is created in the user's home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory.
    """
    CURRENT_USER = "CurrentUser"
    LOCAL_MACHINE = "LocalMachine"


class CertificateVisibility(str, Enum):
    START_TASK = "StartTask"
    TASK = "Task"
    REMOTE_USER = "RemoteUser"


class ComputeNodeDeallocationOption(str, Enum):
    """
    If omitted, the default value is Requeue.
    """
    REQUEUE = "Requeue"
    TERMINATE = "Terminate"
    TASK_COMPLETION = "TaskCompletion"
    RETAINED_DATA = "RetainedData"


class ComputeNodeFillType(str, Enum):
    SPREAD = "Spread"
    PACK = "Pack"


class ContainerType(str, Enum):
    DOCKER_COMPATIBLE = "DockerCompatible"


class ContainerWorkingDirectory(str, Enum):
    TASK_WORKING_DIRECTORY = "TaskWorkingDirectory"
    CONTAINER_IMAGE_DEFAULT = "ContainerImageDefault"


class DiskEncryptionTarget(str, Enum):
    """
    If omitted, no disks on the compute nodes in the pool will be encrypted.
    """
    OS_DISK = "OsDisk"
    TEMPORARY_DISK = "TemporaryDisk"


class ElevationLevel(str, Enum):
    """
    nonAdmin - The auto user is a standard user without elevated access. admin - The auto user is a user with elevated access and operates with full Administrator permissions. The default value is nonAdmin.
    """
    NON_ADMIN = "NonAdmin"
    ADMIN = "Admin"


class IPAddressProvisioningType(str, Enum):
    """
    The default value is BatchManaged
    """
    BATCH_MANAGED = "BatchManaged"
    USER_MANAGED = "UserManaged"
    NO_PUBLIC_IP_ADDRESSES = "NoPublicIPAddresses"


class InboundEndpointProtocol(str, Enum):
    TCP = "TCP"
    UDP = "UDP"


class InterNodeCommunicationState(str, Enum):
    """
    This imposes restrictions on which nodes can be assigned to the pool. Enabling this value can reduce the chance of the requested number of nodes to be allocated in the pool. If not specified, this value defaults to 'Disabled'.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class KeySource(str, Enum):
    """
    Type of the key source.
    """
    MICROSOFT_BATCH = "Microsoft.Batch"
    MICROSOFT_KEY_VAULT = "Microsoft.KeyVault"


class LoginMode(str, Enum):
    """
    Specifies login mode for the user. The default value for VirtualMachineConfiguration pools is interactive mode and for CloudServiceConfiguration pools is batch mode.
    """
    BATCH = "Batch"
    INTERACTIVE = "Interactive"


class NetworkSecurityGroupRuleAccess(str, Enum):
    ALLOW = "Allow"
    DENY = "Deny"


class NodePlacementPolicyType(str, Enum):
    """
    Allocation policy used by Batch Service to provision the nodes. If not specified, Batch will use the regional policy.
    """
    REGIONAL = "Regional"
    ZONAL = "Zonal"


class PoolAllocationMode(str, Enum):
    """
    The pool allocation mode also affects how clients may authenticate to the Batch Service API. If the mode is BatchService, clients may authenticate using access keys or Azure Active Directory. If the mode is UserSubscription, clients must use Azure Active Directory. The default is BatchService.
    """
    BATCH_SERVICE = "BatchService"
    USER_SUBSCRIPTION = "UserSubscription"


class PoolIdentityType(str, Enum):
    """
    The type of identity used for the Batch Pool.
    """
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"


class PublicNetworkAccessType(str, Enum):
    """
    If not specified, the default value is 'enabled'.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the Batch account.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"


class StorageAccountType(str, Enum):
    """
    If omitted, the default is "Standard_LRS". Values are:

     Standard_LRS - The data disk should use standard locally redundant storage.
     Premium_LRS - The data disk should use premium locally redundant storage.
    """
    STANDARD_LRS = "Standard_LRS"
    PREMIUM_LRS = "Premium_LRS"
