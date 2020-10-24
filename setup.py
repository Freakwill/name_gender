# -*- coding: utf-8 -*-

from setuptools import setup

DESCRIPTION = "Name => Gender"

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()
 
KEYWORDS = "Naive Bayes"

setup(
    name = 'name_gender',
    py_modules = ['name_gender'],
    version = "0.1",
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    
    install_requires=[
        'numpy',
        'pandas'
    ],
    classifiers = [
        'License :: Public Domain',  # Public Domain
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'TOPIC :: SCIENTIFIC/ENGINEERING :: ARTIFICIAL INTELLIGENCE',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords = KEYWORDS,
    author = "William Song",
    author_email = "songcwzjut@163.com",
    url = "https://github.com/Freakwill/name_gender",
    license = "MIT",
    # packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)
