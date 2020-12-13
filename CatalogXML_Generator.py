from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    #Return a pretty-printed XML string for the Element.
    
    rough_string = ElementTree.tostring(elem, 'utf-8')
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

#XML
Catalogos = Element('Catalogos')
Tipo_Doc = SubElement(Catalogos, 'Tipo_Doc')
for docId in range(len(tipoDocs)):
    Tipo_Doc.append(Element("TipoDocuIdentidad", Id = str(docId + 1), Nombre=tipoDocs[docId]))

Tipo_Moneda = SubElement(Catalogos, 'TipoMoneda')
for monedaId in range(len(tipoMonedas)):
    Tipo_Moneda.append(Element("TipoMoneda", Id = str(monedaId + 1), Nombre=tipoMonedas[monedaId], Simbolo=simbolos[monedaId]))

Parentezco = SubElement(Catalogos, 'Parentezcos')
for parentezcoId in range(len(Parentezcos)):
    Parentezco.append(Element("Parentezco", Id = str(parentezcoId + 1), Nombre=Parentezcos[parentezcoId]))

Tipo_Cuenta_Ahorro = SubElement(Catalogos, 'Tipo_Cuenta_Ahorro')
for data in range(len(NombresCuentaAhorro)):
    Tipo_Cuenta_Ahorro.append(Element('TipoCuentaAhorro', Id=str(data + 1), Nombre=NombresCuentaAhorro[data], IdTipoMoneda="1", SaldoMinimo=SaldoMinimo_CA[data],
                                      MultaSaldoMin=MultaSaldoMinimo_CA[data], CargoMensual=CargoMensual_CA[data], NumRetiroHumano=NumRetiroHumano_CA[data],
                                      NumRetirosAutomatico=NumRetirosAutomatico_CA[data], ComisionHumano=ComisionHumano_CA[data], ComisionAutomatico=ComisionAutomatico_CA[data],
                                      Interes=Interes_CA[data]))

Tipo_Movimientos = SubElement(Catalogos, 'Tipo_Movimientos')
for mov in range(len(NombreTipoMovimientos_CA)):
    Tipo_Movimientos.append(Element('Tipo_Movimiento', Id=str(mov +1),
                                    Nombre=NombreTipoMovimientos_CA[mov], Tipo=TipoMov[((mov//3)%2)]))

print(prettify(Catalogos))
