#!/usr/bin/env python

from setuptools import setup

data_files = [('share/doc/pymdstat', ['AUTHORS', 'LICENSE', 'NEWS', 'README.rst'])]

setup(
    name='pymdstat',
    version='0.4.2',
    description="Python library to parse Linux /proc/mdstat",
    long_description=open('README.rst').read(),
    author='Nicolas Hennion',
    author_email='nicolas@nicolargo.com',
    url='https://github.com/nicolargo/pymdstat',
    # download_url='https://s3.amazonaws.com/pymdstat/pymdstat-0.4.2.tar.gz',
    license="MIT",
    keywords="raid linux",
    packages=['pymdstat'],
    include_package_data=True,
    data_files=data_files,
    # test_suite="pymdstat.test",
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
