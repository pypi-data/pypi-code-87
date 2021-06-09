import os
import re
import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()

    return re.search('__version__ = [\'"]([^\'"]+)[\'"]', init_py).group(1)


version = get_version('px_access_scopes')


setuptools.setup(
    name='px-access-scopes',
    version=version,
    author='Alex Tkachenko',
    author_email='preusx.dev@gmail.com',
    license='MIT License',
    description='Simple access-scopes utility package.',
    install_requires=(
        'px-domains==0.1.0'
    ),
    extras_require={
        'dev': (
            'pytest>=6.0,<7.0',
            'pytest-watch>=4.2,<5.0',
        ),
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(exclude=('tests', 'tests.*')),
    python_requires='>=3.6',
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',

        'Programming Language :: Python :: 3',

        'Intended Audience :: Developers',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
