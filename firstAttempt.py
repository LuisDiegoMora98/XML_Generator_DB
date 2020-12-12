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

#Load lists with info to fill on the regsiters
datesList = getDatesList(["2020-06-01", "2020-11-1"])

Operaciones = Element('Operaciones')
FechasOperaciones = []
for date in range(len(datesList)):                                                  #Iteratss all the dates
    FechaOperacion = Element('FechaOperacion', Fecha=datesList[date])
    Persona1 = Element('Persona', Campos="{Añadir campos y valores}")
    Persona2 = Element('Persona', Campos="{Añadir campos y valores}")
    Cuenta = Element('Cuenta', Campos="{Añadir campos y valores}")
    Beneficiario = Element('Beneficiario', Campos="{Añadir campos y valores}")
    FechaOperacion.append(Persona1)
    FechaOperacion.append(Persona2)
    FechaOperacion.append(Cuenta)
    FechaOperacion.append(Beneficiario)
    Movs = []
    #For con todos los movs que se desean aadir (Puede sacarse con un intervalo de movs al dia y con un random insertar esos movs)
    for i in range(14):
        Movs.append(Element('Movimiento', Campos="{Añadir campos y valores}"))
    FechaOperacion.extend(Movs)
    FechasOperaciones.append(FechaOperacion)
Operaciones.extend(FechasOperaciones)

print(prettify(Operaciones))





