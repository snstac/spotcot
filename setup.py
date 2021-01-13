#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup for the Spot Cursor-on-Target Gateway.

:author: Greg Albrecht W2GMD <oss@undef.net>
:copyright: Copyright 2021 Orion Labs, Inc.
:license: Apache License, Version 2.0
:source: https://github.com/ampledata/spotcot
"""

import os
import sys

import setuptools

__title__ = "spotcot"
__version__ = "2.0.0"
__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == "publish":
        os.system("python setup.py sdist")
        os.system("twine upload dist/*")
        sys.exit()


publish()


setuptools.setup(
    version=__version__,
    name=__title__,
    packages=[__title__],
    package_dir={__title__: __title__},
    url=f"https://github.com/ampledata/{__title__}",
    description="Spot Cursor-on-Target Gateway.",
    author="Greg Albrecht",
    author_email="oss@undef.net",
    package_data={"": ["LICENSE"]},
    license=open("LICENSE").read(),
    long_description=open("README.rst").read(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "pycot >= 2.5.0",
        "pytak >= 3.0.0"
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License"
    ],
    keywords=[
        "Spot", "Cursor on Target", "ATAK", "TAK", "CoT"
    ],
    entry_points={"console_scripts": ["spotcot = spotcot.commands:cli"]}
)
