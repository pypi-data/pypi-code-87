# Copyright (c) 2021, Apple Inc. All rights reserved.
#
# Use of this source code is governed by a BSD-3-clause license that can be
# found in the LICENSE.txt file or at https://opensource.org/licenses/BSD-3-Clause
import gc
import collections

from coremltools.converters.mil.mil.passes.quantization_passes import AbstractQuantizationPass, FP16ComputePrecision
from coremltools.converters.mil.mil.passes.quantization_passes import ComputePrecision as precision
from coremltools.converters.mil.input_types import InputType, ClassifierConfig
from coremltools.converters.mil.converter import mil_convert
from coremltools.converters.mil.mil import Program
from coremltools._deps import _HAS_TORCH, _HAS_TF_1, _HAS_TF_2
from coremltools.converters._profile_utils import _profile

from coremltools.models import _METADATA_VERSION, _METADATA_SOURCE
from coremltools.converters.mil._deployment_compatibility import (
    AvailableTarget,
    check_deployment_compatibility,
)

if _HAS_TF_1:
    import tensorflow as tf
    from coremltools.converters.mil.frontend.tensorflow.load import TF1Loader
if _HAS_TF_2:
    import tensorflow as tf
    from coremltools.converters.mil.frontend.tensorflow2.load import TF2Loader

if _HAS_TORCH:
    import torch
    from coremltools.converters.mil.frontend.torch.load import (
        _torchscript_from_model as pytorch_load,
    )

@_profile
def convert(
    model,
    source="auto",
    inputs=None,
    outputs=None,
    classifier_config=None,
    minimum_deployment_target=None,
    convert_to=None,
    compute_precision=None,
    **kwargs
):
    """
    Convert TensorFlow or Pytorch models to the Core ML model format. Whether a
    parameter is required may differ between frameworks (see below). Note that
    this function is aliased as `ct.convert` in the tutorials.

    Parameters
    ----------
    model:
        TensorFlow 1, TensorFlow 2 or Pytorch model in one of the following
        formats:

        For TensorFlow versions 1.x:
            - Frozen `tf.Graph <https://www.tensorflow.org/api_docs/python/tf/Graph>`_
            - Frozen graph (``.pb``) file path
            - `tf.keras.Model <https://www.tensorflow.org/api_docs/python/tf/keras>`_
            -  `HDF5 <https://keras.io/api/models/model_saving_apis/>`_ file path (``.h5``)
            - `SavedModel <https://www.tensorflow.org/guide/saved_model>`_ directory path
        For TensorFlow versions 2.x:
            - `tf.keras.Model <https://www.tensorflow.org/api_docs/python/tf/keras>`_
            - `HDF5 file path <https://keras.io/api/models/model_saving_apis/>`_ (``.h5``)
            - `SavedModel <https://www.tensorflow.org/guide/saved_model>`_ directory path
            - A `concrete function <https://www.tensorflow.org/guide/concrete_function>`_
        For Pytorch:
            - A `TorchScript <https://pytorch.org/docs/stable/jit.html>`_ object
            - Path to a ``.pt`` file

    source: str (optional)
        One of [``auto``, ``tensorflow``, ``pytorch``, ``milinternal``]. `auto` determines the
        framework automatically for most cases. Raise ValueError if it fails
        to determine the source framework.

    inputs: list of `TensorType` or `ImageType`
        TensorFlow 1 and 2:
            - ``inputs`` are optional. If not provided, the inputs are
              Placeholder nodes in the model (if model is frozen graph) or
              function inputs (if model is tf function)
            - ``inputs`` must corresponds to all or some of the Placeholder
              nodes in the TF model
            - ``TensorType`` and ``ImageType`` in ``inputs`` must have ``name``
              specified. ``shape`` is optional.
            - If ``inputs`` is provided, it must be a flat list.

        PyTorch:
            - ``inputs`` are required.
            - ``inputs`` may be nested list or tuple.
            - ``TensorType`` and ``ImageType`` in ``inputs`` must have ``name``
              and ``shape`` specified.

    outputs: list[str] (optional)

        TensorFlow 1 and 2:
            - ``outputs`` are optional.

            - If specified, ``outputs`` is a list of string representing node
              names.

            - If ``outputs`` are not specified, converter infers outputs as all
              terminal identity nodes.

        PyTorch:
            - ``outputs`` must not be specified.

    classifier_config: ClassifierConfig class (optional)
        The configuration if the mlmodel is intended to be a classifier.

    minimum_deployment_target: coremltools.target enumeration (optional)
        - one of the members of enum ``coremltools.target``.
        - The value of this parameter determines the type of the model reperesentation
          produced by the converter. Alternatively, the ``convert_to`` argument can be used to
          specify the model type as well (see description of ``convert_to`` argument).
        - if minimum_deployment_target <= coremltools.target.iOS14/
                                          coremltools.target.macOS11/
                                          coremltools.target.watchOS7/
                                          coremltools.target.tvOS14:
            - a model of type neural network is produced.
        -  if minimum_deployment_target >= coremltools.target.iOS15/
                                           coremltools.target.macOS12/
                                           coremltools.target.watchOS8/
                                           coremltools.target.tvOS15:
            - a model of type ML Program is produced.
        - if this argument is specified and ``convert_to`` is also specified then they must be compatible.
            Invalid values are (convert_to="neuralnetwork", minimum_deployment_target=coremltools.target.iOS15)
            or (convert_to="mlprogram", minimum_deployment_target=coremltools.target.iOS14) etc.
        - When both ``minimum_deployment_target`` and the ``convert_to`` arguments are unspecified,
          converter aims to produce the neural network model type with as minimum of a deployment target as possible.

    convert_to: str (optional)
        - Must be one of [``'neuralnetwork'``, ``'mlprogram'``, ``'milinternal'``].
        - The value of this parameter determines the type of the model reperesentation
          produced by the converter. Alternatively, the ``minimum_deployment_target`` argument can be used to
          specify the model type as well (see description of the ``minimum_deployment_target`` argument).
        - ``'neuralnetwork'``: Returns MLModel (i.e. of type `coremltools.models.MLModel`) containing a NeuralNetwork
          proto. This is the older Core ML format and the model saved from this returned object is either, depending
          on the layers used in the model, executable on iOS13/macOS10.15/watchOS6/tvOS13 and above, or ececutable on
          iOS14/macOS11/watchOS7/tvOS14 and above.
        - ``'mlprogram'`` : Returns MLModel (i.e. of type `coremltools.models.MLModel`) containing a MILSpec.Program
          proto. This is the newer Core ML format, and the Core ML model saved from this returned object
          is executable on iOS15, macOS12, watchOS8, tvOS15.
        - ``'milinternal'``: Returns MIL program object (i.e. of type `coremltools.converters.mil.Program`).
            MIL program is primarily used for debugging and inspection. It can be converted to MLModel for execution,
            by using `ct.convert(mil_program, convert_to="neuralnetwork")` or `ct.convert(mil_program, convert_to="mlprogram")`
        - When both ``minimum_deployment_target`` and the ``convert_to`` arguments are unspecified,
          converter aims to produce the neural network model type with as minimum of a deployment target as possible.
          (see description of the ``minimum_deployment_target`` argument).


    compute_precision: coremltools.precision enumeration or of type ct.transform.FP16ComputePrecision() (optional)
        - Must be one of the following:
            - coremltools.precision.FLOAT16
                - in this case the transform "coremltools.transform.FP16ComputePrecision(op_selector= lambda op:True)"
                  will be applied, which injects "cast" ops to convert the float32 dtypes of intermediate tensors to float16
            - coremltools.precision.FLOAT32
                - in this case, no transform is applied and hence the original float32 tensor dtype in the source model is
                  preserved
            - coremltools.transform.FP16ComputePrecision(op_selector=...)
                - this can be used to control which tensors get cast to float16.
                - e.g.: coremltools.transform.FP16ComputePrecision(op_selector= lambda op: op.op_type != "linear")
                  will cast all the float32 tensors to be float16, except the input/output tensors to any "linear" op.
        - If None, defaults to coremltools.precision.FLOAT32
        - TODO: rdar://74140243.
            - Before coremltools 5.0 release, change the default
              to coremltools.precision.FLOAT16 when convert_to="mlprogram"

    Returns
    -------
    model: `coremltools.models.MLModel` or `coremltools.converters.mil.Program`
        A Core ML MLModel object or MIL Program object (see ``convert_to``)

    Examples
    --------
    TensorFlow 1, 2 (``model`` is a frozen graph):

        >>> with tf.Graph().as_default() as graph:
        >>>     x = tf.placeholder(tf.float32, shape=(1, 2, 3), name="input")
        >>>     y = tf.nn.relu(x, name="output")

        # Automatically infer inputs and outputs

        >>> mlmodel = ct.convert(graph)
        >>> test_input = np.random.rand(1, 2, 3) - 0.5
        >>> results = mlmodel.predict({"input": test_input})
        >>> print(results['output'])

    TensorFlow 2 (``model`` is tf.Keras model path):

        >>> x = tf.keras.Input(shape=(32,), name='input')
        >>> y = tf.keras.layers.Dense(16, activation='softmax')(x)
        >>> keras_model = tf.keras.Model(x, y)

        >>> keras_model.save(h5_path)
        >>> mlmodel = ct.convert(h5_path)

        >>> test_input = np.random.rand(2, 32)
        >>> results = mlmodel.predict({'input': test_input})
        >>> print(results['Identity'])

    Pytorch:

        >>> model = torchvision.models.mobilenet_v2()
        >>> model.eval()
        >>> example_input = torch.rand(1, 3, 256, 256)
        >>> traced_model = torch.jit.trace(model, example_input)

        >>> input = ct.TensorType(name='input_name', shape=(1, 3, 256, 256))
        >>> mlmodel = ct.convert(traced_model, inputs=[input])
        >>> results = mlmodel.predict({"input": example_input.numpy()})
        >>> print(results['1651']) # 1651 is the node name given by PyTorch's JIT

    See `neural-network-conversion <https://coremltools.readme.io/docs/neural-network-conversion>`_ for
    more advanced options.
    """
    from coremltools import __version__ as ct_version

    _check_deployment_target(minimum_deployment_target)
    exact_source = _determine_source(model, source, outputs)
    exact_target = _determine_target(convert_to, minimum_deployment_target)
    _validate_inputs(model, exact_source, inputs, outputs, classifier_config, compute_precision,
                     exact_target, **kwargs)


    if compute_precision is None:
        # TODO: rdar://74140243
        # Before 5.0 release,
        # map "None" to "fp32" for "neuralnetwork"
        # and to "fp16" for "mlprogram"
        transforms = list()
    elif compute_precision == precision.FLOAT32:
        transforms = list()
    elif compute_precision == precision.FLOAT16:
        transforms = [FP16ComputePrecision(op_selector=lambda op: True)]
    elif isinstance(compute_precision, FP16ComputePrecision):
        transforms = [compute_precision]
    else:
        raise ValueError("Invalid value of the argument 'compute_precision'")

    mlmodel = mil_convert(
        model,
        convert_from=exact_source,
        convert_to=exact_target,
        inputs=inputs,
        outputs=outputs,
        classifier_config=classifier_config,
        transforms=transforms,
        **kwargs
    )

    if exact_target == 'milinternal':
        return mlmodel # Returns the MIL program

    if minimum_deployment_target is not None:
        check_deployment_compatibility(
            spec=mlmodel.get_spec(),
            representation=exact_target,
            deployment_target=minimum_deployment_target,
        )

    gc.collect()

    mlmodel = _record_src_version(mlmodel, exact_source)
    mlmodel.user_defined_metadata[_METADATA_VERSION] = ct_version

    return mlmodel


def _check_deployment_target(minimum_deployment_target):
    if minimum_deployment_target is not None and \
        not isinstance(minimum_deployment_target, AvailableTarget):
        msg = (
            "Unrecognized value of argument 'minimum_deployment_target': {}. "
            "It needs to be a member of 'coremltools.target' enumeration. "
            "For example, coremltools.target.iOS13"
        )
        raise TypeError(msg.format(minimum_deployment_target))

def _validate_inputs(model, exact_source, inputs, outputs, classifier_config, compute_precision, convert_to,
                     **kwargs):
    """
    Validate and process model, inputs, outputs, classifier_config based on
    `exact_source` (which cannot be `auto`)
    """
    def raise_if_duplicated(input_list):
        # Detect duplicated inputs
        input_names = [t.name for t in input_list if t.name is not None]
        dups = [
            item
            for item, count in collections.Counter(input_names).items()
            if count > 1
        ]
        if len(dups) > 0:
            raise ValueError("Duplicated inputs: {}".format(dups))

    if inputs is not None:
        if not isinstance(inputs, list):
            msg = '"inputs" must be of type list'
            raise ValueError(msg)

    if classifier_config is not None:
        if not isinstance(classifier_config, ClassifierConfig):
            msg = '"classifier_config" must be of type ClassifierConfig'
            raise ValueError(msg)

    if convert_to.lower() == 'neuralnetwork':
        if compute_precision is not None:
            if compute_precision != precision.FLOAT32:
                msg = "'compute_precision' must be coremltools.precision.FLOAT32 when " \
                    "the target is 'neuralnetwork' (i.e. deployment target is less than iOS15)"
                raise ValueError(msg)

    if compute_precision is not None:
        if compute_precision not in [precision.FLOAT32, precision.FLOAT16]:
            if not isinstance(compute_precision, FP16ComputePrecision):
                msg = "'compute_precision' must be either coremltools.precision.FLOAT32 or coremltools.precision.FLOAT16" \
                      " or of type coremltools.transform.FP16ComputePrecision()"
                raise ValueError(msg)

    if exact_source in {"tensorflow", "tensorflow2"}:
        if exact_source == "tensorflow" and not _HAS_TF_1:
            msg = 'Converter was called with source="tensorflow", ' +\
                    'but missing tensorflow package'
            raise ValueError(msg)

        if inputs is not None:
            raise_if_duplicated(inputs)

        if inputs is not None and not all(
            [isinstance(_input, InputType) for _input in inputs]
        ):
            raise ValueError("Input should be a list of TensorType or ImageType")

    elif exact_source == "pytorch":
        if "example_inputs" in kwargs:
            msg = 'Unexpected argument "example_inputs" found'
            raise ValueError(msg)

        if inputs is None:
            msg = 'Expected argument for pytorch "inputs" not provided'
            raise ValueError(msg)

        def _flatten_list(_inputs):
            ret = []
            for _input in _inputs:
                if isinstance(_input, (list, tuple)):
                    ret.extend(_flatten_list(_input))
                elif isinstance(_input, InputType):
                    ret.append(_input)
                else:
                    raise ValueError(
                        "Unknown type {} for flattening into InputType.".format(
                            type(_input)
                        )
                    )
            return ret

        flat_inputs = _flatten_list(inputs)
        raise_if_duplicated(flat_inputs)
        if inputs is not None and not all(
            [isinstance(_input, InputType) for _input in flat_inputs]
        ):
            raise ValueError(
                "Input should be a list/tuple (or nested lists/tuples) of TensorType or ImageType"
            )
        if outputs is not None:
            raise ValueError("outputs must not be specified for PyTorch")

    elif exact_source == "milinternal":
        if not isinstance(model, Program):
            msg = "Converter was asked to convert MIL input, but input is not a MIL program!"
            raise ValueError(msg)


def _determine_source(model, source, outputs):
    """
    Infer source (which can be auto) to the precise framework.
    """
    source = source.lower()
    if source not in {"auto", "tensorflow", "pytorch", "milinternal"}:
        msg = (
            'Unrecognized value of argument "source": {}. '
            'It must be one of ["auto", "tensorflow", "pytorch"].'
        )
        raise ValueError(msg.format(source))


    # Determine tensorflow version
    if source == "tensorflow" and _HAS_TF_2:
        return "tensorflow2"

    if source != 'auto':
        return source

    # Determine `auto` source
    if source == "auto" and _HAS_TF_1:
        try:
            loader = TF1Loader(model, outputs=outputs)
            loader._graph_def_from_model(outputs=outputs)
            return "tensorflow"
        except:
            pass

    if source == "auto" and _HAS_TF_2:
        try:
            loader = TF2Loader(model, outputs=outputs)
            loader._graph_def_from_model(outputs=outputs)
            return "tensorflow2"
        except:
            pass

    if source == "auto" and _HAS_TORCH:
        try:
            pytorch_load(model)
            return "pytorch"
        except:
            pass

    if source == "auto" and isinstance(model, Program):
        return "milinternal"

    msg = (
        "Unable to determine the type of the model, i.e. the source framework. "
        'Please provide the value of argument "source", from one of '
        '["tensorflow", "pytorch", "milinternal"]. Note that model conversion requires the '
        "source package that generates the model. Please make sure you have "
        "the appropriate version of source package installed. E.g., if you're "
        "converting model originally trained with TensorFlow 1.14, make sure "
        "you have `tensorflow==1.14` installed."
    )
    raise ValueError(msg)

def _determine_target(convert_to, minimum_deployment_target):
    """
    Infer the precise backend target, which could be one of ``milinternal``, ``neuralnetwork`` or ``mlprogram``
    """
    if minimum_deployment_target is not None:
        if convert_to == "mlprogram" and \
            minimum_deployment_target.value < AvailableTarget.iOS15.value:
                msg = "When 'convert_to' is {}, the minimum deployment target must be at least iOS15/macOS12/watchOS8/tvOS15"
                raise ValueError(msg.format(convert_to))

        if convert_to == "neuralnetwork" and \
            minimum_deployment_target.value >= AvailableTarget.iOS15.value:
            msg = "If minimum deployment target is iOS15/macOS12/watchOS8/tvOS15 or higher, then " \
                  "'convert_to' cannot be {}. It must be 'mlprogram'"
            raise ValueError(msg.format(convert_to))

    if convert_to is not None:
        return convert_to
    else:
        if minimum_deployment_target is None:
            return "neuralnetwork"
        elif minimum_deployment_target.value <= AvailableTarget.iOS14.value:
            return "neuralnetwork"
        else:
            return "mlprogram"

def _record_src_version(mlmodel, exact_source):
    # recording metadata: coremltools version, source framework and version
    if exact_source in {"tensorflow", "tensorflow2"} and (_HAS_TF_1 or _HAS_TF_2):
        src_pkg_version = "tensorflow=={0}".format(tf.__version__)
    elif exact_source == "pytorch" and _HAS_TORCH:
        src_pkg_version = "torch=={0}".format(torch.__version__)
    elif exact_source == 'milinternal':
        src_pkg_version = "milinternal"
    else:
        raise ValueError('Unsupported source {}'.format(exact_source))

    mlmodel.user_defined_metadata[_METADATA_SOURCE] = src_pkg_version
    return mlmodel
