#!/usr/bin/env python

from distutils.core import setup
import setuptools
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def read_requirements():
    return read('requirements.txt').splitlines()

package_dir = os.path.dirname(os.path.realpath(__file__))
packages = setuptools.find_packages(package_dir, exclude=("tests"))

setup(
    name='ExactHistogramSpecification',
    version='1.0',
    description='`Exact Histogram Specification` by Dinu Coltuc et al',
    url="https://github.com/jkschluesener/ExactHistogramSpecification",
    license='Apache License 2.0',
    author='StefanoD',
    maintainer='Jan K. Schluesener',
    maintainer_email='code@jkschluesener.xyz',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=packages,
    install_requires=read_requirements()
    )
