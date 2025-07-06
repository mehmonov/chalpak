#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

NAME = 'chalpak'
DESCRIPTION = 'Chalpak - mini web framework like fastAPi, flask'
URL = 'https://github.com/mehmonov/chalpak'
EMAIL = 'mehmonov.husniddin1@gmail.com'
AUTHOR = 'Mehmonov Husniddin'
REQUIRES_PYTHON = '>=3.11.0'
VERSION = '0.2.4'

REQUIRED = [
    'aiohttp==3.9.5',
    'aiohttp-jinja2==1.6',
    'watchdog==4.0.0',
    'jurigged==0.5.7',
    'Jinja2==3.1.4'
]

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: Implementation :: CPython',
        ]

   
)