# -*- coding: utf-8 -*-
# http://lxml.de/FAQ.html#why-does-lxml-sometimes-return-str-values-for-text-in-python-2

from __future__ import unicode_literals
import unittest
from lxmlwrapper import E, SE, etree

to_s = etree.tostring

class TestSingleElement(unittest.TestCase):
    def test_element(self):
        e = E('root')
        s = b'<root/>'
        self.assertEqual(to_s(e), s)

        e = E('root', foo='bar')
        s = b'<root foo="bar"/>'
        self.assertEqual(to_s(e), s)

        e = E('root', bar=0)
        s = b'<root bar="0"/>'
        self.assertEqual(to_s(e), s)

        e = E('root', baz=None)
        s = b'<root baz=""/>'
        self.assertEqual(to_s(e), s)

        e = E('root', baz='Zażółć gęślą jaźń')
        s = b'<root baz="Za&#380;&#243;&#322;&#263; g&#281;&#347;l&#261; ja&#378;&#324;"/>'
        self.assertEqual(to_s(e), s)

class TestAddElement(unittest.TestCase):
    def test_add_element(self):
        e = E('root').add()
        s = b'<root/>'
        self.assertEqual(to_s(e), s)

        e = E('root').add(E('child1'))
        s = b'<root><child1/></root>'
        self.assertEqual(to_s(e), s)

        e = E('root').add(E('child1'), E('child2'))
        s = b'<root><child1/><child2/></root>'
        self.assertEqual(to_s(e), s)

        e = E('root').add(E('child1'), E('child2'), E('child3'))
        s = b'<root><child1/><child2/><child3/></root>'
        self.assertEqual(to_s(e), s)

    def test_add_none(self):
        e = E('root').add(None)
        s = b'<root/>'
        self.assertEqual(to_s(e), s)

    def test_add_text(self):
        e = E('root').add('text')
        s = b'<root>text</root>'
        self.assertEqual(to_s(e), s)

        e = E('root').add('text1', 'text2')
        s = b'<root>text1text2</root>'
        self.assertEqual(to_s(e), s)

    def test_add_elem_text(self):
        e = E('root').add('text', E('child'))
        s = b'<root>text<child/></root>'
        self.assertEqual(to_s(e), s)

        e = E('root').add('text1', 'text2', E('child'))
        s = b'<root>text1text2<child/></root>'
        self.assertEqual(to_s(e), s)

    def test_add_elem_tail(self):
        e = E('root').add(E('child'), 'tail')
        s = b'<root><child/>tail</root>'
        self.assertEqual(to_s(e), s)

        e = E('root').add(E('child'), 'tail1', 'tail2')
        s = b'<root><child/>tail1tail2</root>'
        self.assertEqual(to_s(e), s)

        e = E('root').add(E('child1'), 'tail1', 'tail2', E('child2'))
        s = b'<root><child1/>tail1tail2<child2/></root>'
        self.assertEqual(to_s(e), s)

    def test_add_elem_text_tail(self):
        e = E('root').add('text', E('child'), 'tail')
        s = b'<root>text<child/>tail</root>'
        self.assertEqual(to_s(e), s)

        e = E('root').add('text1', 'text2', E('child'), 'tail1', 'tail2')
        s = b'<root>text1text2<child/>tail1tail2</root>'
        self.assertEqual(to_s(e), s)

class TestSE(unittest.TestCase):
    """Testing subelement"""
    def test_add(self):
        e = E('root')
        se = SE(e,'child')
        s = b'<root><child/></root>'
        self.assertEqual(to_s(e), s)

    def test_add_with_text(self):
        e = E('root')
        se = SE(e,'child').add('text')
        s = b'<root><child>text</child></root>'
        self.assertEqual(to_s(e), s)

    def test_add_with_elems(self):
        e = E('root')
        se = SE(e,'child').add(E('child2'))
        s = b'<root><child><child2/></child></root>'
        self.assertEqual(to_s(e), s)


class TestRandomComplexExamples(unittest.TestCase):
    def test_complex(self):
        e = E('root', atr=100).add(
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
        s = b'<root atr="100">text1<child atr="atr"><superchild atr="">sctext1</superchild>tail1tail2</child>tail<child atr="">text</child></root>'
        self.assertEqual(to_s(e), s)

class TestPrettyPrint(unittest.TestCase):
    def test_pretty_print(self):
        e = E('root').add(E('child'))
        s = b"""<root>
  <child/>
</root>
"""
        self.assertEqual(to_s(e, pretty_print=True), s)


if __name__ == '__main__':
    unittest.main()

