# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .domain_service import *
from .get_domain_service import *
from .get_ou_container import *
from .ou_container import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.aad.v20170101 as v20170101
    import pulumi_azure_native.aad.v20170601 as v20170601
    import pulumi_azure_native.aad.v20200101 as v20200101
    import pulumi_azure_native.aad.v20210301 as v20210301
    import pulumi_azure_native.aad.v20210501 as v20210501
else:
    v20170101 = _utilities.lazy_import('pulumi_azure_native.aad.v20170101')
    v20170601 = _utilities.lazy_import('pulumi_azure_native.aad.v20170601')
    v20200101 = _utilities.lazy_import('pulumi_azure_native.aad.v20200101')
    v20210301 = _utilities.lazy_import('pulumi_azure_native.aad.v20210301')
    v20210501 = _utilities.lazy_import('pulumi_azure_native.aad.v20210501')

