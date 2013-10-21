.. lxml-wrapper documentation master file, created by
   sphinx-quickstart on Mon Oct 21 15:04:18 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to lxml-wrapper's documentation!
========================================

Contents:

.. toctree::
   :maxdepth: 2

Installation
============

.. code-block:: sh

   pip install lxml-wrapper

Usage
=====

.. code-block:: python

   from lxmlwrapper import E, etree
   e = E('root', param='foo').add(
           E('SubElement', param='bar').add('just text')
       )
   print etree.tostring(e)
   <root param="foo"><SubElement param="bar">just text</SubElement></root>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

