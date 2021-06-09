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


class DecoratedComputeTemplateConfig(object):
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
        'cloud_id': 'str',
        'max_workers': 'int',
        'region': 'str',
        'allowed_azs': 'list[str]',
        'head_node_type': 'ComputeNodeType',
        'worker_node_types': 'list[WorkerNodeType]',
        'aws': 'AWSNodeOptions',
        'gcp': 'object',
        'azure': 'object',
        'cloud': 'MiniCloud'
    }

    attribute_map = {
        'cloud_id': 'cloud_id',
        'max_workers': 'max_workers',
        'region': 'region',
        'allowed_azs': 'allowed_azs',
        'head_node_type': 'head_node_type',
        'worker_node_types': 'worker_node_types',
        'aws': 'aws',
        'gcp': 'gcp',
        'azure': 'azure',
        'cloud': 'cloud'
    }

    def __init__(self, cloud_id=None, max_workers=None, region=None, allowed_azs=None, head_node_type=None, worker_node_types=None, aws=None, gcp=None, azure=None, cloud=None, local_vars_configuration=None):  # noqa: E501
        """DecoratedComputeTemplateConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_id = None
        self._max_workers = None
        self._region = None
        self._allowed_azs = None
        self._head_node_type = None
        self._worker_node_types = None
        self._aws = None
        self._gcp = None
        self._azure = None
        self._cloud = None
        self.discriminator = None

        self.cloud_id = cloud_id
        if max_workers is not None:
            self.max_workers = max_workers
        self.region = region
        if allowed_azs is not None:
            self.allowed_azs = allowed_azs
        self.head_node_type = head_node_type
        self.worker_node_types = worker_node_types
        if aws is not None:
            self.aws = aws
        if gcp is not None:
            self.gcp = gcp
        if azure is not None:
            self.azure = azure
        self.cloud = cloud

    @property
    def cloud_id(self):
        """Gets the cloud_id of this DecoratedComputeTemplateConfig.  # noqa: E501

        The ID of the Anyscale cloud to use for launching sessions.  # noqa: E501

        :return: The cloud_id of this DecoratedComputeTemplateConfig.  # noqa: E501
        :rtype: str
        """
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, cloud_id):
        """Sets the cloud_id of this DecoratedComputeTemplateConfig.

        The ID of the Anyscale cloud to use for launching sessions.  # noqa: E501

        :param cloud_id: The cloud_id of this DecoratedComputeTemplateConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cloud_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cloud_id`, must not be `None`")  # noqa: E501

        self._cloud_id = cloud_id

    @property
    def max_workers(self):
        """Gets the max_workers of this DecoratedComputeTemplateConfig.  # noqa: E501

        Desired limit on total running workers for this session.  # noqa: E501

        :return: The max_workers of this DecoratedComputeTemplateConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_workers

    @max_workers.setter
    def max_workers(self, max_workers):
        """Sets the max_workers of this DecoratedComputeTemplateConfig.

        Desired limit on total running workers for this session.  # noqa: E501

        :param max_workers: The max_workers of this DecoratedComputeTemplateConfig.  # noqa: E501
        :type: int
        """

        self._max_workers = max_workers

    @property
    def region(self):
        """Gets the region of this DecoratedComputeTemplateConfig.  # noqa: E501

        The region to launch sessions in, e.g. \"us-west-2\".  # noqa: E501

        :return: The region of this DecoratedComputeTemplateConfig.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DecoratedComputeTemplateConfig.

        The region to launch sessions in, e.g. \"us-west-2\".  # noqa: E501

        :param region: The region of this DecoratedComputeTemplateConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and region is None:  # noqa: E501
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def allowed_azs(self):
        """Gets the allowed_azs of this DecoratedComputeTemplateConfig.  # noqa: E501

        The availability zones that sessions are allowed to be launched in, e.g. \"us-west-2a\". If not specified, any AZ may be used.  # noqa: E501

        :return: The allowed_azs of this DecoratedComputeTemplateConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_azs

    @allowed_azs.setter
    def allowed_azs(self, allowed_azs):
        """Sets the allowed_azs of this DecoratedComputeTemplateConfig.

        The availability zones that sessions are allowed to be launched in, e.g. \"us-west-2a\". If not specified, any AZ may be used.  # noqa: E501

        :param allowed_azs: The allowed_azs of this DecoratedComputeTemplateConfig.  # noqa: E501
        :type: list[str]
        """

        self._allowed_azs = allowed_azs

    @property
    def head_node_type(self):
        """Gets the head_node_type of this DecoratedComputeTemplateConfig.  # noqa: E501

        Node configuration to use for the head node.   # noqa: E501

        :return: The head_node_type of this DecoratedComputeTemplateConfig.  # noqa: E501
        :rtype: ComputeNodeType
        """
        return self._head_node_type

    @head_node_type.setter
    def head_node_type(self, head_node_type):
        """Sets the head_node_type of this DecoratedComputeTemplateConfig.

        Node configuration to use for the head node.   # noqa: E501

        :param head_node_type: The head_node_type of this DecoratedComputeTemplateConfig.  # noqa: E501
        :type: ComputeNodeType
        """
        if self.local_vars_configuration.client_side_validation and head_node_type is None:  # noqa: E501
            raise ValueError("Invalid value for `head_node_type`, must not be `None`")  # noqa: E501

        self._head_node_type = head_node_type

    @property
    def worker_node_types(self):
        """Gets the worker_node_types of this DecoratedComputeTemplateConfig.  # noqa: E501

        A list of node types to use for worker nodes.   # noqa: E501

        :return: The worker_node_types of this DecoratedComputeTemplateConfig.  # noqa: E501
        :rtype: list[WorkerNodeType]
        """
        return self._worker_node_types

    @worker_node_types.setter
    def worker_node_types(self, worker_node_types):
        """Sets the worker_node_types of this DecoratedComputeTemplateConfig.

        A list of node types to use for worker nodes.   # noqa: E501

        :param worker_node_types: The worker_node_types of this DecoratedComputeTemplateConfig.  # noqa: E501
        :type: list[WorkerNodeType]
        """
        if self.local_vars_configuration.client_side_validation and worker_node_types is None:  # noqa: E501
            raise ValueError("Invalid value for `worker_node_types`, must not be `None`")  # noqa: E501

        self._worker_node_types = worker_node_types

    @property
    def aws(self):
        """Gets the aws of this DecoratedComputeTemplateConfig.  # noqa: E501

        Fields specific to AWS node types.  # noqa: E501

        :return: The aws of this DecoratedComputeTemplateConfig.  # noqa: E501
        :rtype: AWSNodeOptions
        """
        return self._aws

    @aws.setter
    def aws(self, aws):
        """Sets the aws of this DecoratedComputeTemplateConfig.

        Fields specific to AWS node types.  # noqa: E501

        :param aws: The aws of this DecoratedComputeTemplateConfig.  # noqa: E501
        :type: AWSNodeOptions
        """

        self._aws = aws

    @property
    def gcp(self):
        """Gets the gcp of this DecoratedComputeTemplateConfig.  # noqa: E501

        Fields specific to GCP node types.  # noqa: E501

        :return: The gcp of this DecoratedComputeTemplateConfig.  # noqa: E501
        :rtype: object
        """
        return self._gcp

    @gcp.setter
    def gcp(self, gcp):
        """Sets the gcp of this DecoratedComputeTemplateConfig.

        Fields specific to GCP node types.  # noqa: E501

        :param gcp: The gcp of this DecoratedComputeTemplateConfig.  # noqa: E501
        :type: object
        """

        self._gcp = gcp

    @property
    def azure(self):
        """Gets the azure of this DecoratedComputeTemplateConfig.  # noqa: E501

        Fields specific to Azure node types.  # noqa: E501

        :return: The azure of this DecoratedComputeTemplateConfig.  # noqa: E501
        :rtype: object
        """
        return self._azure

    @azure.setter
    def azure(self, azure):
        """Sets the azure of this DecoratedComputeTemplateConfig.

        Fields specific to Azure node types.  # noqa: E501

        :param azure: The azure of this DecoratedComputeTemplateConfig.  # noqa: E501
        :type: object
        """

        self._azure = azure

    @property
    def cloud(self):
        """Gets the cloud of this DecoratedComputeTemplateConfig.  # noqa: E501

        The decorated cloud_id  # noqa: E501

        :return: The cloud of this DecoratedComputeTemplateConfig.  # noqa: E501
        :rtype: MiniCloud
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this DecoratedComputeTemplateConfig.

        The decorated cloud_id  # noqa: E501

        :param cloud: The cloud of this DecoratedComputeTemplateConfig.  # noqa: E501
        :type: MiniCloud
        """
        if self.local_vars_configuration.client_side_validation and cloud is None:  # noqa: E501
            raise ValueError("Invalid value for `cloud`, must not be `None`")  # noqa: E501

        self._cloud = cloud

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
        if not isinstance(other, DecoratedComputeTemplateConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DecoratedComputeTemplateConfig):
            return True

        return self.to_dict() != other.to_dict()
