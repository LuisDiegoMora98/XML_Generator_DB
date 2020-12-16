import xml.etree.ElementTree as ET
import pandas as pd
import random as r
from datetime import datetime, timedelta 
from dateutil.relativedelta import relativedelta


def GenerateXML(fileName):
    
  
#Data   

    #Transactions date range
    datesList = pd.date_range(start="2020-08-01",end="2020-12-31").strftime("%m/%d/%Y").tolist() 
    
    #Persons id
    valorDocumentoIdentidadDelClienteList = r.sample(range(10000000,99999999),len(datesList)) 
    
    #Names
    dataset = pd.read_csv('~/Downloads/archive/pokemon.csv')

    names = dataset['name']
    namesList = names[0:len(datesList)]
    
    #Primary account number
    numeroCuentaList = r.sample(range(10000000,99999999),len(datesList)) 
    
    #Saving account number
    numeroCuentaAhorroList = r.sample(range(10000000,99999999),len(datesList))
    
    #Primary account type / persons id type
    tipoCuentaIdList = [] 
    tipoDocuIdentidadList = [] 
    for i in range(0, len(datesList)):
        tipoCuentaIdList.append(r.randint(1,3))
        tipoDocuIdentidadList.append(r.randint(1,6))
        
    #Birthdate
    fechas = pd.date_range(start='1950-01-01', end='2002-12-31').strftime('%m/%d/%Y').tolist() 
    fechaNacimientoList = r.sample(fechas, len(datesList))
    
    #Email
    
    def email(name):
        prefix = name
        
        domains = ['gmail.com','yahoo.com', 'outlook.com', 'hotmail.com']
        domain = r.choice(domains)
    
        return prefix + '@' + domain
    
    #Telephones
    telephoneList = r.sample(range(77777777,88888888),len(datesList)) 
    
    #Movements
    movementsList = r.randint(1,9)
    
    #Movements description
    movementDescList = ["Compra", "Retiro ATM", "Retiro Ventana", "Deposito en ATM",
                         "Deposito Ventana", "Devolucion de Compra", "Interes del mes sobre saldo minimo",
                         "Comision exceso de operacion en CH", "Comision exceso de operacion en CA"]
    
    #Relationship_ID
    ParentezcoList = ["Padre", "Madre", "Hijo", "Hija", "Hermano", "Hermana", "Amigo", "Amiga", "Pareja"]
    
    #Final Date - Saving Account
    randNumberList = range(1,3)
    
    #Password lists
    randDigitList = ['$','%','@','&','/','(',')','ª','*']
    randNumList = range(000,999)

#Main Structure: Nodes(persona, cuenta, beneficiarios)      
    root= ET.Element('Operaciones')
    nodesList = []
    
    for i in range(0,31): #Since August has 31 days it is taken as the base month to create all primary accounts
     
        fechaOperacion = ET.Element('FechaOperacion', Fecha= datesList[i])
        persona = ET.Element('Persona'
                             ,TipoDocuIdentidad = str(tipoDocuIdentidadList[i])
                             ,Nombre = namesList[i]
                             ,ValorDocumentoIdentidad = str(valorDocumentoIdentidadDelClienteList[i])
                             ,FechaNacimiento = fechaNacimientoList[i]
                             ,Email = str.lower(email(names[i]))
                             ,Telefono1 = str(telephoneList[i])
                             ,Telefono2 = str(telephoneList[i+1]))

        cuenta = ET.Element('Cuenta'
                            ,ValorDocumentoIdentidadDelCliente = str(valorDocumentoIdentidadDelClienteList[i])
                            ,TipoCuentaId = str(tipoCuentaIdList[i])
                            ,NumeroCuenta = str(numeroCuentaList[i]))
               
        cuentaAhorro = ET.Element('CuentaAhorro'
                                  ,NumeroCuentaPrimaria = str(numeroCuentaList[i])
                                  ,NumeroCuentaAhorro = str(numeroCuentaAhorroList[i])
                                  ,FechaFinal = str(datetime.strptime(datesList[i],'%m/%d/%Y') + relativedelta(months=r.choice(randNumberList))))
        
        usuario = ET.Element('Usuario'
                               ,Usuario = namesList[i].lower()
                               ,Password = r.choice(randDigitList) + namesList[i].lower() + str(r.choice(randNumList))
                               ,Email = str.lower(email(names[i])))
        beneficiarioList = []
        
        for n in range(0,3):
            beneficiario = ET.Element('Beneficiario'
                                    ,NumeroCuenta = str(r.choice(numeroCuentaList))
                                    ,ValorDocumentoIdentidadBeneficiario = str(r.choice(valorDocumentoIdentidadDelClienteList))
                                    ,ParentezcoId = r.choice(ParentezcoList)
                                    ,Porcentaje = str(r.randint(25,33))
                                    )
            beneficiarioList.append(beneficiario)
                                    
                                
                                
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
        fechaOperacion.append(persona)
        fechaOperacion.append(cuenta)
        fechaOperacion.append(cuentaAhorro)
        fechaOperacion.append(usuario)
        fechaOperacion.extend(beneficiarioList)
        fechaOperacion.extend(movementsList)
        
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
            ,CodigoCuenta = str(numeroCuentaList[randCuenta])
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
    


