#!/usr/bin/env python

# import os
import sys
# import glob

from setuptools import setup

data_files = [
    ('share/doc/pymdstat', ['AUTHORS', 'README.rst'])
]

def get_data_files():
    data_files = [
        ('share/doc/pymdstat', ['AUTHORS', 'NEWS', 'README.rst'])
    ]

    # if hasattr(sys, 'real_prefix') or 'bsd' in sys.platform:
    #     conf_path = os.path.join(sys.prefix, 'etc', 'glances')
    # elif not hasattr(sys, 'real_prefix') and 'linux' in sys.platform:
    #     conf_path = os.path.join('/etc', 'glances')
    # elif 'darwin' in sys.platform:
    #     conf_path = os.path.join('/usr/local', 'etc', 'glances')
    # elif 'win32' in sys.platform:
    #     conf_path = os.path.join(os.environ.get('APPDATA'), 'glances')
    # data_files.append((conf_path, ['conf/glances.conf']))

    # for mo in glob.glob('i18n/*/LC_MESSAGES/*.mo'):
    #     data_files.append((os.path.dirname(mo).replace('i18n/', 'share/locale/'), [mo]))

    return data_files


def get_requires():
    requires = []

    if sys.version_info < (2, 7):
        requires += ['argparse']

    return requires


setup(
    name='pymdstat',
    version='0.2',
    description="Python lib to parse the /proc/mdstat file on Linux system",
    long_description=open('README.rst').read(),
    author='Nicolas Hennion',
    author_email='nicolas@nicolargo.com',
    url='https://github.com/nicolargo/pymdstat',
    #download_url='https://s3.amazonaws.com/pymdstat/pymdstat-0.1.tar.gz',
    license="LGPL",
    keywords="...",
    install_requires=get_requires(),
    extras_require={},    
    packages=['pymdstat'],
    include_package_data=True,
    data_files=get_data_files(),
    # test_suite="pymdstat.test",
    entry_points={"console_scripts": ["pymdstat=pymdstat.pymdstat:main"]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
