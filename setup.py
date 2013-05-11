#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup

def publish():
    """Publish to PyPi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

setup(
    name='logit',
    version='0.1.0',
    description='Sometimes you just need to write something down, so logit.',
    long_description='',
    author='Chad Gallemore',
    author_email='chad@gallemore.me',
    url='https://github.com/cgallemore/logit',
    license=open('LICENSE').read(),
    package_data={'': ['LICENSE']},
    classifiers=(
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ),
    entry_points={
        'console_scripts': [
            'logit = logit:main',
            ],
        }
)
