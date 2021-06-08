# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AddressPrefixType',
    'AdminRuleKind',
    'ConfigurationType',
    'ConnectivityTopology',
    'DeleteExistingNSGs',
    'DeleteExistingPeering',
    'GroupConnectivity',
    'IsGlobal',
    'MemberType',
    'SecurityConfigurationRuleAccess',
    'SecurityConfigurationRuleDirection',
    'SecurityConfigurationRuleProtocol',
    'SecurityType',
    'UseHubGateway',
    'UserRuleKind',
]


class AddressPrefixType(str, Enum):
    """
    Address prefix type.
    """
    IP_PREFIX = "IPPrefix"
    SERVICE_TAG = "ServiceTag"


class AdminRuleKind(str, Enum):
    """
    Whether the rule is custom or default.
    """
    CUSTOM = "Custom"
    DEFAULT = "Default"


class ConfigurationType(str, Enum):
    """
    Configuration Deployment Type.
    """
    ADMIN_SECURITY = "AdminSecurity"
    USER_SECURITY = "UserSecurity"
    CONNECTIVITY = "Connectivity"


class ConnectivityTopology(str, Enum):
    """
    Connectivity topology type.
    """
    HUB_AND_SPOKE = "HubAndSpoke"
    MESH = "Mesh"


class DeleteExistingNSGs(str, Enum):
    """
    Flag if need to delete existing network security groups.
    """
    FALSE = "False"
    TRUE = "True"


class DeleteExistingPeering(str, Enum):
    """
    Flag if need to remove current existing peerings.
    """
    FALSE = "False"
    TRUE = "True"


class GroupConnectivity(str, Enum):
    """
    Group connectivity type.
    """
    NONE = "None"
    DIRECTLY_CONNECTED = "DirectlyConnected"


class IsGlobal(str, Enum):
    """
    Flag if global mesh is supported.
    """
    FALSE = "False"
    TRUE = "True"


class MemberType(str, Enum):
    """
    Group member type.
    """
    VIRTUAL_NETWORK = "VirtualNetwork"
    SUBNET = "Subnet"


class SecurityConfigurationRuleAccess(str, Enum):
    """
    Indicates the access allowed for this particular rule
    """
    ALLOW = "Allow"
    DENY = "Deny"
    ALWAYS_ALLOW = "AlwaysAllow"


class SecurityConfigurationRuleDirection(str, Enum):
    """
    Indicates if the traffic matched against the rule in inbound or outbound.
    """
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class SecurityConfigurationRuleProtocol(str, Enum):
    """
    Network protocol this rule applies to.
    """
    TCP = "Tcp"
    UDP = "Udp"
    ICMP = "Icmp"
    ESP = "Esp"
    ANY = "Any"
    AH = "Ah"


class SecurityType(str, Enum):
    """
    Security Type.
    """
    ADMIN_POLICY = "AdminPolicy"
    USER_POLICY = "UserPolicy"


class UseHubGateway(str, Enum):
    """
    Flag if need to use hub gateway.
    """
    FALSE = "False"
    TRUE = "True"


class UserRuleKind(str, Enum):
    """
    Whether the rule is custom or default.
    """
    CUSTOM = "Custom"
    DEFAULT = "Default"
