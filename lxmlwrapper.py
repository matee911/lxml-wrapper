# -*- coding: utf-8 -*-

"""
Now you can simplify your xml generation code.

Example XML:

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

Old way:

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

New way:

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
"""

__VERSION__ = '0.3.2'

from lxml import etree

def E(_tag, attrib=None, nsmap=None, **_extra):
    return _make_elem(_tag, attrib, nsmap, **_extra)
    
def SE(elem, _tag, attrib=None, nsmap=None, **_extra):
    e = _make_elem(_tag, attrib, nsmap, **_extra)
    elem.append(e)
    return elem
    
def _make_elem(_tag, attrib=None, nsmap=None, **_extra):
    for k,v in _extra.items():
        if isinstance(v, (int, long, float)):
            v = str(v)
        elif v is None:
            v = ''
        _extra[k] = v
    _E.TAG = _tag
    return _E(**_extra)

#
# Main magick class
#

class _E(etree.ElementBase):
    
    def add_if(self, condition, * elements):
        """Conditional add.
        
        Add given elements only if condition is true.
        """
        if condition:
            return self.add(* elements)
        else:
            return self
            
    def add_for(self, iterable, fun=lambda item: item):
        self.add(*[fun(item) for item in iterable])
        return self
    
    def add(self, * elements):
        """You can add ElementTrees or strings or even integers now."""
        
        if not elements: # .add()
            return self
        
        prev_elem = None
        text_elems = []
        
        for elem in elements:
            if elem is None: # we don't like nones
                continue
            
            if not isinstance(elem, (basestring, int, long, float)):
                # we have elemettree
                if prev_elem is not None:
                    # because we have previous elem
                    # we could append it now
                    if text_elems:
                        prev_elem.tail = "".join(text_elems)
                    self.append(prev_elem)
                    text_elems = []
                else:
                    # we haven't elementtree yet
                    # so we shoud join together text_elems
                    # assign them to self.text
                    # and clear
                    if text_elems:
                        self.text = "".join(text_elems)
                    text_elems = []
                prev_elem = elem
            else:
                # we have some text
                # so we can store it for later
                if isinstance(elem, (int, long, float)):
                    elem = str(elem)
                text_elems.append(elem)
        else:
            if elem is None: # we don't like nones
                return self
            
            if not isinstance(elem, (basestring, int, long, float)):
                # last element isn't string
                # so we shoud append it
                self.append(elem)
            else:
                # last element isn't element tree
                # so we should do something
                if prev_elem is not None:
                    if text_elems:
                        prev_elem.tail = "".join(text_elems)
                    self.append(prev_elem)
                    text_elems = []
                else:
                    if text_elems:
                        self.text = "".join(text_elems)
                    text_elems = []
        
        return self

