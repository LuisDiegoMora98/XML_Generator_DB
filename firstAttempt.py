from xml.etree.ElementTree import Element, SubElement, Comment, tostring

from xml.etree import ElementTree
from xml.dom import minidom
from datetime import datetime, timedelta
from collections import OrderedDict

def getDatesList(pIntervalListDate):
    """Entry must be a list like this: ["2020-06-01", "2020-11-1"]
                                        start ↑    ->   end ↑
    The function returns a list with string dates of the range between the first position and second position on the entry list"""
    start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in pIntervalListDate]
    datesList = list(OrderedDict(((start + timedelta(_)).strftime("%Y-%m-%d"), None) for _ in range((end - start).days)).keys())
    return datesList

def prettify(elem):
    #Return a pretty-printed XML string for the Element.
    
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

datesList = getDatesList(["2020-06-01", "2020-11-1"])

top = Element('Operaciones')
listaFechas = []
children = [
    Element('FechaOperacion', Fecha=datesList[date])
    for date in range(len(datesList))
    ]

top.extend(children)

print(prettify(top))





