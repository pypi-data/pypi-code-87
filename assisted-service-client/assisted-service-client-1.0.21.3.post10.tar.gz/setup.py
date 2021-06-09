
import setuptools

setuptools.setup(
    name="assisted-service-client",
    description="AssistedInstall",
    setup_requires=['vcversioner'],
    vcversioner={'vcs_args': ['git', 'describe', '--tags', '--long']},
    author="RedHat",
    author_email="UNKNOWN",
    url="https://github.com/openshift/assisted-service",
    keywords=['Swagger', 'AssistedInstall'],
    install_requires=['certifi>=2017.4.17', 'python-dateutil>=2.1', 'six>=1.10', 'urllib3>=1.23'],
    packages=['assisted_service_client', 'test', 'assisted_service_client.models', 'assisted_service_client.api'],
    include_package_data=True,    
    python_requires='>=3.6',
    long_description='''
    # assisted-service-client
Assisted installation

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install assisted-service-client
```
(you may need to run `pip` with root permission: `sudo pip install assisted-service-client`)

Then import the package:
```python
import assisted_service_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import assisted_service_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import assisted_service_client
from assisted_service_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: userAuth
configuration = assisted_service_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = assisted_service_client.AssistedServiceIsoApi(assisted_service_client.ApiClient(configuration))
assisted_service_iso_create_params = assisted_service_client.AssistedServiceIsoCreateParams() # AssistedServiceIsoCreateParams | Parameters for creating an Assisted Service ISO.

try:
    api_instance.create_iso_and_upload_to_s3(assisted_service_iso_create_params)
except ApiException as e:
    print("Exception when calling AssistedServiceIsoApi->create_iso_and_upload_to_s3: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://api.openshift.com/api/assisted-install/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AssistedServiceIsoApi* | [**create_iso_and_upload_to_s3**](docs/AssistedServiceIsoApi.md#create_iso_and_upload_to_s3) | **POST** /assisted-service-iso | 
*AssistedServiceIsoApi* | [**download_iso**](docs/AssistedServiceIsoApi.md#download_iso) | **GET** /assisted-service-iso/data | 
*AssistedServiceIsoApi* | [**get_presigned_for_assisted_service_iso**](docs/AssistedServiceIsoApi.md#get_presigned_for_assisted_service_iso) | **GET** /assisted-service-iso/presigned | 
*EventsApi* | [**list_events**](docs/EventsApi.md#list_events) | **GET** /clusters/{cluster_id}/events | 
*InstallerApi* | [**cancel_installation**](docs/InstallerApi.md#cancel_installation) | **POST** /clusters/{cluster_id}/actions/cancel | 
*InstallerApi* | [**complete_installation**](docs/InstallerApi.md#complete_installation) | **POST** /clusters/{cluster_id}/actions/complete_installation | 
*InstallerApi* | [**deregister_cluster**](docs/InstallerApi.md#deregister_cluster) | **DELETE** /clusters/{cluster_id} | 
*InstallerApi* | [**deregister_host**](docs/InstallerApi.md#deregister_host) | **DELETE** /clusters/{cluster_id}/hosts/{host_id} | 
*InstallerApi* | [**disable_host**](docs/InstallerApi.md#disable_host) | **DELETE** /clusters/{cluster_id}/hosts/{host_id}/actions/enable | 
*InstallerApi* | [**download_cluster_files**](docs/InstallerApi.md#download_cluster_files) | **GET** /clusters/{cluster_id}/downloads/files | 
*InstallerApi* | [**download_cluster_iso**](docs/InstallerApi.md#download_cluster_iso) | **GET** /clusters/{cluster_id}/downloads/image | 
*InstallerApi* | [**download_cluster_iso_headers**](docs/InstallerApi.md#download_cluster_iso_headers) | **HEAD** /clusters/{cluster_id}/downloads/image | 
*InstallerApi* | [**download_cluster_kubeconfig**](docs/InstallerApi.md#download_cluster_kubeconfig) | **GET** /clusters/{cluster_id}/downloads/kubeconfig | 
*InstallerApi* | [**download_cluster_logs**](docs/InstallerApi.md#download_cluster_logs) | **GET** /clusters/{cluster_id}/logs | 
*InstallerApi* | [**download_host_ignition**](docs/InstallerApi.md#download_host_ignition) | **GET** /clusters/{cluster_id}/hosts/{host_id}/downloads/ignition | 
*InstallerApi* | [**download_host_logs**](docs/InstallerApi.md#download_host_logs) | **GET** /clusters/{cluster_id}/hosts/{host_id}/logs | 
*InstallerApi* | [**enable_host**](docs/InstallerApi.md#enable_host) | **POST** /clusters/{cluster_id}/hosts/{host_id}/actions/enable | 
*InstallerApi* | [**generate_cluster_iso**](docs/InstallerApi.md#generate_cluster_iso) | **POST** /clusters/{cluster_id}/downloads/image | 
*InstallerApi* | [**get_cluster**](docs/InstallerApi.md#get_cluster) | **GET** /clusters/{cluster_id} | 
*InstallerApi* | [**get_cluster_default_config**](docs/InstallerApi.md#get_cluster_default_config) | **GET** /clusters/default-config | 
*InstallerApi* | [**get_cluster_host_requirements**](docs/InstallerApi.md#get_cluster_host_requirements) | **GET** /clusters/{cluster_id}/host-requirements | 
*InstallerApi* | [**get_cluster_install_config**](docs/InstallerApi.md#get_cluster_install_config) | **GET** /clusters/{cluster_id}/install-config | 
*InstallerApi* | [**get_credentials**](docs/InstallerApi.md#get_credentials) | **GET** /clusters/{cluster_id}/credentials | 
*InstallerApi* | [**get_discovery_ignition**](docs/InstallerApi.md#get_discovery_ignition) | **GET** /clusters/{cluster_id}/discovery-ignition | 
*InstallerApi* | [**get_free_addresses**](docs/InstallerApi.md#get_free_addresses) | **GET** /clusters/{cluster_id}/free_addresses | 
*InstallerApi* | [**get_host**](docs/InstallerApi.md#get_host) | **GET** /clusters/{cluster_id}/hosts/{host_id} | 
*InstallerApi* | [**get_host_ignition**](docs/InstallerApi.md#get_host_ignition) | **GET** /clusters/{cluster_id}/hosts/{host_id}/ignition | 
*InstallerApi* | [**get_host_requirements**](docs/InstallerApi.md#get_host_requirements) | **GET** /host_requirements | 
*InstallerApi* | [**get_next_steps**](docs/InstallerApi.md#get_next_steps) | **GET** /clusters/{cluster_id}/hosts/{host_id}/instructions | 
*InstallerApi* | [**get_preflight_requirements**](docs/InstallerApi.md#get_preflight_requirements) | **GET** /clusters/{cluster_id}/preflight-requirements | 
*InstallerApi* | [**get_presigned_for_cluster_files**](docs/InstallerApi.md#get_presigned_for_cluster_files) | **GET** /clusters/{cluster_id}/downloads/files-presigned | 
*InstallerApi* | [**install_cluster**](docs/InstallerApi.md#install_cluster) | **POST** /clusters/{cluster_id}/actions/install | 
*InstallerApi* | [**install_host**](docs/InstallerApi.md#install_host) | **POST** /clusters/{cluster_id}/hosts/{host_id}/actions/install | 
*InstallerApi* | [**install_hosts**](docs/InstallerApi.md#install_hosts) | **POST** /clusters/{cluster_id}/actions/install_hosts | 
*InstallerApi* | [**list_clusters**](docs/InstallerApi.md#list_clusters) | **GET** /clusters | 
*InstallerApi* | [**list_hosts**](docs/InstallerApi.md#list_hosts) | **GET** /clusters/{cluster_id}/hosts | 
*InstallerApi* | [**list_of_cluster_operators**](docs/InstallerApi.md#list_of_cluster_operators) | **GET** /clusters/{cluster_id}/monitored_operators | 
*InstallerApi* | [**post_step_reply**](docs/InstallerApi.md#post_step_reply) | **POST** /clusters/{cluster_id}/hosts/{host_id}/instructions | 
*InstallerApi* | [**register_add_hosts_cluster**](docs/InstallerApi.md#register_add_hosts_cluster) | **POST** /add_hosts_clusters | 
*InstallerApi* | [**register_cluster**](docs/InstallerApi.md#register_cluster) | **POST** /clusters | 
*InstallerApi* | [**register_host**](docs/InstallerApi.md#register_host) | **POST** /clusters/{cluster_id}/hosts | 
*InstallerApi* | [**report_monitored_operator_status**](docs/InstallerApi.md#report_monitored_operator_status) | **PUT** /clusters/{cluster_id}/monitored_operators | 
*InstallerApi* | [**reset_cluster**](docs/InstallerApi.md#reset_cluster) | **POST** /clusters/{cluster_id}/actions/reset | 
*InstallerApi* | [**reset_host**](docs/InstallerApi.md#reset_host) | **POST** /clusters/{cluster_id}/hosts/{host_id}/actions/reset | 
*InstallerApi* | [**reset_host_validation**](docs/InstallerApi.md#reset_host_validation) | **PATCH** /clusters/{cluster_id}/hosts/{host_id}/actions/reset-validation/{validation_id} | Reset failed host validation.
*InstallerApi* | [**update_cluster**](docs/InstallerApi.md#update_cluster) | **PATCH** /clusters/{cluster_id} | 
*InstallerApi* | [**update_cluster_install_config**](docs/InstallerApi.md#update_cluster_install_config) | **PATCH** /clusters/{cluster_id}/install-config | 
*InstallerApi* | [**update_cluster_logs_progress**](docs/InstallerApi.md#update_cluster_logs_progress) | **PUT** /clusters/{cluster_id}/logs_progress | 
*InstallerApi* | [**update_discovery_ignition**](docs/InstallerApi.md#update_discovery_ignition) | **PATCH** /clusters/{cluster_id}/discovery-ignition | 
*InstallerApi* | [**update_host_ignition**](docs/InstallerApi.md#update_host_ignition) | **PATCH** /clusters/{cluster_id}/hosts/{host_id}/ignition | 
*InstallerApi* | [**update_host_install_progress**](docs/InstallerApi.md#update_host_install_progress) | **PUT** /clusters/{cluster_id}/hosts/{host_id}/progress | 
*InstallerApi* | [**update_host_installer_args**](docs/InstallerApi.md#update_host_installer_args) | **PATCH** /clusters/{cluster_id}/hosts/{host_id}/installer-args | 
*InstallerApi* | [**update_host_logs_progress**](docs/InstallerApi.md#update_host_logs_progress) | **PUT** /clusters/{cluster_id}/hosts/{host_id}/logs_progress | 
*InstallerApi* | [**upload_cluster_ingress_cert**](docs/InstallerApi.md#upload_cluster_ingress_cert) | **POST** /clusters/{cluster_id}/uploads/ingress-cert | 
*InstallerApi* | [**upload_host_logs**](docs/InstallerApi.md#upload_host_logs) | **POST** /clusters/{cluster_id}/hosts/{host_id}/logs | 
*InstallerApi* | [**upload_logs**](docs/InstallerApi.md#upload_logs) | **POST** /clusters/{cluster_id}/logs | 
*ManagedDomainsApi* | [**list_managed_domains**](docs/ManagedDomainsApi.md#list_managed_domains) | **GET** /domains | 
*ManifestsApi* | [**create_cluster_manifest**](docs/ManifestsApi.md#create_cluster_manifest) | **POST** /clusters/{cluster_id}/manifests | 
*ManifestsApi* | [**delete_cluster_manifest**](docs/ManifestsApi.md#delete_cluster_manifest) | **DELETE** /clusters/{cluster_id}/manifests | 
*ManifestsApi* | [**download_cluster_manifest**](docs/ManifestsApi.md#download_cluster_manifest) | **GET** /clusters/{cluster_id}/manifests/files | 
*ManifestsApi* | [**list_cluster_manifests**](docs/ManifestsApi.md#list_cluster_manifests) | **GET** /clusters/{cluster_id}/manifests | 
*OperatorsApi* | [**list_of_cluster_operators**](docs/OperatorsApi.md#list_of_cluster_operators) | **GET** /clusters/{cluster_id}/monitored_operators | 
*OperatorsApi* | [**list_operator_properties**](docs/OperatorsApi.md#list_operator_properties) | **GET** /supported-operators/{operator_name} | 
*OperatorsApi* | [**list_supported_operators**](docs/OperatorsApi.md#list_supported_operators) | **GET** /supported-operators | 
*OperatorsApi* | [**report_monitored_operator_status**](docs/OperatorsApi.md#report_monitored_operator_status) | **PUT** /clusters/{cluster_id}/monitored_operators | 
*VersionsApi* | [**list_component_versions**](docs/VersionsApi.md#list_component_versions) | **GET** /component_versions | 
*VersionsApi* | [**list_supported_openshift_versions**](docs/VersionsApi.md#list_supported_openshift_versions) | **GET** /openshift_versions | 


## Documentation For Models

 - [AddHostsClusterCreateParams](docs/AddHostsClusterCreateParams.md)
 - [ApiVipConnectivityRequest](docs/ApiVipConnectivityRequest.md)
 - [ApiVipConnectivityResponse](docs/ApiVipConnectivityResponse.md)
 - [AssistedServiceIsoCreateParams](docs/AssistedServiceIsoCreateParams.md)
 - [Boot](docs/Boot.md)
 - [Cluster](docs/Cluster.md)
 - [ClusterCreateParams](docs/ClusterCreateParams.md)
 - [ClusterDefaultConfig](docs/ClusterDefaultConfig.md)
 - [ClusterHostRequirements](docs/ClusterHostRequirements.md)
 - [ClusterHostRequirementsDetails](docs/ClusterHostRequirementsDetails.md)
 - [ClusterHostRequirementsList](docs/ClusterHostRequirementsList.md)
 - [ClusterList](docs/ClusterList.md)
 - [ClusterUpdateParams](docs/ClusterUpdateParams.md)
 - [ClusterValidationId](docs/ClusterValidationId.md)
 - [ClusterupdateparamsDisksSelectedConfig](docs/ClusterupdateparamsDisksSelectedConfig.md)
 - [ClusterupdateparamsHostsMachineConfigPoolNames](docs/ClusterupdateparamsHostsMachineConfigPoolNames.md)
 - [ClusterupdateparamsHostsNames](docs/ClusterupdateparamsHostsNames.md)
 - [ClusterupdateparamsHostsRoles](docs/ClusterupdateparamsHostsRoles.md)
 - [CompletionParams](docs/CompletionParams.md)
 - [ConnectivityCheckHost](docs/ConnectivityCheckHost.md)
 - [ConnectivityCheckNic](docs/ConnectivityCheckNic.md)
 - [ConnectivityCheckParams](docs/ConnectivityCheckParams.md)
 - [ConnectivityRemoteHost](docs/ConnectivityRemoteHost.md)
 - [ConnectivityReport](docs/ConnectivityReport.md)
 - [ContainerImageAvailability](docs/ContainerImageAvailability.md)
 - [ContainerImageAvailabilityRequest](docs/ContainerImageAvailabilityRequest.md)
 - [ContainerImageAvailabilityResponse](docs/ContainerImageAvailabilityResponse.md)
 - [ContainerImageAvailabilityResult](docs/ContainerImageAvailabilityResult.md)
 - [Cpu](docs/Cpu.md)
 - [CreateManifestParams](docs/CreateManifestParams.md)
 - [Credentials](docs/Credentials.md)
 - [DhcpAllocationRequest](docs/DhcpAllocationRequest.md)
 - [DhcpAllocationResponse](docs/DhcpAllocationResponse.md)
 - [DiscoveryIgnitionParams](docs/DiscoveryIgnitionParams.md)
 - [Disk](docs/Disk.md)
 - [DiskConfigParams](docs/DiskConfigParams.md)
 - [DiskInfo](docs/DiskInfo.md)
 - [DiskInstallationEligibility](docs/DiskInstallationEligibility.md)
 - [DiskRole](docs/DiskRole.md)
 - [DiskSpeed](docs/DiskSpeed.md)
 - [DiskSpeedCheckRequest](docs/DiskSpeedCheckRequest.md)
 - [DiskSpeedCheckResponse](docs/DiskSpeedCheckResponse.md)
 - [DomainResolutionRequest](docs/DomainResolutionRequest.md)
 - [DomainResolutionRequestDomains](docs/DomainResolutionRequestDomains.md)
 - [DomainResolutionResponse](docs/DomainResolutionResponse.md)
 - [DomainResolutionResponseResolutions](docs/DomainResolutionResponseResolutions.md)
 - [Error](docs/Error.md)
 - [Event](docs/Event.md)
 - [EventList](docs/EventList.md)
 - [FreeAddressesList](docs/FreeAddressesList.md)
 - [FreeAddressesRequest](docs/FreeAddressesRequest.md)
 - [FreeNetworkAddresses](docs/FreeNetworkAddresses.md)
 - [FreeNetworksAddresses](docs/FreeNetworksAddresses.md)
 - [Gpu](docs/Gpu.md)
 - [Host](docs/Host.md)
 - [HostCreateParams](docs/HostCreateParams.md)
 - [HostIgnitionParams](docs/HostIgnitionParams.md)
 - [HostList](docs/HostList.md)
 - [HostNetwork](docs/HostNetwork.md)
 - [HostProgress](docs/HostProgress.md)
 - [HostProgressInfo](docs/HostProgressInfo.md)
 - [HostRegistrationResponse](docs/HostRegistrationResponse.md)
 - [HostRegistrationResponseNextStepRunnerCommand](docs/HostRegistrationResponseNextStepRunnerCommand.md)
 - [HostRequirements](docs/HostRequirements.md)
 - [HostRequirementsRole](docs/HostRequirementsRole.md)
 - [HostRole](docs/HostRole.md)
 - [HostRoleUpdateParams](docs/HostRoleUpdateParams.md)
 - [HostStage](docs/HostStage.md)
 - [HostStaticNetworkConfig](docs/HostStaticNetworkConfig.md)
 - [HostTypeHardwareRequirements](docs/HostTypeHardwareRequirements.md)
 - [HostTypeHardwareRequirementsWrapper](docs/HostTypeHardwareRequirementsWrapper.md)
 - [HostValidationId](docs/HostValidationId.md)
 - [ImageCreateParams](docs/ImageCreateParams.md)
 - [ImageInfo](docs/ImageInfo.md)
 - [ImageType](docs/ImageType.md)
 - [InfraError](docs/InfraError.md)
 - [IngressCertParams](docs/IngressCertParams.md)
 - [InstallerArgsParams](docs/InstallerArgsParams.md)
 - [Interface](docs/Interface.md)
 - [Inventory](docs/Inventory.md)
 - [IoPerf](docs/IoPerf.md)
 - [L2Connectivity](docs/L2Connectivity.md)
 - [L3Connectivity](docs/L3Connectivity.md)
 - [ListManagedDomains](docs/ListManagedDomains.md)
 - [ListManifests](docs/ListManifests.md)
 - [ListVersions](docs/ListVersions.md)
 - [LogsProgressParams](docs/LogsProgressParams.md)
 - [LogsState](docs/LogsState.md)
 - [LogsType](docs/LogsType.md)
 - [MacInterfaceMap](docs/MacInterfaceMap.md)
 - [MacInterfaceMapInner](docs/MacInterfaceMapInner.md)
 - [ManagedDomain](docs/ManagedDomain.md)
 - [Manifest](docs/Manifest.md)
 - [Memory](docs/Memory.md)
 - [MonitoredOperator](docs/MonitoredOperator.md)
 - [MonitoredOperatorsList](docs/MonitoredOperatorsList.md)
 - [NtpSource](docs/NtpSource.md)
 - [NtpSynchronizationRequest](docs/NtpSynchronizationRequest.md)
 - [NtpSynchronizationResponse](docs/NtpSynchronizationResponse.md)
 - [OpenshiftVersion](docs/OpenshiftVersion.md)
 - [OpenshiftVersions](docs/OpenshiftVersions.md)
 - [OperatorCreateParams](docs/OperatorCreateParams.md)
 - [OperatorHardwareRequirements](docs/OperatorHardwareRequirements.md)
 - [OperatorHostRequirements](docs/OperatorHostRequirements.md)
 - [OperatorMonitorReport](docs/OperatorMonitorReport.md)
 - [OperatorProperties](docs/OperatorProperties.md)
 - [OperatorProperty](docs/OperatorProperty.md)
 - [OperatorStatus](docs/OperatorStatus.md)
 - [OperatorType](docs/OperatorType.md)
 - [PreflightHardwareRequirements](docs/PreflightHardwareRequirements.md)
 - [Presigned](docs/Presigned.md)
 - [Route](docs/Route.md)
 - [SourceState](docs/SourceState.md)
 - [Step](docs/Step.md)
 - [StepReply](docs/StepReply.md)
 - [StepType](docs/StepType.md)
 - [Steps](docs/Steps.md)
 - [StepsReply](docs/StepsReply.md)
 - [SystemVendor](docs/SystemVendor.md)
 - [Usage](docs/Usage.md)
 - [VersionedHostRequirements](docs/VersionedHostRequirements.md)
 - [Versions](docs/Versions.md)


## Documentation For Authorization


## agentAuth

- **Type**: API key
- **API key parameter name**: X-Secret-Key
- **Location**: HTTP header

## urlAuth

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string

## userAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



''',
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
