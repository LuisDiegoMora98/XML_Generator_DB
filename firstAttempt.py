from xml.etree.ElementTree import Element, SubElement, Comment, tostring

from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

top = Element('Operaciones')

children = [
    Element('FechaOperacion', Fecha=str(i))
    for i in range(3)
    ]

top.extend(children)

print(prettify(top))
