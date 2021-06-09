from setuptools import find_packages, setup

my_pckg = find_packages(include=["skbel"])

setup(
    name="skbel",
    version="1.0.7",
    packages=my_pckg,
    include_package_data=True,
    url="https://github.com/robinthibaut/skbel",
    license="BSD-3",
    author="Robin Thibaut",
    author_email="robin.thibaut@UGent.be",
    description="A set of Python modules to implement the Bayesian Evidential Learning framework",
    install_requires=["numpy", "pandas", "scipy", "matplotlib", "scikit-learn", "joblib"],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires=">=3.6",
)
