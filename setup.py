#!/usr/bin/env python

from setuptools import setup
import os
import re

with open(os.path.join('pymdstat', '__init__.py'), encoding='utf-8') as f:
    version = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M).group(1)

if not version:
    raise RuntimeError('Cannot find version information in __init__.py file.')

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

data_files = [('share/doc/pymdstat', ['AUTHORS', 'LICENSE', 'NEWS', 'README.rst'])]

setup(
    name='pymdstat',
    version=version,
    description="Python library to parse Linux /proc/mdstat",
    long_description=long_description,
    author='Nicolas Hennion',
    author_email='nicolas@nicolargo.com',
    url='https://github.com/nicolargo/pymdstat',
    # download_url='https://s3.amazonaws.com/pymdstat/pymdstat-0.4.2.tar.gz',
    license="MIT",
    keywords="raid linux",
    packages=['pymdstat'],
    include_package_data=True,
    data_files=data_files,
    test_suite="unitest.py",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
