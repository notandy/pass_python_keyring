#!/usr/bin/env python

from setuptools import setup

setup(
    name='pass_python_keyring',
    version='1.1',
    description=u"pass backend for python keyring lib",
    long_description=open('README.md').read(),
    url='http://github.com/notandy/pass_python_keyring',
    author='Andrew Karpow',
    author_email='andy@ndyk.de',
    license='PSF and MIT',
    keywords=['pass', 'password', 'keyring'],
    py_modules=['pass'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    setup_requires=['setuptools>=0.6c11'],
)
