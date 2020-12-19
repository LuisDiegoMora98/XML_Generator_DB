import xml.etree.ElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    #Return a pretty-printed XML string for the Element.
    
    rough_string = ET.ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

#Listas de Informacion
tipoDocs = ["Cedula Nacional","Cedula Residente", "Pasaporte", "Cedula Juridica", "Permiso de Trabajo", "Cedula Extranjera"]
tipoMonedas = ["Colones","Dolares", "Euros"]
simbolos = ["₡", "$", "€"]
Parentezcos = ["Padre", "Madre", "Hijo", "Hija", "Hermano", "Hermana", "Amigo", "Amiga", "Pareja"]
NombresCuentaAhorro = ["Proletario", "Profesional","Exclusivo"]
SaldoMinimo_CA = ["25000.00", "50000.00", "100000.00"]
MultaSaldoMinimo_CA = ["3000.00", "3000.00", "3000.00"]
CargoMensual_CA = ["5000", "15000", "30000"]
NumRetiroHumano_CA = ["5", "5", "5"]
NumRetirosAutomatico_CA = ["8", "8", "8"]
ComisionHumano_CA = ["300", "500", "1000"]
ComisionAutomatico_CA = ["300", "500", "1000"]
Interes_CA = ["10", "15", "20"]
NombreTipoMovimientos_CA = ["Compra", "Retiro ATM", "Retiro Ventana", "Deposito en ATM",
                         "Deposito Ventana", "Devolucion de Compra", "Interes del mes sobre saldo minimo",
                         "Comision exceso de operacion en CH", "Comision exceso de operacion en CA"]
TipoMov = ["Debito", "Credito"]
TipoMovimientoCuentaAhorro = ["Deposito por ahorro", "Deposito por redencion de intereses", "Redencion de la CO"]

TipoEvento = ["Insertar Beneficiarios","Modificar Beneficiario","Eliminar (desactivar) Beneficiario","Insertar CO","Modificar CO","Eliminar (desactivar) CO"]

#XML
Catalogos = ET.Element('Catalogos')
Tipo_Doc = ET.SubElement(Catalogos, 'TipoDoc')
for docId in range(len(tipoDocs)):
    Tipo_Doc.append(ET.Element("TipoDocuIdentidad", Id = str(docId + 1), Nombre=tipoDocs[docId]))

Tipo_Moneda = ET.SubElement(Catalogos, 'TipoMoneda')
for monedaId in range(len(tipoMonedas)):
    Tipo_Moneda.append(ET.Element("TipoMoneda", Id = str(monedaId + 1), Nombre=tipoMonedas[monedaId], Simbolo=simbolos[monedaId]))

Parentezco = ET.SubElement(Catalogos, 'Parentezcos')
for parentezcoId in range(len(Parentezcos)):
    Parentezco.append(ET.Element("Parentezco", Id = str(parentezcoId + 1), Nombre=Parentezcos[parentezcoId]))

Tipo_Cuenta_Ahorro = ET.SubElement(Catalogos, 'Tipo_Cuenta_Ahorro')
for data in range(len(NombresCuentaAhorro)):
    Tipo_Cuenta_Ahorro.append(ET.Element('TipoCuentaAhorro', Id=str(data + 1), Nombre=NombresCuentaAhorro[data], IdTipoMoneda="1", SaldoMinimo=SaldoMinimo_CA[data],
                                      MultaSaldoMin=MultaSaldoMinimo_CA[data], CargoMensual=CargoMensual_CA[data], NumRetiroHumano=NumRetiroHumano_CA[data],
                                      NumRetirosAutomatico=NumRetirosAutomatico_CA[data], ComisionHumano=ComisionHumano_CA[data], ComisionAutomatico=ComisionAutomatico_CA[data],
                                      Interes=Interes_CA[data]))

Tipo_Movimientos = ET.SubElement(Catalogos, 'TipoMovimientos')
for mov in range(len(NombreTipoMovimientos_CA)):
    Tipo_Movimientos.append(ET.Element('TipoMovimiento', Id=str(mov +1),
                                    Nombre=NombreTipoMovimientos_CA[mov], Tipo=TipoMov[((mov//3)%2)]))

Tipo_MovimientosCuentaAhorro = ET.SubElement(Catalogos, 'TiposMovimientoCuentaAhorro')
for movCO in range(len(TipoMovimientoCuentaAhorro)):
    Tipo_MovimientosCuentaAhorro.append(ET.Element('Tipo_Movimiento', Id=str(movCO +1),
                                    Nombre=TipoMovimientoCuentaAhorro[movCO]))

Tipo_Evento = ET.SubElement(Catalogos, 'TiposEvento')
for tipo in range(len(TipoEvento)):
    Tipo_Evento.append(ET.Element('TipoEvento', Id=str(tipo +1),
                                    Nombre=TipoEvento[tipo]))

#Writing XML File
    tree = ET.ElementTree(Catalogos)
    with open("Catalogo-Tarea-3.xml", 'wb') as files:
            tree.write(files)

import webbrowser
new = 2 # open in a new tab, if possible
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# open an HTML file on my own (Windows) computer
url = "file://C:/Users/aguil/Dropbox/My PC (LAPTOP-1OL20O36)/Downloads/XML_Generator_DB-main/Catalogo-Tarea-3.xml"
webbrowser.get(chrome_path).open(url,new=new)
