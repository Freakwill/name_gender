# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='name_gender',
    version='0.1',
    url='https://github.com/Freakwill/name_gender',
    license='MIT',
    author='William Song',
    description='Name => Gender',
    long_description=__doc__,
    install_requires=[
        'numpy',
        'pandas'
    ],
    tests_require = ['nose', 'pytest'],
    py_modules=['name_gender'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'TOPIC :: SCIENTIFIC/ENGINEERING :: ARTIFICIAL INTELLIGENCE',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
