#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of elementary-test-generator.
# https://github.com/rflorianobr/elementary-test-generator

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Rafael Floriano da Silva <rflorianobr@gmail.com>

from setuptools import setup, find_packages
from elementary_test_generator import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='elementary-test-generator',
    version=__version__,
    description='an incredible django app',
    long_description='''
an incredible django app
''',
    keywords='python sparql elementary school test generator',
    author='Rafael Floriano da Silva',
    author_email='rflorianobr@gmail.com',
    url='https://github.com/rflorianobr/elementary-test-generator',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'django',
        # 'django-rq',
        'SPARQLWrapper',
        'dj-database-url',
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.(y+1).0' notation
        # (this way you get bugfixes but no breaking changes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'elementary-test-generator=elementary_test_generator.cli:main',
        ],
    },
)
