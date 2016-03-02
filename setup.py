#!/usr/bin/env python
from setuptools import setup, find_packages
from csvhandler import VERSION


setup(name='csvhandler',
      version=VERSION,
      url='https://github.com/bantalon/csvhandler',
      author="Alon Herbst",
      author_email="bantalon@gmail.com",
      description="A command-line utility and Python API for manipulating CSV data, eg plucking columns and reordering them.  It's a bit like the unix utility 'cut'",
      license='MIT',
      long_description=open('README.rst').read(),
      packages=find_packages(exclude=["tests*"]),
      scripts=['bin/csvhandler'])
