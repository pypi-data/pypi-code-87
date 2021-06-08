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
    'GetPrivateStoreCollectionResult',
    'AwaitableGetPrivateStoreCollectionResult',
    'get_private_store_collection',
]

@pulumi.output_type
class GetPrivateStoreCollectionResult:
    """
    The Collection data structure.
    """
    def __init__(__self__, all_subscriptions=None, claim=None, collection_id=None, collection_name=None, enabled=None, id=None, name=None, number_of_offers=None, subscriptions_list=None, system_data=None, type=None):
        if all_subscriptions and not isinstance(all_subscriptions, bool):
            raise TypeError("Expected argument 'all_subscriptions' to be a bool")
        pulumi.set(__self__, "all_subscriptions", all_subscriptions)
        if claim and not isinstance(claim, str):
            raise TypeError("Expected argument 'claim' to be a str")
        pulumi.set(__self__, "claim", claim)
        if collection_id and not isinstance(collection_id, str):
            raise TypeError("Expected argument 'collection_id' to be a str")
        pulumi.set(__self__, "collection_id", collection_id)
        if collection_name and not isinstance(collection_name, str):
            raise TypeError("Expected argument 'collection_name' to be a str")
        pulumi.set(__self__, "collection_name", collection_name)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if number_of_offers and not isinstance(number_of_offers, float):
            raise TypeError("Expected argument 'number_of_offers' to be a float")
        pulumi.set(__self__, "number_of_offers", number_of_offers)
        if subscriptions_list and not isinstance(subscriptions_list, list):
            raise TypeError("Expected argument 'subscriptions_list' to be a list")
        pulumi.set(__self__, "subscriptions_list", subscriptions_list)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="allSubscriptions")
    def all_subscriptions(self) -> Optional[bool]:
        """
        Indicating whether all subscriptions are selected (=true) or not (=false).
        """
        return pulumi.get(self, "all_subscriptions")

    @property
    @pulumi.getter
    def claim(self) -> Optional[str]:
        """
        Gets or sets the association with Commercial's Billing Account.
        """
        return pulumi.get(self, "claim")

    @property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> str:
        """
        Gets collection Id.
        """
        return pulumi.get(self, "collection_id")

    @property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> Optional[str]:
        """
        Gets or sets collection name.
        """
        return pulumi.get(self, "collection_name")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Indicating whether the collection is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numberOfOffers")
    def number_of_offers(self) -> float:
        """
        Gets the number of offers associated with the collection.
        """
        return pulumi.get(self, "number_of_offers")

    @property
    @pulumi.getter(name="subscriptionsList")
    def subscriptions_list(self) -> Optional[Sequence[str]]:
        """
        Gets or sets subscription ids list. Empty list indicates all subscriptions are selected, null indicates no update is done, explicit list indicates the explicit selected subscriptions. On insert, null is considered as bad request
        """
        return pulumi.get(self, "subscriptions_list")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetPrivateStoreCollectionResult(GetPrivateStoreCollectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateStoreCollectionResult(
            all_subscriptions=self.all_subscriptions,
            claim=self.claim,
            collection_id=self.collection_id,
            collection_name=self.collection_name,
            enabled=self.enabled,
            id=self.id,
            name=self.name,
            number_of_offers=self.number_of_offers,
            subscriptions_list=self.subscriptions_list,
            system_data=self.system_data,
            type=self.type)


def get_private_store_collection(collection_id: Optional[str] = None,
                                 private_store_id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateStoreCollectionResult:
    """
    The Collection data structure.


    :param str collection_id: The collection ID
    :param str private_store_id: The store ID - must use the tenant ID
    """
    __args__ = dict()
    __args__['collectionId'] = collection_id
    __args__['privateStoreId'] = private_store_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:marketplace/v20210601:getPrivateStoreCollection', __args__, opts=opts, typ=GetPrivateStoreCollectionResult).value

    return AwaitableGetPrivateStoreCollectionResult(
        all_subscriptions=__ret__.all_subscriptions,
        claim=__ret__.claim,
        collection_id=__ret__.collection_id,
        collection_name=__ret__.collection_name,
        enabled=__ret__.enabled,
        id=__ret__.id,
        name=__ret__.name,
        number_of_offers=__ret__.number_of_offers,
        subscriptions_list=__ret__.subscriptions_list,
        system_data=__ret__.system_data,
        type=__ret__.type)
