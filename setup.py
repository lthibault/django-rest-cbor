#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-rest-cbor',
    version='0.0.1',
    description='Django Rest Framework CBOR Renderer & Parser',
    author='lthibault',
    url='https://github.com/lthibault/django-rest-cbor',
    packages=find_packages(),
    install_requires=['django', 'cbor2', 'djangorestframework']
)