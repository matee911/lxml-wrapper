============
lxml-wrapper
============

:Author: matee
:Source: See `github <http://github.com/matee911/lxml-wrapper/>`_ for the latest source.
:Documentation: `lxml-wrapper@read-the-docs <http://lxml-wrapper.readthedocs.org/en/latest/>`_
:BugTracker: `Github issues <https://github.com/matee911/lxml-wrapper/issues>`_

.. image:: https://travis-ci.org/matee911/lxml-wrapper.png?branch=master
    :target: https://travis-ci.org/matee911/lxml-wrapper
    :alt: Build status
    
.. image:: https://coveralls.io/repos/matee911/lxml-wrapper/badge.png?branch=master 
    :target: https://coveralls.io/r/matee911/lxml-wrapper?branch=master
    :alt: Coverage

.. image:: https://pypip.in/v/lxml-wrapper/badge.png
    :target: https://crate.io/packages/lxml-wrapper/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/lxml-wrapper/badge.png
    :target: https://crate.io/packages/lxml-wrapper/
    :alt: Number of PyPI downloads

About
=====

This wrapper simplifies your Python xml generation code.

Changes
=======

add_if
------

::

  E('root').add_if(1==1, E('child')) # <root><child /></root>
  E('root').add_if(1==0, E('child')) # <root/>

add_for
-------

::

  E('root').add_for([1,2], lambda item: E('item', attr=item)) # <root><item attr="1"/><item attr="2"/></root>


Dependencies
============

- `lxml http://codespeak.net/lxml/` 

Installation
============

::

  pip install lxml-wrapper

Examples
========

XML
---

::

  <root atr="100">
    text1
    <child atr="atr">
      <superchild atr="">sctext1</superchild>
      tail1
      tail2
    </child>
    tail
    <child atr="">text</child>
  </root>

Old way
-------

::

  root = Element('root', atr=str(100))
  root.text = 'text1'
  child = SubElement(root, 'child', atr="atr")
  superchild = SubElement(root, 'superchild', atr="" if value is None else value)
  superchild.text = 'sctext1'
  superchild.tail = 'tail1'
  superchild.tail += 'tail2'
  child.tail = 'tail'
  child = SubElement(root, 'child', atr="")
  child.text = 'text'

New way
-------

::

  root = E('root', atr=100).add(
           'text1',
           E('child', atr="atr").add(
             E('superchild', atr=None).add('sctext1'),
             'tail1',
             'tail2'
           ),
           'tail',
           E('child', atr="").add(
               'text'
           )
       )
