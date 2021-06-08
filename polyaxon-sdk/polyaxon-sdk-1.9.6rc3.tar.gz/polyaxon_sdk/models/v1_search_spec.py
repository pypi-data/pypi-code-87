#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.9.6-rc3
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from polyaxon_sdk.configuration import Configuration


class V1SearchSpec(object):
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
        'query': 'str',
        'sort': 'str',
        'limit': 'int',
        'groupby': 'str',
        'columns': 'str',
        'pins': 'str'
    }

    attribute_map = {
        'query': 'query',
        'sort': 'sort',
        'limit': 'limit',
        'groupby': 'groupby',
        'columns': 'columns',
        'pins': 'pins'
    }

    def __init__(self, query=None, sort=None, limit=None, groupby=None, columns=None, pins=None, local_vars_configuration=None):  # noqa: E501
        """V1SearchSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query = None
        self._sort = None
        self._limit = None
        self._groupby = None
        self._columns = None
        self._pins = None
        self.discriminator = None

        if query is not None:
            self.query = query
        if sort is not None:
            self.sort = sort
        if limit is not None:
            self.limit = limit
        if groupby is not None:
            self.groupby = groupby
        if columns is not None:
            self.columns = columns
        if pins is not None:
            self.pins = pins

    @property
    def query(self):
        """Gets the query of this V1SearchSpec.  # noqa: E501


        :return: The query of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this V1SearchSpec.


        :param query: The query of this V1SearchSpec.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def sort(self):
        """Gets the sort of this V1SearchSpec.  # noqa: E501


        :return: The sort of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this V1SearchSpec.


        :param sort: The sort of this V1SearchSpec.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def limit(self):
        """Gets the limit of this V1SearchSpec.  # noqa: E501


        :return: The limit of this V1SearchSpec.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this V1SearchSpec.


        :param limit: The limit of this V1SearchSpec.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def groupby(self):
        """Gets the groupby of this V1SearchSpec.  # noqa: E501


        :return: The groupby of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._groupby

    @groupby.setter
    def groupby(self, groupby):
        """Sets the groupby of this V1SearchSpec.


        :param groupby: The groupby of this V1SearchSpec.  # noqa: E501
        :type: str
        """

        self._groupby = groupby

    @property
    def columns(self):
        """Gets the columns of this V1SearchSpec.  # noqa: E501


        :return: The columns of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this V1SearchSpec.


        :param columns: The columns of this V1SearchSpec.  # noqa: E501
        :type: str
        """

        self._columns = columns

    @property
    def pins(self):
        """Gets the pins of this V1SearchSpec.  # noqa: E501


        :return: The pins of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._pins

    @pins.setter
    def pins(self, pins):
        """Sets the pins of this V1SearchSpec.


        :param pins: The pins of this V1SearchSpec.  # noqa: E501
        :type: str
        """

        self._pins = pins

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
        if not isinstance(other, V1SearchSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SearchSpec):
            return True

        return self.to_dict() != other.to_dict()
