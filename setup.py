# -*- coding: utf-8 -*-
# Puppet-Diamond (c) Ian Dennis Miller

import os
import re
import codecs
from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return codecs.open(os.path.join(os.path.dirname(__file__), *rnames), 'r', 'utf-8').read()


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, read('puppet_diamond/__meta__.py'))
    return strval


setup(
    version=grep('__version__'),
    name='Puppet-Diamond',
    description="Puppet-Diamond can manage an IT Enterprise consisting of many Linux servers.",
    scripts=[
        "bin/pup",
        "bin/generate_sshd_keys.sh",
        "bin/get_submodules.sh",
    ],
    long_description=read('Readme.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 2.7",
        "Topic :: System :: Clustering",
        "Topic :: System :: Systems Administration",
    ],
    packages=find_packages(),
    include_package_data=True,
    keywords='',
    author=grep('__author__'),
    author_email=grep('__email__'),
    url=grep('__url__'),
    install_requires=read('requirements.txt'),
    license='MIT',
    zip_safe=False,
)
