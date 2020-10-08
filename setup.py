#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the Spot Cursor-on-Target Gateway.

Source:: https://github.com/ampledata/spotcot
"""

import os
import sys

import setuptools

__title__ = 'spotcot'
__version__ = '1.0.1'
__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    name=__title__,
    version=__version__,
    description='Spot Cursor-on-Target Gateway.',
    author='Greg Albrecht',
    author_email='oss@undef.net',
    packages=['spotcot'],
    package_data={'': ['LICENSE']},
    package_dir={'spotcot': 'spotcot'},
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    url='https://github.com/ampledata/spotcot',
    zip_safe=False,
    include_package_data=True,
    tests_requires=[
        'coverage >= 3.7.1',
        'pytest'
    ],
    install_requires=[
        'pycot >= 2.0.0',
        'spot_sdk'
    ],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License'
    ],
    keywords=[
        'Sailing', 'Spot', 'Cursor on Target', 'ATAK', 'TAK', 'CoT'
    ],
    entry_points={'console_scripts': ['spotcot = spotcot.cmd:cli']}
)
