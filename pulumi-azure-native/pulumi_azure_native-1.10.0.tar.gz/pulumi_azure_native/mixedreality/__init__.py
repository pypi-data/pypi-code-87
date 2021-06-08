# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .get_object_anchors_account import *
from .get_remote_rendering_account import *
from .get_spatial_anchors_account import *
from .list_object_anchors_account_keys import *
from .list_remote_rendering_account_keys import *
from .list_spatial_anchors_account_keys import *
from .object_anchors_account import *
from .remote_rendering_account import *
from .spatial_anchors_account import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.mixedreality.v20190228preview as v20190228preview
    import pulumi_azure_native.mixedreality.v20191202preview as v20191202preview
    import pulumi_azure_native.mixedreality.v20200406preview as v20200406preview
    import pulumi_azure_native.mixedreality.v20200501 as v20200501
    import pulumi_azure_native.mixedreality.v20210101 as v20210101
    import pulumi_azure_native.mixedreality.v20210301preview as v20210301preview
else:
    v20190228preview = _utilities.lazy_import('pulumi_azure_native.mixedreality.v20190228preview')
    v20191202preview = _utilities.lazy_import('pulumi_azure_native.mixedreality.v20191202preview')
    v20200406preview = _utilities.lazy_import('pulumi_azure_native.mixedreality.v20200406preview')
    v20200501 = _utilities.lazy_import('pulumi_azure_native.mixedreality.v20200501')
    v20210101 = _utilities.lazy_import('pulumi_azure_native.mixedreality.v20210101')
    v20210301preview = _utilities.lazy_import('pulumi_azure_native.mixedreality.v20210301preview')

