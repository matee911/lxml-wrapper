============
lxml-wrapper
============

:Info: See `github <http://github.com/matee911/lxml-wrapper/>`_ for the latest source.
:Author: matee

About
=====

This wrapper simplifies your Python xml generation code.

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
