# type: ignore
import os
import platform
import shutil
import stat
import sys

import setuptools

from semgrep import __VERSION__


SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SOURCE_DIR)
BIN_DIR = "bin"
PACKAGE_BIN_DIR = os.path.join(SOURCE_DIR, "semgrep", BIN_DIR)
SEMGREP_CORE_BIN = "semgrep-core"
SEMGREP_CORE_BIN_ENV = "SEMGREP_CORE_BIN"
SPACEGREP_BIN = "spacegrep"
SPACEGREP_BIN_ENV = "SPACEGREP_BIN"
SEMGREP_SKIP_BIN = "SEMGREP_SKIP_BIN" in os.environ
SEMGREP_FORCE_INSTALL = "SEMGREP_FORCE_INSTALL" in os.environ
IS_WINDOWS = platform.system() == "Windows"
WHEEL_CMD = "bdist_wheel"

if WHEEL_CMD in sys.argv:
    try:
        from wheel.bdist_wheel import bdist_wheel
    except ImportError:
        raise Exception(f"The 'wheel' package is required when running '{WHEEL_CMD}'")

    class BdistWheel(bdist_wheel):
        def finalize_options(self):
            bdist_wheel.finalize_options(self)
            self.root_is_pure = False  # We have platform specific binaries

        def get_tag(self):
            _, _, plat = bdist_wheel.get_tag(self)
            python = "cp36.cp37.cp38.cp39.py36.py37.py38.py39"
            abi = "none"
            plat = "macosx_10_14_x86_64" if "macosx" in plat else "any"
            return python, abi, plat

    cmdclass = {WHEEL_CMD: BdistWheel}
else:
    cmdclass = {}

if IS_WINDOWS and not SEMGREP_FORCE_INSTALL:
    raise Exception(
        "Semgrep does not support Windows yet, please try again with WSL "
        "or visit the following for more information: "
        "https://github.com/returntocorp/semgrep/issues/1330"
    )

try:
    with open(os.path.join(REPO_ROOT, "README.md")) as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "**SETUP: README NOT FOUND**"


def find_executable(env_name, exec_name):
    # First, check for an environment override
    env_value = os.getenv(env_name)
    if env_value:
        return env_value

    # Second, fallback to any system executable
    which_name = shutil.which(exec_name)
    if which_name is not None:
        return which_name

    raise Exception(
        f"Could not find '{exec_name}' executable, tried '{env_name}' and system '{exec_name}'"
    )


if not SEMGREP_SKIP_BIN:
    binaries = [
        (SEMGREP_CORE_BIN_ENV, SEMGREP_CORE_BIN),
        (SPACEGREP_BIN_ENV, SPACEGREP_BIN),
    ]

    for binary_env, binary_name in binaries:
        src = find_executable(binary_env, binary_name)
        dst = os.path.join(PACKAGE_BIN_DIR, binary_name)
        shutil.copyfile(src, dst)
        os.chmod(dst, os.stat(dst).st_mode | stat.S_IEXEC)

setuptools.setup(
    name="semgrep",
    version=__VERSION__,
    author="Return To Corporation",
    author_email="support@r2c.dev",
    description="Lightweight static analysis for many languages. Find bug variants with patterns that look like source code.",
    cmdclass=cmdclass,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/returntocorp/semgrep",
    install_requires=[
        "attrs>=19.3.0",
        "colorama>=0.4.3",
        "requests>=2.22.0",
        # Pin exact version of 'ruamel.yaml' because of unstable API.
        # Ensure default type is still 'rt' (round-trip) and that RoundTrip
        # inherits from Safe when upgrading the version.
        "ruamel.yaml>=0.16.0,<0.18",
        "tqdm>=4.46.1",
        "packaging>=20.4",
        "jsonschema~=3.2.0",
        # Include 'setuptools' for 'pkg_resources' usage. We shouldn't be
        # overly prescriptive and pin the version for two reasons: 1) because
        # it may interfere with other 'setuptools' installs on the system,
        # and 2) our 'pkg_resources' API usage appears to have been available
        # in 'setuptools' for a very long time, so we don't need a recent
        # version.
        "setuptools",
    ],
    entry_points={"console_scripts": ["semgrep=semgrep.__main__:main"]},
    packages=setuptools.find_packages(),
    package_data={"semgrep": [os.path.join(BIN_DIR, "*")]},
    include_package_data=True,
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Security",
        "Topic :: Software Development :: Quality Assurance",
    ],
    python_requires=">=3.6",
    zip_safe=False,
)
