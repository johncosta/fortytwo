#/usr/bin/env python
import os
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

test_requirements = []
setup(
    name="fortytwo",
    version='0.0.1',
    description="This does absolutely nothing but sleep from 0 to 42 seconds.",
    packages=[''],
    install_requires=[''] + test_requirements,
    scripts  = [
        'bin/fortytwo'
    ],
    zip_safe=False,
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Other Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
    )
