import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-kaniko",
    "version": "0.2.12",
    "description": "CDK construct library that allows you to build docker images with kaniko in AWS Fargate",
    "license": "Apache-2.0",
    "url": "https://github.com/pahud/cdk-kaniko.git",
    "long_description_content_type": "text/markdown",
    "author": "Pahud Hsieh<pahudnet@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/pahud/cdk-kaniko.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_kaniko",
        "cdk_kaniko._jsii"
    ],
    "package_data": {
        "cdk_kaniko._jsii": [
            "cdk-kaniko@0.2.12.jsii.tgz"
        ],
        "cdk_kaniko": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-ec2>=1.96.0, <2.0.0",
        "aws-cdk.aws-ecr>=1.96.0, <2.0.0",
        "aws-cdk.aws-ecs>=1.96.0, <2.0.0",
        "aws-cdk.aws-events>=1.96.0, <2.0.0",
        "aws-cdk.core>=1.96.0, <2.0.0",
        "cdk-fargate-run-task>=0.1.31, <0.2.0",
        "constructs>=3.2.27, <4.0.0",
        "jsii>=1.30.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
