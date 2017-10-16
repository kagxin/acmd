#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
readme_file = os.path.join(here, 'README.md')

install_requires = []
long_description = '\n\n'.join((
    open(readme_file).read(),
))


setup(
    name = 'acmd',
    version = '0.0.1',
    url = 'http://github.com/kagxin/acmd',
    license = 'BSD',
    description = 'an asynchronous implementation of the python cmd module.',
    long_description = long_description,
    author = "kagxin",
    author_email = 'kagxin at gmail dot com',
    packages = ['acmd'],
    install_requires=install_requires,
)