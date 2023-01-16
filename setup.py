# coding=utf-8
"""
File: setup.py
Created on 2023/1/16 15:57
__author__= yangh
__remark__=
"""

from setuptools import setup
setup(
    name='pytest-yh-plugins',
    url='',
    version='1.0',
    author="yh",
    author_email='',
    description='turn . into √，turn F into x',
    long_description='print result on terminal turn . into √，turn F into x using hook',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    py_modules=['pytest_yh_plugins'],
    keywords=[
        'pytest', 'py.test', 'pytest-yh-plugins',
    ],

    install_requires=[
        'pytest'
    ],
    entry_points={
        'pytest11': [
            'change-report = pytest_yh_plugins',
        ]
    }
)
