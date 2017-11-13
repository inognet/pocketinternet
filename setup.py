#!/usr/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup

import pocketnet

install_requires = [
    "Jinja2>=2.9.6",
    "PyYAML>=3.12",
    "docker>=2.5.1"
]

setup(
    name="pocketinternet",
    version=pocketnet.__version__,
    packages=['pocketnet'],
    author='PocketInternet Team',
    description="RIPE NCC Hackathon Version 6",
    
    install_requires=install_requires,
    scripts=['bin/pocketinternet']
)