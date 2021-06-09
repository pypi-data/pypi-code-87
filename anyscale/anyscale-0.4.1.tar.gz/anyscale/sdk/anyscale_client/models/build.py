# coding: utf-8

"""
    Anyscale API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from anyscale_client.configuration import Configuration


class Build(object):
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
        'application_template_id': 'str',
        'config_json': 'AppConfigConfigSchema',
        'id': 'str',
        'revision': 'int',
        'creator_id': 'str',
        'docker_image_name': 'str',
        'error_message': 'str',
        'status': 'BuildStatus',
        'created_at': 'datetime',
        'last_modified_at': 'datetime',
        'deleted_at': 'datetime'
    }

    attribute_map = {
        'application_template_id': 'application_template_id',
        'config_json': 'config_json',
        'id': 'id',
        'revision': 'revision',
        'creator_id': 'creator_id',
        'docker_image_name': 'docker_image_name',
        'error_message': 'error_message',
        'status': 'status',
        'created_at': 'created_at',
        'last_modified_at': 'last_modified_at',
        'deleted_at': 'deleted_at'
    }

    def __init__(self, application_template_id=None, config_json=None, id=None, revision=None, creator_id=None, docker_image_name=None, error_message=None, status=None, created_at=None, last_modified_at=None, deleted_at=None, local_vars_configuration=None):  # noqa: E501
        """Build - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_template_id = None
        self._config_json = None
        self._id = None
        self._revision = None
        self._creator_id = None
        self._docker_image_name = None
        self._error_message = None
        self._status = None
        self._created_at = None
        self._last_modified_at = None
        self._deleted_at = None
        self.discriminator = None

        self.application_template_id = application_template_id
        self.config_json = config_json
        self.id = id
        self.revision = revision
        self.creator_id = creator_id
        if docker_image_name is not None:
            self.docker_image_name = docker_image_name
        if error_message is not None:
            self.error_message = error_message
        self.status = status
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        if deleted_at is not None:
            self.deleted_at = deleted_at

    @property
    def application_template_id(self):
        """Gets the application_template_id of this Build.  # noqa: E501

        ID of the App Config this Build belongs to.  # noqa: E501

        :return: The application_template_id of this Build.  # noqa: E501
        :rtype: str
        """
        return self._application_template_id

    @application_template_id.setter
    def application_template_id(self, application_template_id):
        """Sets the application_template_id of this Build.

        ID of the App Config this Build belongs to.  # noqa: E501

        :param application_template_id: The application_template_id of this Build.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application_template_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_template_id`, must not be `None`")  # noqa: E501

        self._application_template_id = application_template_id

    @property
    def config_json(self):
        """Gets the config_json of this Build.  # noqa: E501

        Config JSON used to create this Build.  # noqa: E501

        :return: The config_json of this Build.  # noqa: E501
        :rtype: AppConfigConfigSchema
        """
        return self._config_json

    @config_json.setter
    def config_json(self, config_json):
        """Sets the config_json of this Build.

        Config JSON used to create this Build.  # noqa: E501

        :param config_json: The config_json of this Build.  # noqa: E501
        :type: AppConfigConfigSchema
        """
        if self.local_vars_configuration.client_side_validation and config_json is None:  # noqa: E501
            raise ValueError("Invalid value for `config_json`, must not be `None`")  # noqa: E501

        self._config_json = config_json

    @property
    def id(self):
        """Gets the id of this Build.  # noqa: E501

        Server assigned unique identifier.  # noqa: E501

        :return: The id of this Build.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Build.

        Server assigned unique identifier.  # noqa: E501

        :param id: The id of this Build.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def revision(self):
        """Gets the revision of this Build.  # noqa: E501

        Auto incrementing version number for this Build  # noqa: E501

        :return: The revision of this Build.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this Build.

        Auto incrementing version number for this Build  # noqa: E501

        :param revision: The revision of this Build.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and revision is None:  # noqa: E501
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def creator_id(self):
        """Gets the creator_id of this Build.  # noqa: E501

        ID of the user who created this Build.  # noqa: E501

        :return: The creator_id of this Build.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this Build.

        ID of the user who created this Build.  # noqa: E501

        :param creator_id: The creator_id of this Build.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and creator_id is None:  # noqa: E501
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def docker_image_name(self):
        """Gets the docker_image_name of this Build.  # noqa: E501

        The name of the docker image for this build.  # noqa: E501

        :return: The docker_image_name of this Build.  # noqa: E501
        :rtype: str
        """
        return self._docker_image_name

    @docker_image_name.setter
    def docker_image_name(self, docker_image_name):
        """Sets the docker_image_name of this Build.

        The name of the docker image for this build.  # noqa: E501

        :param docker_image_name: The docker_image_name of this Build.  # noqa: E501
        :type: str
        """

        self._docker_image_name = docker_image_name

    @property
    def error_message(self):
        """Gets the error_message of this Build.  # noqa: E501

        Detailed error message. This will only be populated if the Build operation failed.  # noqa: E501

        :return: The error_message of this Build.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this Build.

        Detailed error message. This will only be populated if the Build operation failed.  # noqa: E501

        :param error_message: The error_message of this Build.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def status(self):
        """Gets the status of this Build.  # noqa: E501


        :return: The status of this Build.  # noqa: E501
        :rtype: BuildStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Build.


        :param status: The status of this Build.  # noqa: E501
        :type: BuildStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this Build.  # noqa: E501

        Timestamp of when this Build was created.  # noqa: E501

        :return: The created_at of this Build.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Build.

        Timestamp of when this Build was created.  # noqa: E501

        :param created_at: The created_at of this Build.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this Build.  # noqa: E501

        Timestamp of when this Build was last updated.  # noqa: E501

        :return: The last_modified_at of this Build.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this Build.

        Timestamp of when this Build was last updated.  # noqa: E501

        :param last_modified_at: The last_modified_at of this Build.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_at`, must not be `None`")  # noqa: E501

        self._last_modified_at = last_modified_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Build.  # noqa: E501

        Timestamp of when this Build was deleted.  # noqa: E501

        :return: The deleted_at of this Build.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Build.

        Timestamp of when this Build was deleted.  # noqa: E501

        :param deleted_at: The deleted_at of this Build.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

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
        if not isinstance(other, Build):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Build):
            return True

        return self.to_dict() != other.to_dict()
