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


class AWSCredentials(object):
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
        'aws_access_key_id': 'str',
        'aws_secret_access_key': 'str',
        'aws_session_token': 'str'
    }

    attribute_map = {
        'aws_access_key_id': 'AWS_ACCESS_KEY_ID',
        'aws_secret_access_key': 'AWS_SECRET_ACCESS_KEY',
        'aws_session_token': 'AWS_SESSION_TOKEN'
    }

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, local_vars_configuration=None):  # noqa: E501
        """AWSCredentials - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aws_access_key_id = None
        self._aws_secret_access_key = None
        self._aws_session_token = None
        self.discriminator = None

        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_session_token = aws_session_token

    @property
    def aws_access_key_id(self):
        """Gets the aws_access_key_id of this AWSCredentials.  # noqa: E501


        :return: The aws_access_key_id of this AWSCredentials.  # noqa: E501
        :rtype: str
        """
        return self._aws_access_key_id

    @aws_access_key_id.setter
    def aws_access_key_id(self, aws_access_key_id):
        """Sets the aws_access_key_id of this AWSCredentials.


        :param aws_access_key_id: The aws_access_key_id of this AWSCredentials.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and aws_access_key_id is None:  # noqa: E501
            raise ValueError("Invalid value for `aws_access_key_id`, must not be `None`")  # noqa: E501

        self._aws_access_key_id = aws_access_key_id

    @property
    def aws_secret_access_key(self):
        """Gets the aws_secret_access_key of this AWSCredentials.  # noqa: E501


        :return: The aws_secret_access_key of this AWSCredentials.  # noqa: E501
        :rtype: str
        """
        return self._aws_secret_access_key

    @aws_secret_access_key.setter
    def aws_secret_access_key(self, aws_secret_access_key):
        """Sets the aws_secret_access_key of this AWSCredentials.


        :param aws_secret_access_key: The aws_secret_access_key of this AWSCredentials.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and aws_secret_access_key is None:  # noqa: E501
            raise ValueError("Invalid value for `aws_secret_access_key`, must not be `None`")  # noqa: E501

        self._aws_secret_access_key = aws_secret_access_key

    @property
    def aws_session_token(self):
        """Gets the aws_session_token of this AWSCredentials.  # noqa: E501


        :return: The aws_session_token of this AWSCredentials.  # noqa: E501
        :rtype: str
        """
        return self._aws_session_token

    @aws_session_token.setter
    def aws_session_token(self, aws_session_token):
        """Sets the aws_session_token of this AWSCredentials.


        :param aws_session_token: The aws_session_token of this AWSCredentials.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and aws_session_token is None:  # noqa: E501
            raise ValueError("Invalid value for `aws_session_token`, must not be `None`")  # noqa: E501

        self._aws_session_token = aws_session_token

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
        if not isinstance(other, AWSCredentials):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AWSCredentials):
            return True

        return self.to_dict() != other.to_dict()
