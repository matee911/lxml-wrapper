# -*- coding: utf-8 -*-

import unittest
from lxmlwrapper import E, SE, etree

to_s = etree.tostring

class TestSingleElement(unittest.TestCase):
    def test_element(self):
        e = E('root')
        s = '<root/>'
        self.assertEqual(to_s(e), s)
        
        e = E('root', foo='bar')
        s = '<root foo="bar"/>'
        self.assertEqual(to_s(e), s)
        
        e = E('root', bar=0)
        s = '<root bar="0"/>'
        self.assertEqual(to_s(e), s)
        
        e = E('root', baz=None)
        s = '<root baz=""/>'
        self.assertEqual(to_s(e), s)
        
class TestAddElement(unittest.TestCase):
    def test_add_element(self):
        e = E('root').add()
        s = '<root/>'
        self.assertEqual(to_s(e), s)
        
        e = E('root').add(E('child1'))
        s = '<root><child1/></root>'
        self.assertEqual(to_s(e), s)
        
        e = E('root').add(E('child1'), E('child2'))
        s = '<root><child1/><child2/></root>'
        self.assertEqual(to_s(e), s)
        
        e = E('root').add(E('child1'), E('child2'), E('child3'))
        s = '<root><child1/><child2/><child3/></root>'
        self.assertEqual(to_s(e), s)
        
    def test_add_none(self):
        e = E('root').add(None)
        s = '<root/>'
        self.assertEqual(to_s(e), s)
        
    def test_add_text(self):
        e = E('root').add('text')
        s = '<root>text</root>'
        self.assertEqual(to_s(e), s)
        
        e = E('root').add('text1', 'text2')
        s = '<root>text1text2</root>'
        self.assertEqual(to_s(e), s)
        
    def test_add_elem_text(self):
        e = E('root').add('text', E('child'))
        s = '<root>text<child/></root>'
        self.assertEqual(to_s(e), s)
        
        e = E('root').add('text1', 'text2', E('child'))
        s = '<root>text1text2<child/></root>'
        self.assertEqual(to_s(e), s)
        
    def test_add_elem_tail(self):
        e = E('root').add(E('child'), 'tail')
        s = '<root><child/>tail</root>'
        self.assertEqual(to_s(e), s)
        
        e = E('root').add(E('child'), 'tail1', 'tail2')
        s = '<root><child/>tail1tail2</root>'
        self.assertEqual(to_s(e), s)
        
        e = E('root').add(E('child1'), 'tail1', 'tail2', E('child2'))
        s = '<root><child1/>tail1tail2<child2/></root>'
        self.assertEqual(to_s(e), s)
        
    def test_add_elem_text_tail(self):
        e = E('root').add('text', E('child'), 'tail')
        s = '<root>text<child/>tail</root>'
        self.assertEqual(to_s(e), s)
        
        e = E('root').add('text1', 'text2', E('child'), 'tail1', 'tail2')
        s = '<root>text1text2<child/>tail1tail2</root>'
        self.assertEqual(to_s(e), s)

class TestSE(unittest.TestCase):
    """Testing subelement
    """
    def test_add(self):
        e = E('root')
        se = SE(e,'child')
        s = '<root><child/></root>'
        self.assertEqual(to_s(e), s)

    def test_add_with_text(self):
        e = E('root')
        se = SE(e,'child').add('text')
        s = '<root><child>text</child></root>'
        self.assertEqual(to_s(e), s)

    def test_add_with_elems(self):
        e = E('root')
        se = SE(e,'child').add(E('child2'))
        s = '<root><child><child2/></child></root>'
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
        s = '<root atr="100">text1<child atr="atr"><superchild atr="">sctext1</superchild>tail1tail2</child>tail<child atr="">text</child></root>'
        self.assertEqual(to_s(e), s)
    
class TestPrettyPrint(unittest.TestCase):
    def test_pretty_print(self):
        e = E('root').add(E('child'))
        s = """<root>
  <child/>
</root>
"""
        self.assertEqual(to_s(e, pretty_print=True), s)
        
        
if __name__ == '__main__':
    
    unittest.main()
