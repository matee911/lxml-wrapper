#!/usr/bin/env python

from distutils.core import setup
# http://pypi.python.org/pypi?%3Aaction=list_classifiers
setup(name='lxml-wrapper',
      description='lxml wrapper that simplifies xml generation code.',
      keywords='lxml wrapper dsl',
      version='0.3.4',
      license='BSD',
      url='http://github.com/matee911/lxml-wrapper', # home page for the package
      download_url='http://github.com/matee911/lxml-wrapper/downloads',
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
      
      
      Now with .add_if and .add_for methods:
      
      E('root').add_if(1==1, E('child')) -> <root><child /></root>
      
      E('root').add_if(1==0, E('child')) -> <root/>
      
      E('root').add_for([1,2], lambda item: E('item', attr=item)) -> <root><item attr="1"/><item attr="2"/></root>
      
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
