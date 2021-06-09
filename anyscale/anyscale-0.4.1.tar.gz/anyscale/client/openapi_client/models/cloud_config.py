# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class CloudConfig(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'max_stopped_instances': 'int'
    }

    attribute_map = {
        'max_stopped_instances': 'max_stopped_instances'
    }

    def __init__(self, max_stopped_instances=0, local_vars_configuration=None):  # noqa: E501
        """CloudConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_stopped_instances = None
        self.discriminator = None

        if max_stopped_instances is not None:
            self.max_stopped_instances = max_stopped_instances

    @property
    def max_stopped_instances(self):
        """Gets the max_stopped_instances of this CloudConfig.  # noqa: E501


        :return: The max_stopped_instances of this CloudConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_stopped_instances

    @max_stopped_instances.setter
    def max_stopped_instances(self, max_stopped_instances):
        """Sets the max_stopped_instances of this CloudConfig.


        :param max_stopped_instances: The max_stopped_instances of this CloudConfig.  # noqa: E501
        :type: int
        """

        self._max_stopped_instances = max_stopped_instances

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudConfig):
            return True

        return self.to_dict() != other.to_dict()
