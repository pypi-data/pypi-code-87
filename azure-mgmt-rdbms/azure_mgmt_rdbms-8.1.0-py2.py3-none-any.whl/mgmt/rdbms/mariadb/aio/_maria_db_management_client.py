# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import MariaDBManagementClientConfiguration
from .operations import ServersOperations
from .operations import ReplicasOperations
from .operations import FirewallRulesOperations
from .operations import VirtualNetworkRulesOperations
from .operations import DatabasesOperations
from .operations import ConfigurationsOperations
from .operations import ServerParametersOperations
from .operations import LogFilesOperations
from .operations import RecoverableServersOperations
from .operations import ServerBasedPerformanceTierOperations
from .operations import LocationBasedPerformanceTierOperations
from .operations import CheckNameAvailabilityOperations
from .operations import Operations
from .operations import QueryTextsOperations
from .operations import TopQueryStatisticsOperations
from .operations import WaitStatisticsOperations
from .operations import MariaDBManagementClientOperationsMixin
from .operations import AdvisorsOperations
from .operations import RecommendedActionsOperations
from .operations import LocationBasedRecommendedActionSessionsOperationStatusOperations
from .operations import LocationBasedRecommendedActionSessionsResultOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import ServerSecurityAlertPoliciesOperations
from .. import models


class MariaDBManagementClient(MariaDBManagementClientOperationsMixin):
    """The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MariaDB resources including servers, databases, firewall rules, VNET rules, log files and configurations with new business model.

    :ivar servers: ServersOperations operations
    :vartype servers: azure.mgmt.rdbms.mariadb.aio.operations.ServersOperations
    :ivar replicas: ReplicasOperations operations
    :vartype replicas: azure.mgmt.rdbms.mariadb.aio.operations.ReplicasOperations
    :ivar firewall_rules: FirewallRulesOperations operations
    :vartype firewall_rules: azure.mgmt.rdbms.mariadb.aio.operations.FirewallRulesOperations
    :ivar virtual_network_rules: VirtualNetworkRulesOperations operations
    :vartype virtual_network_rules: azure.mgmt.rdbms.mariadb.aio.operations.VirtualNetworkRulesOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: azure.mgmt.rdbms.mariadb.aio.operations.DatabasesOperations
    :ivar configurations: ConfigurationsOperations operations
    :vartype configurations: azure.mgmt.rdbms.mariadb.aio.operations.ConfigurationsOperations
    :ivar server_parameters: ServerParametersOperations operations
    :vartype server_parameters: azure.mgmt.rdbms.mariadb.aio.operations.ServerParametersOperations
    :ivar log_files: LogFilesOperations operations
    :vartype log_files: azure.mgmt.rdbms.mariadb.aio.operations.LogFilesOperations
    :ivar recoverable_servers: RecoverableServersOperations operations
    :vartype recoverable_servers: azure.mgmt.rdbms.mariadb.aio.operations.RecoverableServersOperations
    :ivar server_based_performance_tier: ServerBasedPerformanceTierOperations operations
    :vartype server_based_performance_tier: azure.mgmt.rdbms.mariadb.aio.operations.ServerBasedPerformanceTierOperations
    :ivar location_based_performance_tier: LocationBasedPerformanceTierOperations operations
    :vartype location_based_performance_tier: azure.mgmt.rdbms.mariadb.aio.operations.LocationBasedPerformanceTierOperations
    :ivar check_name_availability: CheckNameAvailabilityOperations operations
    :vartype check_name_availability: azure.mgmt.rdbms.mariadb.aio.operations.CheckNameAvailabilityOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.rdbms.mariadb.aio.operations.Operations
    :ivar query_texts: QueryTextsOperations operations
    :vartype query_texts: azure.mgmt.rdbms.mariadb.aio.operations.QueryTextsOperations
    :ivar top_query_statistics: TopQueryStatisticsOperations operations
    :vartype top_query_statistics: azure.mgmt.rdbms.mariadb.aio.operations.TopQueryStatisticsOperations
    :ivar wait_statistics: WaitStatisticsOperations operations
    :vartype wait_statistics: azure.mgmt.rdbms.mariadb.aio.operations.WaitStatisticsOperations
    :ivar advisors: AdvisorsOperations operations
    :vartype advisors: azure.mgmt.rdbms.mariadb.aio.operations.AdvisorsOperations
    :ivar recommended_actions: RecommendedActionsOperations operations
    :vartype recommended_actions: azure.mgmt.rdbms.mariadb.aio.operations.RecommendedActionsOperations
    :ivar location_based_recommended_action_sessions_operation_status: LocationBasedRecommendedActionSessionsOperationStatusOperations operations
    :vartype location_based_recommended_action_sessions_operation_status: azure.mgmt.rdbms.mariadb.aio.operations.LocationBasedRecommendedActionSessionsOperationStatusOperations
    :ivar location_based_recommended_action_sessions_result: LocationBasedRecommendedActionSessionsResultOperations operations
    :vartype location_based_recommended_action_sessions_result: azure.mgmt.rdbms.mariadb.aio.operations.LocationBasedRecommendedActionSessionsResultOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.rdbms.mariadb.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.rdbms.mariadb.aio.operations.PrivateLinkResourcesOperations
    :ivar server_security_alert_policies: ServerSecurityAlertPoliciesOperations operations
    :vartype server_security_alert_policies: azure.mgmt.rdbms.mariadb.aio.operations.ServerSecurityAlertPoliciesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MariaDBManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.servers = ServersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replicas = ReplicasOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_rules = VirtualNetworkRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.configurations = ConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_parameters = ServerParametersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.log_files = LogFilesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.recoverable_servers = RecoverableServersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_based_performance_tier = ServerBasedPerformanceTierOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.location_based_performance_tier = LocationBasedPerformanceTierOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.check_name_availability = CheckNameAvailabilityOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.query_texts = QueryTextsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.top_query_statistics = TopQueryStatisticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.wait_statistics = WaitStatisticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.advisors = AdvisorsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.recommended_actions = RecommendedActionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.location_based_recommended_action_sessions_operation_status = LocationBasedRecommendedActionSessionsOperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.location_based_recommended_action_sessions_result = LocationBasedRecommendedActionSessionsResultOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_security_alert_policies = ServerSecurityAlertPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MariaDBManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
