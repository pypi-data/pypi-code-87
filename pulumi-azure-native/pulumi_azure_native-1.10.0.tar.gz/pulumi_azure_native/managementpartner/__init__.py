# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from .get_partner import *
from .partner import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.managementpartner.v20180201 as v20180201
else:
    v20180201 = _utilities.lazy_import('pulumi_azure_native.managementpartner.v20180201')

