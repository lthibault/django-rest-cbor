#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='drf_cbor',
    version='1.0.0',
    description='Django Rest Framework CBOR Renderer & Parser',
    author='lthibault',
    url='https://github.com/lthibault/django-rest-cbor',
    packages=find_packages(),
    install_requires=['django', 'cbor2', 'djangorestframework']
)