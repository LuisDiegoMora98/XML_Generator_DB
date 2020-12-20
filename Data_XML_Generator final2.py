import xml.etree.ElementTree as ET
import pandas as pd
import random as r
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def printLista(lista):
    for i in range(len(lista)):
        print(str(i + 1) + ": " + str(lista[i]))

def changeDateFormat(lista):
    for date in lista:
        date.replace("/", "-")
    return lista

def GenerateXML(fileName):
    
  
#Data   

    #Transactions date range
    datesList = pd.date_range(start="2020-08-01",end="2020-12-31").strftime("%m-%d-%Y").tolist()
    datesList = changeDateFormat(datesList)
    
    #Persons id
    valorDocumentoIdentidadDelClienteList = r.sample(range(99999999),128)       #128 elements so 31*4 = persons created will be fulfilled succesfully
    
    #Names
    dataset = pd.read_csv('C:/Users/aguil/Dropbox/My PC (LAPTOP-1OL20O36)/Downloads/XML_Generator_DB-main/pokemon.csv')

    names = dataset['name']
    namesList = names[0:len(datesList)]
    
    #Primary account number
    numeroCuentaList = r.sample(range(10000000,99999999), 31)
    
    #Saving account number
    numeroCuentaAhorroList = r.sample(range(10000000,99999999),len(datesList))

    #Saving account amount
    montoAhorro = range(10000,200000, 10000)

    #Saving account description
    descriptionSavingAccountList = ['Vacaciones', 'Piedra de evolución Pokemon', 'Pociones y Antidotos', 'Bicicleta', 'Pokedex', 'Liga Pokemon']

    #Saving day
    randSavingDay = range(1,30,1)

    #Primary account type / persons id type
    tipoCuentaIdList = [] 
    tipoDocuIdentidadList = [] 
    for i in range(0, len(datesList)):
        tipoCuentaIdList.append(r.randint(1,3))
        tipoDocuIdentidadList.append(r.randint(1,6))
        
    #Birthdate
    fechas = pd.date_range(start='1950-01-01', end='2002-12-31').strftime('%m-%d-%Y').tolist()
    fechas = changeDateFormat(fechas)
    fechaNacimientoList = r.sample(fechas, len(datesList))
    fechaNacimientoList = changeDateFormat(fechaNacimientoList)
    #Email
    
    def email(name):
        prefix = name
        
        domains = ['gmail.com','yahoo.com', 'outlook.com', 'hotmail.com']
        domain = r.choice(domains)
    
        return prefix + '@' + domain
    
    #Telephones
    telephoneList = r.sample(range(77777777,88888888),len(datesList)) 
    telephoneList2 = r.sample(range(77777777,88888888),len(datesList)) 
    #Movements
    movementsList = r.randint(1,9)
    
    #Movements description
    movementDescList = ["Compra", "Retiro ATM", "Retiro Ventana", "Deposito en ATM",
                         "Deposito Ventana", "Devolucion de Compra", "Interes del mes sobre saldo minimo",
                         "Comision exceso de operacion en CH", "Comision exceso de operacion en CA"]
    
    #Relationship_ID
    ParentezcoList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
#Final Date - Saving Account
    randNumberList = range(2,12)

#Main Structure: Nodes(persona, cuenta, beneficiarios)      
    root= ET.Element('Operaciones')
    nodesList = []
    
    
#Final person/account list to choose beneficiaries

    PersonlistAfterRandomSelection = []
    AccountListAfterRandomSelection = []
    
    personCount = 0        #To take docsIds for persons below
    #Prints to troubleshoot
    print("Lista de cedulas existentes:\n")
    printLista(valorDocumentoIdentidadDelClienteList)
    print("\n**************************************************\nFin Lista de cedulas\n**************************************************\n")

    for i in range(0,31): #Since August has 31 days it is taken as the base month to create all primary accounts

        fechaOperacion = ET.Element('FechaOperacion', Fecha= datesList[i])

        for k in range(0, 4):    #NEW
            docId = str(valorDocumentoIdentidadDelClienteList[personCount])
            print("DocID de persona " + str(personCount + 1) + "= " + docId)
            persona = ET.Element('Persona'
                                ,TipoDocuIdentidad = str(tipoDocuIdentidadList[personCount])
                                ,Nombre = namesList[personCount]
                                ,ValorDocumentoIdentidad = docId
                                ,FechaNacimiento = fechaNacimientoList[personCount]
                                ,Email = str.lower(email(names[personCount]))
                                ,Telefono1 = str(telephoneList[personCount])
                                ,Telefono2 = str(telephoneList2[personCount]))
            fechaOperacion.append(persona)
            PersonlistAfterRandomSelection.append(docId)
            personCount += 1
        print("Ultimo id de persona aniadido deberia ser: " + str(valorDocumentoIdentidadDelClienteList[personCount - 1]))
        numCuenta = str(numeroCuentaList[i])
        cuenta = ET.Element('Cuenta'
                            ,ValorDocumentoIdentidadDelCliente = str(valorDocumentoIdentidadDelClienteList[personCount - 1])
                            ,TipoCuentaId = str(tipoCuentaIdList[i])
                            ,NumeroCuenta = numCuenta)
         
        AccountListAfterRandomSelection.append(numCuenta)

        fechaFinalSA = str(datetime.strptime(datesList[i],'%m-%d-%Y') + relativedelta(months=r.choice(randNumberList)))
        fechaFinalSA.replace("/","-")

        cuentaAhorro = ET.Element('CuentaAhorro'
                                  ,NumeroCuentaPrimaria = str(numCuenta)
                                  ,NumeroCuentaAhorro = str(numeroCuentaAhorroList[i])
                                  ,MontoAhorro = str(r.choice(montoAhorro))
                                  ,DiaAhorro = str(r.choice(randSavingDay))
                                  ,FechaFinal = fechaFinalSA
                                  ,Descripcion = r.choice(descriptionSavingAccountList))
        fechaOperacion.append(cuentaAhorro)

        print("Personas creadas hasta ahora: ")     #NEW
        printLista(PersonlistAfterRandomSelection)   
                
        beneficiarioList = []

        beneficiariosPorFecha = []
        subListIDs = PersonlistAfterRandomSelection[:-1]
        print("Sublista antes de beneficiarios = ")
        printLista(subListIDs)
        print("\n-------------------------\nFin SubLista que excluye el dueño de cuenta\n")

        #********************************************               ADD BENEFICIARIES       *******************************************************
        for n in range(0,3):
            beneficiarioCed = r.choice(subListIDs)
            
            while(beneficiarioCed in beneficiariosPorFecha):    #Not duplicated beneficiaries
               beneficiarioCed =  r.choice(subListIDs)
            beneficiario = ET.Element('Beneficiario'
                                    ,NumeroCuenta = numCuenta
                                    ,ValorDocumentoIdentidadBeneficiario = beneficiarioCed
                                    ,ParentezcoId = str(r.choice(ParentezcoList))
                                    ,Porcentaje = str(r.randint(25,33))
                                    )
            beneficiariosPorFecha.append(beneficiarioCed)
            beneficiarioList.append(beneficiario)
         
            
        usuario = ET.Element('Usuario'
                            ,User = str(namesList[personCount - 1])
                            ,Pass = str(valorDocumentoIdentidadDelClienteList[personCount - 1])
                            ,Email = str.lower(email(names[personCount - 1]))
                            ,ValorDocumentoIdentidad = str(valorDocumentoIdentidadDelClienteList[personCount - 1])
                            ,EsAdministrador = str(r.randint(0,1))
                            )
        usuarioBool = r.randint(0,2)
        if(usuarioBool == 1):
            usuarioPuedeVer = ET.Element('UsuarioPuedeVer'
                            ,User = str(valorDocumentoIdentidadDelClienteList[personCount - 1])
                            ,Cuenta = numCuenta
                            )

            fechaOperacion.append(usuarioPuedeVer)


#first list of movements. This list is used to add at least one movement of each type to all accounts.
        movementsList = []
        movementsList.append(ET.Element('Movimientos'
                                        ,Tipo = str(4)
                                        ,CodigoCuenta = str(numeroCuentaList[i])
                                        ,Monto = str(r.randint(6000000,10000000)) #6.000.000 is the minimum amount to ensure that in a scenario where all the movements were debits, the final balance (of this month) will be 0
                                        ,Descripcion = movementDescList[4]))
        for x in range(0,6):           
            movimiento = ET.Element('Movimientos'
            ,Tipo = str(x)
            ,CodigoCuenta = str(numeroCuentaList[i])
            ,Monto = str(r.randint(100000,1000000))
            ,Descripcion = movementDescList[x]
            )
            
            movementsList.append(movimiento)

#Building XML structure

        fechaOperacion.append(cuenta)
        fechaOperacion.extend(beneficiarioList)    
        fechaOperacion.extend(movementsList)
        fechaOperacion.append(usuario)
        nodesList.append(fechaOperacion)
           
#Second list of movements. This one is used to add random movements to random accounts 
    for i in range(31,len(datesList)):
        movementsList2 = []
        
        fechaOperacion = ET.Element('FechaOperacion', Fecha= datesList[i])
        
        for x in range(1,20):
            
            randCuenta = r.randint(0, len(numeroCuentaList)-1)
            randTipo = r.randint(0,5)
            
            movimiento = ET.Element('Movimientos'
            ,Tipo = str(randTipo)
            ,CodigoCuenta = str(AccountListAfterRandomSelection[randCuenta])
            ,Monto = str(r.randint(10000,500000))
            ,Descripcion = movementDescList[randTipo])  
            movementsList2.append(movimiento)

        fechaOperacion.extend(movementsList2)

        nodesList.append(fechaOperacion)
         
    root.extend(nodesList)


    
#Writing XML File
    tree = ET.ElementTree(root)
    with open(fileName, 'wb') as files:
            tree.write(files)
        
GenerateXML('xmlTest.xml')
    
import webbrowser
new = 2 # open in a new tab, if possible
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
#open an HTML file on my own (Windows) computer

url = "file://C:/Users/aguil/Dropbox/My PC (LAPTOP-1OL20O36)/Downloads/XML_Generator_DB-main/xmlTest.xml"
webbrowser.get(chrome_path).open(url,new=new)
