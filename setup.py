#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import setup, find_packages

requirements = [
    'django',
    'ipython'
]

setup(
    name="onlinepetition",
    version="1.0",
    author="Online",
    description="Simple system for registering and validating people signing an online petition.",
    keywords="django online petition",
    packages=find_packages(),
    zip_safe=False,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    include_package_data=True,
)
