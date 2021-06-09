# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kfx', 'kfx.dsl', 'kfx.vis']

package_data = \
{'': ['*']}

install_requires = \
['kfp>=0.2.0,<2', 'pydantic>=1.0.0,<2.0.0', 'typing-extensions']

setup_kwargs = {
    'name': 'kfx',
    'version': '0.1.0',
    'description': 'Extensions for kubeflow pipeline sdk.',
    'long_description': '# kfx\n\n[![PyPI version](https://badge.fury.io/py/kfx.svg)](https://badge.fury.io/py/kfx)\n[![Build Status](https://travis-ci.org/e2fyi/kfx.svg?branch=master)](https://travis-ci.org/e2fyi/kfx)\n[![Coverage Status](https://coveralls.io/repos/github/e2fyi/kfx/badge.svg?branch=master)](https://coveralls.io/github/e2fyi/kfx?branch=master)\n[![Documentation Status](https://readthedocs.org/projects/kfx/badge/?version=latest)](https://kfx.readthedocs.io/en/latest/?badge=latest)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Downloads](https://pepy.tech/badge/kfx/month)](https://pepy.tech/project/kfx/month)\n\n`kfx` is a python package with the namespace `kfx`. Currently, it provides the\nfollowing sub-packages\n\n- `kfx.lib.dsl` - Extensions to the kubeflow pipeline dsl.\n\n- `kfx.lib.vis` - Data models and helpers to help generate the  `mlpipeline-metrics.json` and `mlpipeline-ui-metadata.json` required to render visualization in the kubeflow pipeline UI. See also https://www.kubeflow.org/docs/pipelines/sdk/pipelines-metrics/ and https://www.kubeflow.org/docs/pipelines/sdk/output-viewer/\n\n> - Documentation: [https://kfx.readthedocs.io](https://kfx.readthedocs.io).\n> - Repo: [https://github.com/e2fyi/kfx](https://github.com/e2fyi/kfx)\n\n> ### NOTE this is currently alpha\n>\n> There will likely to have breaking changes, and feel free to do a feature request\n>\n> ### Known issues\n>\n> - `kfx.vis.vega.vega_web_app` and `KfpArtifact` does not work well together (see example) because of CORs - the web app is hosted inside an iFrame which prevents it from accessing the `ml-pipeline-ui` API server.\n> - `kfx.vis.vega.vega_web_app` is only supported in the latest kubeflow pipeline UI (as inline is only supported after `0.2.5`)\n\n### Changelog\n\nRefer to [CHANGELOG.md](./CHANGELOG.md).\n\n## Quick start\n\nInstallation\n\n```bash\npip install kfx\n```\n\n## Usage\n\nExample: Using `ContainerOpTransform` to configure the internal k8s properties\nof kubeflow pipelines tasks.\n\n> `kfx.dsl.ContainerOpTransform` is a helper to modify the interal k8s properties\n> (e.g. resources, environment variables, etc) of kubeflow pipeline tasks.\n\n```python\nimport kfp.components\nimport kfp.dsl\nimport kfx.dsl\n\ntransforms = (\n    kfx.dsl.ContainerOpTransform()\n    .set_resources(cpu="500m", memory=("1G", "4G"))\n    .set_image_pull_policy("Always")\n    .set_env_vars({"ENV": "production"})\n    .set_env_var_from_secret("AWS_ACCESS_KEY", secret_name="aws", secret_key="access_key")\n    .set_annotations({"iam.amazonaws.com/role": "some-arn"})\n)\n\n\n@kfp.dsl.components.func_to_container_op\ndef echo(text: str) -> str:\n    print(text)\n    return text\n\n\n@kfp.dsl.pipeline(name="demo")\ndef pipeline(text: str):\n    op1 = echo(text)\n    op2 = echo("%s-%s" % text)\n\n    # u can apply the transform on op1 only\n    # op1.apply(transforms)\n\n    # or apply on all ops in the pipeline\n    kfp.dsl.get_pipeline_conf().add_op_transformer(transforms)\n\n```\n\nExample: Using `ArtifactLocationHelper` and `KfpArtifact` to determine the\nuri of your data artifact generated by the kubeflow pipeline task.\n\n> `kfx.dsl.ArtifactLocationHelper` is a helper to modify the kubeflow pipeline task\n> so that you can use `kfx.dsl.KfpArtifact` to represent the artifact generated\n> inside the task.\n\n```python\nimport kfp.components\nimport kfp.dsl\nimport kfx.dsl\n\n\n# creates the helper that has the argo configs (tells you how artifacts will be stored)\n# see https://github.com/argoproj/argo/blob/master/docs/workflow-controller-configmap.yaml\nhelper = kfx.dsl.ArtifactLocationHelper(\n    scheme="minio", bucket="mlpipeline", key_prefix="artifacts/"\n)\n\n@kfp.components.func_to_container_op\ndef test_op(\n    mlpipeline_ui_metadata: OutputTextFile(str), markdown_data_file: OutputTextFile(str)\n):\n    "A test kubeflow pipeline task."\n\n    import json\n\n    import kfx.dsl\n    import kfx.vis\n    import kfx.vis.vega\n\n    # `KfpArtifact` provides the reference to data artifact created\n    # inside this task\n    spec = {\n        "$schema": "https://vega.github.io/schema/vega-lite/v4.json",\n        "description": "A simple bar chart",\n        "data": {\n            "values": [\n                {"a": "A", "b": 28},\n                {"a": "B", "b": 55},\n                {"a": "C", "b": 43},\n                {"a": "D", "b": 91},\n                {"a": "E", "b": 81},\n                {"a": "F", "b": 53},\n                {"a": "G", "b": 19},\n                {"a": "H", "b": 87},\n                {"a": "I", "b": 52},\n            ]\n        },\n        "mark": "bar",\n        "encoding": {\n            "x": {"field": "a", "type": "ordinal"},\n            "y": {"field": "b", "type": "quantitative"},\n        },\n    }\n\n    # write the markdown to the `markdown-data` artifact\n    markdown_data_file.write("### hello world")\n\n    # creates an ui metadata object\n    ui_metadata = kfx.vis.kfp_ui_metadata(\n        # Describes the vis to generate in the kubeflow pipeline UI.\n        [\n            # markdown vis from a markdown artifact.\n            # `KfpArtifact` provides the reference to data artifact created\n            # inside this task\n            kfx.vis.markdown(kfx.dsl.KfpArtifact("markdown_data_file")),\n            # a vega web app from the vega data artifact.\n            kfx.vis.vega.vega_web_app(spec),\n        ]\n    )\n\n    # writes the ui metadata object as the `mlpipeline-ui-metadata` artifact\n    mlpipeline_ui_metadata.write(kfx.vis.asjson(ui_metadata))\n\n    # prints the uri to the markdown artifact\n    print(ui_metadata.outputs[0].source)\n\n\n@kfp.dsl.pipeline()\ndef test_pipeline():\n    "A test kubeflow pipeline"\n\n    op: kfp.dsl.ContainerOp = test_op()\n\n    # modify kfp operator with artifact location metadata through env vars\n    op.apply(helper.set_envs())\n\n```\n\nExample: Using `pydantic` data models to generate `mlpipeline-metrics.json` and\n`mlpipeline-ui-metadata.json`.\n\n(See also https://www.kubeflow.org/docs/pipelines/sdk/output-viewer/ and\nhttps://www.kubeflow.org/docs/pipelines/sdk/pipelines-metrics/).\n\n> `kfx.vis` has helper functions (with corresponding hints) to describe and\n> create `mlpipeline-metrics.json` and `mlpipeline-ui-metadata.json` files\n> (required by kubeflow pipeline UI to render any metrics or visualizations).\n\n```python\nimport functools\n\nimport kfp.components\n\n\n# install kfx\nkfx_component = functools.partial(kfp.components.func_to_container_op, packages_to_install=["kfx"])\n\n\n@kfx_component\ndef some_op(\n    # mlpipeline_metrics is a path - i.e. open(mlpipeline_metrics, "w")\n    mlpipeline_metrics: kfp.components.OutputPath(str),\n    # mlpipeline_ui_metadata is a FileLike obj - i.e. mlpipeline_ui_metadata.write("something")\n    mlpipeline_ui_metadata: kfp.components.OutputTextFile(str),\n):\n    "kfp operator that provides metrics and metadata for visualizations."\n\n    # import inside kfp task\n    import kfx.vis\n\n    # output metrics to mlpipeline_metrics path\n    kfx.vis.kfp_metrics([\n        # render as percent\n        kfx.vis.kfp_metric("recall-score", 0.9, percent=true),\n        # override metric format with custom value\n        kfx.vis.kfp_metric(name="percision-score", value=0.8, metric_format="PERCENTAGE"),\n        # render raw score\n        kfx.vis.kfp_metric("raw-score", 123.45),\n    ]).write_to(mlpipeline_metrics)\n\n    # output visualization metadata to mlpipeline_ui_metadata obj\n    kfx.vis.kfp_ui_metadata(\n        [\n            # creates a confusion matrix vis\n            kfx.vis.confusion_matrix(\n                source="gs://your_project/your_bucket/your_cm_file",\n                labels=["True", "False"],\n            ),\n            # creates a markdown with inline source\n            kfx.vis.markdown(\n                "# Inline Markdown: [A link](https://www.kubeflow.org/)",\n                storage="inline",\n            ),\n            # creates a markdown with a remote source\n            kfx.vis.markdown(\n                "gs://your_project/your_bucket/your_markdown_file",\n            ),\n            # creates a ROC curve with a remote source\n            kfx.vis.roc(\n                "gs://your_project/your_bucket/your_roc_file",\n            ),\n            # creates a Table with a remote source\n            kfx.vis.table(\n                "gs://your_project/your_bucket/your_csv_file",\n                header=["col1", "col2"],\n            ),\n            # creates a tensorboard viewer\n            kfx.vis.tensorboard(\n                "gs://your_project/your_bucket/logs/*",\n            ),\n            # creates a custom web app from a remote html file\n            kfx.vis.web_app(\n                "gs://your_project/your_bucket/your_html_file",\n            ),\n            # creates a Vega-Lite vis as a web app\n            kfx.vis.vega.vega_web_app(spec={\n                "$schema": "https://vega.github.io/schema/vega-lite/v4.json",\n                "description": "A simple bar chart with embedded data.",\n                "data": {\n                    "values": [\n                        {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},\n                        {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},\n                        {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}\n                    ]\n                },\n                "mark": "bar",\n                "encoding": {\n                    "x": {"field": "a", "type": "ordinal"},\n                    "y": {"field": "b", "type": "quantitative"}\n                }\n            })\n        ]\n    ).write_to(mlpipeline_ui_metadata)\n```\n\n## Developer guide\n\nThis project used:\n\n- isort: to manage import order\n- pylint: to manage general coding best practices\n- flake8: to manage code complexity and coding best practices\n- black: to manage formats and styles\n- pydocstyle: to manage docstr style/format\n- pytest/coverage: to manage unit tests and code coverage\n- bandit: to find common security issues\n- pyenv: to manage dev env: python version (3.6)\n- pipenv: to manage dev env: python packages\n\nConvention for unit tests are to suffix with `_test` and colocate with the actual\npython module - i.e. `<module_name>_test.py`.\n\nThe version of the package is read from `version.txt` - i.e. please update the\nappropriate semantic version (major -> breaking changes, minor -> new features, patch -> bug fix, postfix -> pre-release/post-release).\n\n### `Makefile`:\n\n```bash\n# autoformat codes with docformatter, isort, and black\nmake format\n\n# check style, formats, and code complexity\nmake check\n\n# check style, formats, code complexity, and run unit tests\nmake test\n\n# test everything including building the package and check the sdist\nmake test-all\n\n# run unit test only\nmake test-only\n\n# generate and update the requirements.txt and requirements-dev.txt\nmake requirements\n\n# generate the docs with sphinx and autoapi extension\nmake docs\n\n# generate distributions\nmake dists\n\n# publish to pypi with twine (twine must be configured)\nmake publish\n```\n',
    'author': 'eterna2',
    'author_email': 'eterna2@hotmail.com',
    'maintainer': 'eterna2',
    'maintainer_email': 'eterna2@hotmail.com',
    'url': 'https://github.com/e2fyi/kfx',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)
