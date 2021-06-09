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


class Organization(object):
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
        'id': 'str',
        'name': 'str',
        'public_identifier': 'str',
        'default_cloud_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'public_identifier': 'public_identifier',
        'default_cloud_id': 'default_cloud_id'
    }

    def __init__(self, id=None, name=None, public_identifier=None, default_cloud_id=None, local_vars_configuration=None):  # noqa: E501
        """Organization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._public_identifier = None
        self._default_cloud_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.public_identifier = public_identifier
        if default_cloud_id is not None:
            self.default_cloud_id = default_cloud_id

    @property
    def id(self):
        """Gets the id of this Organization.  # noqa: E501


        :return: The id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.


        :param id: The id of this Organization.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Organization.  # noqa: E501


        :return: The name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.


        :param name: The name of this Organization.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def public_identifier(self):
        """Gets the public_identifier of this Organization.  # noqa: E501


        :return: The public_identifier of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._public_identifier

    @public_identifier.setter
    def public_identifier(self, public_identifier):
        """Sets the public_identifier of this Organization.


        :param public_identifier: The public_identifier of this Organization.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and public_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `public_identifier`, must not be `None`")  # noqa: E501

        self._public_identifier = public_identifier

    @property
    def default_cloud_id(self):
        """Gets the default_cloud_id of this Organization.  # noqa: E501


        :return: The default_cloud_id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._default_cloud_id

    @default_cloud_id.setter
    def default_cloud_id(self, default_cloud_id):
        """Sets the default_cloud_id of this Organization.


        :param default_cloud_id: The default_cloud_id of this Organization.  # noqa: E501
        :type: str
        """

        self._default_cloud_id = default_cloud_id

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
        if not isinstance(other, Organization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Organization):
            return True

        return self.to_dict() != other.to_dict()
