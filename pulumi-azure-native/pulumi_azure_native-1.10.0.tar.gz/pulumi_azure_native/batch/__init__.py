# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .application import *
from .application_package import *
from .batch_account import *
from .certificate import *
from .get_application import *
from .get_application_package import *
from .get_batch_account import *
from .get_certificate import *
from .get_pool import *
from .list_batch_account_keys import *
from .pool import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.batch.v20151201 as v20151201
    import pulumi_azure_native.batch.v20170101 as v20170101
    import pulumi_azure_native.batch.v20170501 as v20170501
    import pulumi_azure_native.batch.v20170901 as v20170901
    import pulumi_azure_native.batch.v20181201 as v20181201
    import pulumi_azure_native.batch.v20190401 as v20190401
    import pulumi_azure_native.batch.v20190801 as v20190801
    import pulumi_azure_native.batch.v20200301 as v20200301
    import pulumi_azure_native.batch.v20200501 as v20200501
    import pulumi_azure_native.batch.v20200901 as v20200901
    import pulumi_azure_native.batch.v20210101 as v20210101
else:
    v20151201 = _utilities.lazy_import('pulumi_azure_native.batch.v20151201')
    v20170101 = _utilities.lazy_import('pulumi_azure_native.batch.v20170101')
    v20170501 = _utilities.lazy_import('pulumi_azure_native.batch.v20170501')
    v20170901 = _utilities.lazy_import('pulumi_azure_native.batch.v20170901')
    v20181201 = _utilities.lazy_import('pulumi_azure_native.batch.v20181201')
    v20190401 = _utilities.lazy_import('pulumi_azure_native.batch.v20190401')
    v20190801 = _utilities.lazy_import('pulumi_azure_native.batch.v20190801')
    v20200301 = _utilities.lazy_import('pulumi_azure_native.batch.v20200301')
    v20200501 = _utilities.lazy_import('pulumi_azure_native.batch.v20200501')
    v20200901 = _utilities.lazy_import('pulumi_azure_native.batch.v20200901')
    v20210101 = _utilities.lazy_import('pulumi_azure_native.batch.v20210101')

