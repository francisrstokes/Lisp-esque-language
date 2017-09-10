# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lel-lang',

    version='0.0.1',

    description='Lel programming language(Lisp-esque language)',
    long_description=long_description,

    url='https://github.com/osaatcioglu/Lisp-esque-language',

    author='Ömer Saatcioglu',
    author_email='osaatcioglu@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Software Development :: Compilers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='compiler lisp lel parser ast tokenize',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['six'],

    extras_require={
        'dev': [],
        'test': [],
    },

    package_data={},

    entry_points={
        'console_scripts': [
            'pylel=pylel:package_main',
        ],
    },
)
