# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .app import *
from .binding import *
from .certificate import *
from .custom_domain import *
from .deployment import *
from .get_app import *
from .get_app_resource_upload_url import *
from .get_binding import *
from .get_certificate import *
from .get_custom_domain import *
from .get_deployment import *
from .get_deployment_log_file_url import *
from .get_service import *
from .list_service_test_keys import *
from .service import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.appplatform.v20190501preview as v20190501preview
    import pulumi_azure_native.appplatform.v20200701 as v20200701
    import pulumi_azure_native.appplatform.v20201101preview as v20201101preview
    import pulumi_azure_native.appplatform.v20210601preview as v20210601preview
else:
    v20190501preview = _utilities.lazy_import('pulumi_azure_native.appplatform.v20190501preview')
    v20200701 = _utilities.lazy_import('pulumi_azure_native.appplatform.v20200701')
    v20201101preview = _utilities.lazy_import('pulumi_azure_native.appplatform.v20201101preview')
    v20210601preview = _utilities.lazy_import('pulumi_azure_native.appplatform.v20210601preview')

