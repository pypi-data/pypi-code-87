import logging
import os

from ludwig.api import LudwigModel
from ludwig.callbacks import Callback
from ludwig.utils.data_utils import chunk_dict, flatten_dict, to_json_dict
from ludwig.utils.package_utils import LazyLoader

mlflow = LazyLoader('mlflow', globals(), 'mlflow')

logger = logging.getLogger(__name__)


def _get_or_create_experiment_id(experiment_name):
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is not None:
        return experiment.experiment_id
    return mlflow.create_experiment(name=experiment_name)


class MlflowCallback(Callback):
    def __init__(self, tracking_uri=None):
        self.experiment_id = None
        self.run = None
        self.tracking_uri = tracking_uri
        if tracking_uri:
            mlflow.set_tracking_uri(tracking_uri)

    def on_hyperopt_init(self, experiment_name):
        self.experiment_id = _get_or_create_experiment_id(experiment_name)

    def on_hyperopt_trial_start(self, parameters):
        # Filter out mlflow params like tracking URI, experiment ID, etc.
        params = {k: v for k, v in parameters.items() if k != 'mlflow'}
        self._log_params({'hparam': params})

    def on_train_init(
            self,
            base_config,
            experiment_name,
            output_directory,
            **kwargs
    ):
        # Experiment may already have been set during hyperopt init, in
        # which case we don't want to create a new experiment / run, as
        # this should be handled by the executor.
        if self.experiment_id is None:
            self.experiment_id = _get_or_create_experiment_id(experiment_name)
            run_name = os.path.basename(output_directory)
            self.run = mlflow.start_run(
                experiment_id=self.experiment_id,
                run_name=run_name
            )

        mlflow.log_dict(to_json_dict(base_config), 'config.yaml')

    def on_train_start(self, config, **kwargs):
        self._log_params({'training': config['training']})

    def on_train_end(self, output_directory):
        _log_artifacts(output_directory)
        if self.run is not None:
            mlflow.end_run()

    def on_epoch_end(self, trainer, progress_tracker, save_path):
        mlflow.log_metrics(
            progress_tracker.log_metrics,
            step=progress_tracker.steps
        )

        mlflow.pyfunc.log_model(
            artifact_path='model',
            **_export_kwargs(save_path)
        )

    def on_visualize_figure(self, fig):
        # TODO: need to also include a filename for this figure
        # mlflow.log_figure(fig)
        pass

    def prepare_ray_tune(self, train_fn, tune_config, tune_callbacks):
        from ray.tune.integration.mlflow import mlflow_mixin

        return mlflow_mixin(train_fn), {
            **tune_config,
            'mlflow': {
                'experiment_id': self.experiment_id,
                'tracking_uri': mlflow.get_tracking_uri(),
            }
        }

    def _log_params(self, params):
        flat_params = flatten_dict(params)
        for chunk in chunk_dict(flat_params, chunk_size=100):
            mlflow.log_params(chunk)

    def __setstate__(self, d):
        self.__dict__ = d
        if self.tracking_uri:
            mlflow.set_tracking_uri(self.tracking_uri)


class LudwigMlflowModel(mlflow.pyfunc.PythonModel):
    def __init__(self):
        super().__init__()
        self._model = None

    def load_context(self, context):
        self._model = LudwigModel.load(context.artifacts['model'])

    def predict(self, context, model_input):
        pred_df, _ = self._model.predict(model_input)
        return pred_df


def _export_kwargs(model_path):
    return dict(
        python_model=LudwigMlflowModel(),
        artifacts={
            'model': model_path,
        },
    )


def _log_artifacts(output_directory):
    for fname in os.listdir(output_directory):
        lpath = os.path.join(output_directory, fname)
        if fname == 'model':
            mlflow.pyfunc.log_model(
                artifact_path='model',
                **_export_kwargs(lpath)
            )
        else:
            mlflow.log_artifact(lpath)


def export_model(model_path, output_path, registered_model_name=None):
    kwargs = _export_kwargs(model_path)
    if registered_model_name:
        if not model_path.startswith('runs:/') or output_path is not None:
            # No run specified, so in order to register the model in mlflow, we need
            # to create a new run and upload the model as an artifact first
            output_path = output_path or 'model'
            with mlflow.start_run():
                mlflow.pyfunc.log_model(
                    artifact_path=output_path,
                    registered_model_name=registered_model_name,
                    **kwargs
                )
        else:
            # Registering a model from an artifact of an existing run
            mlflow.register_model(
                model_path,
                registered_model_name,
            )
    else:
        # No model name means we only want to save the model locally
        mlflow.pyfunc.save_model(
            path=output_path,
            **kwargs
        )
