# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CompatibilityLevel',
    'Encoding',
    'EventsOutOfOrderPolicy',
    'JsonOutputSerializationFormat',
    'OutputErrorPolicy',
    'OutputStartMode',
    'SkuName',
]


class CompatibilityLevel(str, Enum):
    """
    Controls certain runtime behaviors of the streaming job.
    """
    COMPATIBILITY_LEVEL_1_0 = "1.0"


class Encoding(str, Enum):
    """
    Specifies the encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. Required on PUT (CreateOrReplace) requests.
    """
    UTF8 = "UTF8"


class EventsOutOfOrderPolicy(str, Enum):
    """
    Indicates the policy to apply to events that arrive out of order in the input event stream.
    """
    ADJUST = "Adjust"
    DROP = "Drop"


class JsonOutputSerializationFormat(str, Enum):
    """
    This property only applies to JSON serialization of outputs only. It is not applicable to inputs. This property specifies the format of the JSON the output will be written in. The currently supported values are 'lineSeparated' indicating the output will be formatted by having each JSON object separated by a new line and 'array' indicating the output will be formatted as an array of JSON objects. Default value is 'lineSeparated' if left null.
    """
    LINE_SEPARATED = "LineSeparated"
    ARRAY = "Array"


class OutputErrorPolicy(str, Enum):
    """
    Indicates the policy to apply to events that arrive at the output and cannot be written to the external storage due to being malformed (missing column values, column values of wrong type or size).
    """
    STOP = "Stop"
    DROP = "Drop"


class OutputStartMode(str, Enum):
    """
    This property should only be utilized when it is desired that the job be started immediately upon creation. Value may be JobStartTime, CustomTime, or LastOutputEventTime to indicate whether the starting point of the output event stream should start whenever the job is started, start at a custom user time stamp specified via the outputStartTime property, or start from the last event output time.
    """
    JOB_START_TIME = "JobStartTime"
    CUSTOM_TIME = "CustomTime"
    LAST_OUTPUT_EVENT_TIME = "LastOutputEventTime"


class SkuName(str, Enum):
    """
    The name of the SKU. Required on PUT (CreateOrReplace) requests.
    """
    STANDARD = "Standard"
