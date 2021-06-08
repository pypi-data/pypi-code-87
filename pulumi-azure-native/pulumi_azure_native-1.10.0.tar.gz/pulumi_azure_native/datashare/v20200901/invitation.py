# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['InvitationArgs', 'Invitation']

@pulumi.input_type
class InvitationArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 share_name: pulumi.Input[str],
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 invitation_name: Optional[pulumi.Input[str]] = None,
                 target_active_directory_id: Optional[pulumi.Input[str]] = None,
                 target_email: Optional[pulumi.Input[str]] = None,
                 target_object_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Invitation resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_name: The name of the share to send the invitation for.
        :param pulumi.Input[str] expiration_date: The expiration date for the invitation and share subscription.
        :param pulumi.Input[str] invitation_name: The name of the invitation.
        :param pulumi.Input[str] target_active_directory_id: The target Azure AD Id. Can't be combined with email.
        :param pulumi.Input[str] target_email: The email the invitation is directed to.
        :param pulumi.Input[str] target_object_id: The target user or application Id that invitation is being sent to.
               Must be specified along TargetActiveDirectoryId. This enables sending
               invitations to specific users or applications in an AD tenant.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "share_name", share_name)
        if expiration_date is not None:
            pulumi.set(__self__, "expiration_date", expiration_date)
        if invitation_name is not None:
            pulumi.set(__self__, "invitation_name", invitation_name)
        if target_active_directory_id is not None:
            pulumi.set(__self__, "target_active_directory_id", target_active_directory_id)
        if target_email is not None:
            pulumi.set(__self__, "target_email", target_email)
        if target_object_id is not None:
            pulumi.set(__self__, "target_object_id", target_object_id)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the share account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="shareName")
    def share_name(self) -> pulumi.Input[str]:
        """
        The name of the share to send the invitation for.
        """
        return pulumi.get(self, "share_name")

    @share_name.setter
    def share_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "share_name", value)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[str]]:
        """
        The expiration date for the invitation and share subscription.
        """
        return pulumi.get(self, "expiration_date")

    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_date", value)

    @property
    @pulumi.getter(name="invitationName")
    def invitation_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the invitation.
        """
        return pulumi.get(self, "invitation_name")

    @invitation_name.setter
    def invitation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "invitation_name", value)

    @property
    @pulumi.getter(name="targetActiveDirectoryId")
    def target_active_directory_id(self) -> Optional[pulumi.Input[str]]:
        """
        The target Azure AD Id. Can't be combined with email.
        """
        return pulumi.get(self, "target_active_directory_id")

    @target_active_directory_id.setter
    def target_active_directory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_active_directory_id", value)

    @property
    @pulumi.getter(name="targetEmail")
    def target_email(self) -> Optional[pulumi.Input[str]]:
        """
        The email the invitation is directed to.
        """
        return pulumi.get(self, "target_email")

    @target_email.setter
    def target_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_email", value)

    @property
    @pulumi.getter(name="targetObjectId")
    def target_object_id(self) -> Optional[pulumi.Input[str]]:
        """
        The target user or application Id that invitation is being sent to.
        Must be specified along TargetActiveDirectoryId. This enables sending
        invitations to specific users or applications in an AD tenant.
        """
        return pulumi.get(self, "target_object_id")

    @target_object_id.setter
    def target_object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_object_id", value)


class Invitation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 invitation_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_name: Optional[pulumi.Input[str]] = None,
                 target_active_directory_id: Optional[pulumi.Input[str]] = None,
                 target_email: Optional[pulumi.Input[str]] = None,
                 target_object_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Invitation data transfer object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] expiration_date: The expiration date for the invitation and share subscription.
        :param pulumi.Input[str] invitation_name: The name of the invitation.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_name: The name of the share to send the invitation for.
        :param pulumi.Input[str] target_active_directory_id: The target Azure AD Id. Can't be combined with email.
        :param pulumi.Input[str] target_email: The email the invitation is directed to.
        :param pulumi.Input[str] target_object_id: The target user or application Id that invitation is being sent to.
               Must be specified along TargetActiveDirectoryId. This enables sending
               invitations to specific users or applications in an AD tenant.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InvitationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Invitation data transfer object.

        :param str resource_name: The name of the resource.
        :param InvitationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InvitationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 invitation_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_name: Optional[pulumi.Input[str]] = None,
                 target_active_directory_id: Optional[pulumi.Input[str]] = None,
                 target_email: Optional[pulumi.Input[str]] = None,
                 target_object_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = InvitationArgs.__new__(InvitationArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["expiration_date"] = expiration_date
            __props__.__dict__["invitation_name"] = invitation_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if share_name is None and not opts.urn:
                raise TypeError("Missing required property 'share_name'")
            __props__.__dict__["share_name"] = share_name
            __props__.__dict__["target_active_directory_id"] = target_active_directory_id
            __props__.__dict__["target_email"] = target_email
            __props__.__dict__["target_object_id"] = target_object_id
            __props__.__dict__["invitation_id"] = None
            __props__.__dict__["invitation_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["responded_at"] = None
            __props__.__dict__["sent_at"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["user_email"] = None
            __props__.__dict__["user_name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:datashare/v20200901:Invitation"), pulumi.Alias(type_="azure-native:datashare:Invitation"), pulumi.Alias(type_="azure-nextgen:datashare:Invitation"), pulumi.Alias(type_="azure-native:datashare/v20181101preview:Invitation"), pulumi.Alias(type_="azure-nextgen:datashare/v20181101preview:Invitation"), pulumi.Alias(type_="azure-native:datashare/v20191101:Invitation"), pulumi.Alias(type_="azure-nextgen:datashare/v20191101:Invitation"), pulumi.Alias(type_="azure-native:datashare/v20201001preview:Invitation"), pulumi.Alias(type_="azure-nextgen:datashare/v20201001preview:Invitation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Invitation, __self__).__init__(
            'azure-native:datashare/v20200901:Invitation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Invitation':
        """
        Get an existing Invitation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InvitationArgs.__new__(InvitationArgs)

        __props__.__dict__["expiration_date"] = None
        __props__.__dict__["invitation_id"] = None
        __props__.__dict__["invitation_status"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["responded_at"] = None
        __props__.__dict__["sent_at"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["target_active_directory_id"] = None
        __props__.__dict__["target_email"] = None
        __props__.__dict__["target_object_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_email"] = None
        __props__.__dict__["user_name"] = None
        return Invitation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[Optional[str]]:
        """
        The expiration date for the invitation and share subscription.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter(name="invitationId")
    def invitation_id(self) -> pulumi.Output[str]:
        """
        unique invitation id
        """
        return pulumi.get(self, "invitation_id")

    @property
    @pulumi.getter(name="invitationStatus")
    def invitation_status(self) -> pulumi.Output[str]:
        """
        The status of the invitation.
        """
        return pulumi.get(self, "invitation_status")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="respondedAt")
    def responded_at(self) -> pulumi.Output[str]:
        """
        The time the recipient responded to the invitation.
        """
        return pulumi.get(self, "responded_at")

    @property
    @pulumi.getter(name="sentAt")
    def sent_at(self) -> pulumi.Output[str]:
        """
        Gets the time at which the invitation was sent.
        """
        return pulumi.get(self, "sent_at")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetActiveDirectoryId")
    def target_active_directory_id(self) -> pulumi.Output[Optional[str]]:
        """
        The target Azure AD Id. Can't be combined with email.
        """
        return pulumi.get(self, "target_active_directory_id")

    @property
    @pulumi.getter(name="targetEmail")
    def target_email(self) -> pulumi.Output[Optional[str]]:
        """
        The email the invitation is directed to.
        """
        return pulumi.get(self, "target_email")

    @property
    @pulumi.getter(name="targetObjectId")
    def target_object_id(self) -> pulumi.Output[Optional[str]]:
        """
        The target user or application Id that invitation is being sent to.
        Must be specified along TargetActiveDirectoryId. This enables sending
        invitations to specific users or applications in an AD tenant.
        """
        return pulumi.get(self, "target_object_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> pulumi.Output[str]:
        """
        Email of the user who created the resource
        """
        return pulumi.get(self, "user_email")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        Name of the user who created the resource
        """
        return pulumi.get(self, "user_name")

