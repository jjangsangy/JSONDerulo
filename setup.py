# -*- coding: utf-8 -*-
"""
JSONDerulo
============
A JSON serialization that is dirty to talk about

:copyright: (c) 2015 Sang Han
"""

from setuptools import setup

setup(
    name='JSONDerulo',
    description='A JSON serialization that is dirty to talk about',
    long_description=open('README.md', 'rb').read().decode('utf-8'),
    author='Sang Han',
    license='Apache License 2.0',
    url='https://github.com/jjangsangy/JSONDerulo',
    author_email='jjangsangy@gmail.com',
    include_package_data=True,
    version='1',
    packages=['JSONDerulo'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'derulo = JSONDerulo.__main__:main'
        ]
    },
)
