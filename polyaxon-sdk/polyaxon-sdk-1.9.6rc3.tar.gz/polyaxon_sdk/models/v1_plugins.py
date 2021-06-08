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


class V1Plugins(object):
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
        'auth': 'bool',
        'docker': 'bool',
        'shm': 'bool',
        'mount_artifacts_store': 'bool',
        'collect_artifacts': 'bool',
        'collect_logs': 'bool',
        'collect_resources': 'str',
        'sync_statuses': 'bool',
        'auto_resume': 'bool',
        'log_level': 'str',
        'external_host': 'bool',
        'sidecar': 'V1PolyaxonSidecarContainer',
        'notifications': 'list[V1Notification]'
    }

    attribute_map = {
        'auth': 'auth',
        'docker': 'docker',
        'shm': 'shm',
        'mount_artifacts_store': 'mountArtifactsStore',
        'collect_artifacts': 'collectArtifacts',
        'collect_logs': 'collectLogs',
        'collect_resources': 'collectResources',
        'sync_statuses': 'syncStatuses',
        'auto_resume': 'autoResume',
        'log_level': 'logLevel',
        'external_host': 'externalHost',
        'sidecar': 'sidecar',
        'notifications': 'notifications'
    }

    def __init__(self, auth=None, docker=None, shm=None, mount_artifacts_store=None, collect_artifacts=None, collect_logs=None, collect_resources=None, sync_statuses=None, auto_resume=None, log_level=None, external_host=None, sidecar=None, notifications=None, local_vars_configuration=None):  # noqa: E501
        """V1Plugins - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auth = None
        self._docker = None
        self._shm = None
        self._mount_artifacts_store = None
        self._collect_artifacts = None
        self._collect_logs = None
        self._collect_resources = None
        self._sync_statuses = None
        self._auto_resume = None
        self._log_level = None
        self._external_host = None
        self._sidecar = None
        self._notifications = None
        self.discriminator = None

        if auth is not None:
            self.auth = auth
        if docker is not None:
            self.docker = docker
        if shm is not None:
            self.shm = shm
        if mount_artifacts_store is not None:
            self.mount_artifacts_store = mount_artifacts_store
        if collect_artifacts is not None:
            self.collect_artifacts = collect_artifacts
        if collect_logs is not None:
            self.collect_logs = collect_logs
        if collect_resources is not None:
            self.collect_resources = collect_resources
        if sync_statuses is not None:
            self.sync_statuses = sync_statuses
        if auto_resume is not None:
            self.auto_resume = auto_resume
        if log_level is not None:
            self.log_level = log_level
        if external_host is not None:
            self.external_host = external_host
        if sidecar is not None:
            self.sidecar = sidecar
        if notifications is not None:
            self.notifications = notifications

    @property
    def auth(self):
        """Gets the auth of this V1Plugins.  # noqa: E501


        :return: The auth of this V1Plugins.  # noqa: E501
        :rtype: bool
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this V1Plugins.


        :param auth: The auth of this V1Plugins.  # noqa: E501
        :type: bool
        """

        self._auth = auth

    @property
    def docker(self):
        """Gets the docker of this V1Plugins.  # noqa: E501


        :return: The docker of this V1Plugins.  # noqa: E501
        :rtype: bool
        """
        return self._docker

    @docker.setter
    def docker(self, docker):
        """Sets the docker of this V1Plugins.


        :param docker: The docker of this V1Plugins.  # noqa: E501
        :type: bool
        """

        self._docker = docker

    @property
    def shm(self):
        """Gets the shm of this V1Plugins.  # noqa: E501


        :return: The shm of this V1Plugins.  # noqa: E501
        :rtype: bool
        """
        return self._shm

    @shm.setter
    def shm(self, shm):
        """Sets the shm of this V1Plugins.


        :param shm: The shm of this V1Plugins.  # noqa: E501
        :type: bool
        """

        self._shm = shm

    @property
    def mount_artifacts_store(self):
        """Gets the mount_artifacts_store of this V1Plugins.  # noqa: E501


        :return: The mount_artifacts_store of this V1Plugins.  # noqa: E501
        :rtype: bool
        """
        return self._mount_artifacts_store

    @mount_artifacts_store.setter
    def mount_artifacts_store(self, mount_artifacts_store):
        """Sets the mount_artifacts_store of this V1Plugins.


        :param mount_artifacts_store: The mount_artifacts_store of this V1Plugins.  # noqa: E501
        :type: bool
        """

        self._mount_artifacts_store = mount_artifacts_store

    @property
    def collect_artifacts(self):
        """Gets the collect_artifacts of this V1Plugins.  # noqa: E501


        :return: The collect_artifacts of this V1Plugins.  # noqa: E501
        :rtype: bool
        """
        return self._collect_artifacts

    @collect_artifacts.setter
    def collect_artifacts(self, collect_artifacts):
        """Sets the collect_artifacts of this V1Plugins.


        :param collect_artifacts: The collect_artifacts of this V1Plugins.  # noqa: E501
        :type: bool
        """

        self._collect_artifacts = collect_artifacts

    @property
    def collect_logs(self):
        """Gets the collect_logs of this V1Plugins.  # noqa: E501


        :return: The collect_logs of this V1Plugins.  # noqa: E501
        :rtype: bool
        """
        return self._collect_logs

    @collect_logs.setter
    def collect_logs(self, collect_logs):
        """Sets the collect_logs of this V1Plugins.


        :param collect_logs: The collect_logs of this V1Plugins.  # noqa: E501
        :type: bool
        """

        self._collect_logs = collect_logs

    @property
    def collect_resources(self):
        """Gets the collect_resources of this V1Plugins.  # noqa: E501


        :return: The collect_resources of this V1Plugins.  # noqa: E501
        :rtype: str
        """
        return self._collect_resources

    @collect_resources.setter
    def collect_resources(self, collect_resources):
        """Sets the collect_resources of this V1Plugins.


        :param collect_resources: The collect_resources of this V1Plugins.  # noqa: E501
        :type: str
        """

        self._collect_resources = collect_resources

    @property
    def sync_statuses(self):
        """Gets the sync_statuses of this V1Plugins.  # noqa: E501


        :return: The sync_statuses of this V1Plugins.  # noqa: E501
        :rtype: bool
        """
        return self._sync_statuses

    @sync_statuses.setter
    def sync_statuses(self, sync_statuses):
        """Sets the sync_statuses of this V1Plugins.


        :param sync_statuses: The sync_statuses of this V1Plugins.  # noqa: E501
        :type: bool
        """

        self._sync_statuses = sync_statuses

    @property
    def auto_resume(self):
        """Gets the auto_resume of this V1Plugins.  # noqa: E501


        :return: The auto_resume of this V1Plugins.  # noqa: E501
        :rtype: bool
        """
        return self._auto_resume

    @auto_resume.setter
    def auto_resume(self, auto_resume):
        """Sets the auto_resume of this V1Plugins.


        :param auto_resume: The auto_resume of this V1Plugins.  # noqa: E501
        :type: bool
        """

        self._auto_resume = auto_resume

    @property
    def log_level(self):
        """Gets the log_level of this V1Plugins.  # noqa: E501


        :return: The log_level of this V1Plugins.  # noqa: E501
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this V1Plugins.


        :param log_level: The log_level of this V1Plugins.  # noqa: E501
        :type: str
        """

        self._log_level = log_level

    @property
    def external_host(self):
        """Gets the external_host of this V1Plugins.  # noqa: E501


        :return: The external_host of this V1Plugins.  # noqa: E501
        :rtype: bool
        """
        return self._external_host

    @external_host.setter
    def external_host(self, external_host):
        """Sets the external_host of this V1Plugins.


        :param external_host: The external_host of this V1Plugins.  # noqa: E501
        :type: bool
        """

        self._external_host = external_host

    @property
    def sidecar(self):
        """Gets the sidecar of this V1Plugins.  # noqa: E501


        :return: The sidecar of this V1Plugins.  # noqa: E501
        :rtype: V1PolyaxonSidecarContainer
        """
        return self._sidecar

    @sidecar.setter
    def sidecar(self, sidecar):
        """Sets the sidecar of this V1Plugins.


        :param sidecar: The sidecar of this V1Plugins.  # noqa: E501
        :type: V1PolyaxonSidecarContainer
        """

        self._sidecar = sidecar

    @property
    def notifications(self):
        """Gets the notifications of this V1Plugins.  # noqa: E501


        :return: The notifications of this V1Plugins.  # noqa: E501
        :rtype: list[V1Notification]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this V1Plugins.


        :param notifications: The notifications of this V1Plugins.  # noqa: E501
        :type: list[V1Notification]
        """

        self._notifications = notifications

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
        if not isinstance(other, V1Plugins):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Plugins):
            return True

        return self.to_dict() != other.to_dict()
