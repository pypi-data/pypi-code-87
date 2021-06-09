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


class AppConfigConfigSchema(object):
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
        'base_image': 'BASEIMAGESENUM',
        'env_vars': 'object',
        'debian_packages': 'list[str]',
        'python': 'PythonModules',
        'post_build_cmds': 'list[str]'
    }

    attribute_map = {
        'base_image': 'base_image',
        'env_vars': 'env_vars',
        'debian_packages': 'debian_packages',
        'python': 'python',
        'post_build_cmds': 'post_build_cmds'
    }

    def __init__(self, base_image=None, env_vars=None, debian_packages=None, python=None, post_build_cmds=None, local_vars_configuration=None):  # noqa: E501
        """AppConfigConfigSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base_image = None
        self._env_vars = None
        self._debian_packages = None
        self._python = None
        self._post_build_cmds = None
        self.discriminator = None

        self.base_image = base_image
        if env_vars is not None:
            self.env_vars = env_vars
        if debian_packages is not None:
            self.debian_packages = debian_packages
        if python is not None:
            self.python = python
        if post_build_cmds is not None:
            self.post_build_cmds = post_build_cmds

    @property
    def base_image(self):
        """Gets the base_image of this AppConfigConfigSchema.  # noqa: E501


        :return: The base_image of this AppConfigConfigSchema.  # noqa: E501
        :rtype: BASEIMAGESENUM
        """
        return self._base_image

    @base_image.setter
    def base_image(self, base_image):
        """Sets the base_image of this AppConfigConfigSchema.


        :param base_image: The base_image of this AppConfigConfigSchema.  # noqa: E501
        :type: BASEIMAGESENUM
        """
        if self.local_vars_configuration.client_side_validation and base_image is None:  # noqa: E501
            raise ValueError("Invalid value for `base_image`, must not be `None`")  # noqa: E501

        self._base_image = base_image

    @property
    def env_vars(self):
        """Gets the env_vars of this AppConfigConfigSchema.  # noqa: E501

        Environment varibles in the docker image that'll be used at runtime.  # noqa: E501

        :return: The env_vars of this AppConfigConfigSchema.  # noqa: E501
        :rtype: object
        """
        return self._env_vars

    @env_vars.setter
    def env_vars(self, env_vars):
        """Sets the env_vars of this AppConfigConfigSchema.

        Environment varibles in the docker image that'll be used at runtime.  # noqa: E501

        :param env_vars: The env_vars of this AppConfigConfigSchema.  # noqa: E501
        :type: object
        """

        self._env_vars = env_vars

    @property
    def debian_packages(self):
        """Gets the debian_packages of this AppConfigConfigSchema.  # noqa: E501

        List of debian packages that'll be included in the image.  # noqa: E501

        :return: The debian_packages of this AppConfigConfigSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._debian_packages

    @debian_packages.setter
    def debian_packages(self, debian_packages):
        """Sets the debian_packages of this AppConfigConfigSchema.

        List of debian packages that'll be included in the image.  # noqa: E501

        :param debian_packages: The debian_packages of this AppConfigConfigSchema.  # noqa: E501
        :type: list[str]
        """

        self._debian_packages = debian_packages

    @property
    def python(self):
        """Gets the python of this AppConfigConfigSchema.  # noqa: E501

        Python related dependencies.  # noqa: E501

        :return: The python of this AppConfigConfigSchema.  # noqa: E501
        :rtype: PythonModules
        """
        return self._python

    @python.setter
    def python(self, python):
        """Sets the python of this AppConfigConfigSchema.

        Python related dependencies.  # noqa: E501

        :param python: The python of this AppConfigConfigSchema.  # noqa: E501
        :type: PythonModules
        """

        self._python = python

    @property
    def post_build_cmds(self):
        """Gets the post_build_cmds of this AppConfigConfigSchema.  # noqa: E501

        List of post build commands that'll be included in the image.  # noqa: E501

        :return: The post_build_cmds of this AppConfigConfigSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._post_build_cmds

    @post_build_cmds.setter
    def post_build_cmds(self, post_build_cmds):
        """Sets the post_build_cmds of this AppConfigConfigSchema.

        List of post build commands that'll be included in the image.  # noqa: E501

        :param post_build_cmds: The post_build_cmds of this AppConfigConfigSchema.  # noqa: E501
        :type: list[str]
        """

        self._post_build_cmds = post_build_cmds

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
        if not isinstance(other, AppConfigConfigSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppConfigConfigSchema):
            return True

        return self.to_dict() != other.to_dict()
