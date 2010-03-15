#!/usr/bin/env python

from distutils.core import setup
# http://pypi.python.org/pypi?%3Aaction=list_classifiers
setup(name='lxml-wrapper',
      description='lxml wrapper that simplifies xml generation code.',
      keywords='lxml wrapper',
      version='0.1b',
      license='BSD',
      url='http://github.com/matee911/lxml-wrapper', # home page for the package
      download_url='http://download.github.com/matee911-lxml-wrapper-5c40170.tar.gz',
      author='Mateusz `matee` Pawlik',
      author_email='matee@matee.net',
      long_description='''
      This wrapper simplifies your Python xml generation code.
      
      Example XML:
      
      <root attrib="10">
        text
        <child attrib="">
          childtext
        </child>
        tail
      </root>
      
      New way:
      
      E('root', attrib=10).add(
          'text', 
          E('child', attrib=None).add(
              'childtext'), 
          'tail')
      
      Old way:
      
      root = Element('root', attrib=str(10)) # cast to str
      root.text = 'text'
      child = SubElement(root, 'child', attrib=value or "") # change None to empty string
      child.text = 'childtext'
      child.tail = 'tail'
      
      ''',
      requires=['lxml'],
      #package_dir={'':'src'},
      py_modules=['lxmlwrapper'],
      platforms=['Any'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
      ],)
