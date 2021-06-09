import os
from setuptools import setup

README = """
See the README on `GitHub
<https://github.com/uw-it-aca/uw-restclients-adsel>`_.
"""

# The VERSION file is created by travis-ci, based on the tag name
version_path = 'uw_adsel/VERSION'
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

url = "https://github.com/uw-it-aca/uw-restclients-adsel"
setup(
    name='UW-RestClients-AdSel',
    version=VERSION,
    packages=['uw_adsel'],
    author="UW-IT AXDD",
    author_email="aca-it@uw.edu",
    include_package_data=True,
    install_requires=['UW-RestClients-Core>1.0,<2.0',
                      'mock',
                      'python-dateutil'
                     ],
    license='Apache License, Version 2.0',
    description=('A library for connecting to the AdSel API at the University'
                 ' of Washington'),
    long_description=README,
    url=url,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)


