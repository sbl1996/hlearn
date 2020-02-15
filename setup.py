#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
from setuptools import find_packages, setup

# with open('requirements.txt') as f:
#     requirements = f.read().splitlines()

# Package meta-data.

NAME = 'hlearn'
IMPORT_NAME = 'hlearn'
DESCRIPTION = "HrvvI's utils for machine learning"
URL = 'https://github.com/sbl1996/hlearn'
EMAIL = 'sbl1996@126.com'
AUTHOR = 'HrvvI'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = [
    "numpy",
    "toolz",
]

DEPENDENCY_LINKS = [
]

# What packages are optional?

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.dirname(os.path.abspath(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's _version.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, IMPORT_NAME, '_version.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    dependency_links=DEPENDENCY_LINKS,
    # include_package_data=True,
    license='MIT',
)
