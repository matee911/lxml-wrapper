#!/usr/bin/env python

from lxmlwrapper import __VERSION__
from distutils.core import setup
# http://pypi.python.org/pypi?%3Aaction=list_classifiers
setup(name='lxml-wrapper',
      description='lxml wrapper that simplifies xml generation code.',
      keywords='lxml wrapper dsl',
      version=__VERSION__,
      license='BSD',
      url='http://github.com/matee911/lxml-wrapper', # home page for the package
      download_url='https://github.com/matee911/lxml-wrapper/archive/%s.tar.gz' % __VERSION__,
      author='Mateusz `matee` Pawlik',
      author_email='matee@matee.net',
      long_description=open('README.rst').read(),
      requires=['lxml'],
      #package_dir={'':'src'},
      py_modules=['lxmlwrapper'],
      platforms=['Any'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
      ],)

