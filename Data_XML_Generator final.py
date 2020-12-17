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
    dataset = pd.read_csv('pokemon.csv')

    names = dataset['name']
    namesList = names[0:len(datesList)]
    
    #Primary account number
    numeroCuentaList = r.sample(range(10000000,99999999),len(datesList)) 
    
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
    
    movementBusinessList = ['Zara', 'Pequeño Mundo', 'MaxiPali','MaxMenos','Farmacia La Bomba','Ferreteria El Buen Pastor', 'Gimnasio SoloGood',
                            'El REY','Cemaco','Hotel Catalina','Amazon', 'Wish', 'CRAutos','Soda del Pueblo', 'Pulpería del Chino Antonio','Aliss']
    
    #Relationship_ID
    ParentezcoList = ["Padre", "Madre", "Hijo", "Hija", "Hermano", "Hermana", "Amigo", "Amiga", "Pareja"]
    
    #Final Date - Saving Account
    randNumberList = range(2,12)
    
    #Password lists
    randDigitList = ['$','%','@','&','/','(',')','ª','*']
    randNumList = range(000,999)

    #Hash to evaluate all accounts final balance
    hashCuenta = dict()

    
#Main Structure: Nodes(persona, cuenta, beneficiarios)      
    root= ET.Element('Operaciones')
    nodesList = []
    
    for i in range(0,31): #Since August has 31 days it is taken as the base month to create all primary accounts
     
        fechaOperacion = ET.Element('FechaOperacion', Fecha= datesList[i])
        cedula =  str(valorDocumentoIdentidadDelClienteList[i])
        persona = ET.Element('Persona'
                             ,TipoDocuIdentidad = str(tipoDocuIdentidadList[i])
                             ,Nombre = namesList[i]
                             ,ValorDocumentoIdentidad = cedula
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
                                  ,MontoAhorro = str(r.choice(montoAhorro))
                                  ,DiaAhorro = str(r.choice(randSavingDay))
                                  ,FechaFinal = str(datetime.strptime(datesList[i],'%m/%d/%Y') + relativedelta(months=r.choice(randNumberList)))
                                  ,Descripcion = r.choice(descriptionSavingAccountList))
        
        usuario = ET.Element('Usuario'
                               ,Usuario = namesList[i].lower()
                               ,Password = r.choice(randDigitList) + namesList[i].lower() + str(r.choice(randNumList))
                               ,Email = str.lower(email(names[i])))
        beneficiarioList = []
        
        for n in range(0,3):
            beneficiarioCed = ValorDocumentoIdentidadBeneficiario = str(r.choice(valorDocumentoIdentidadDelClienteList))
            while(beneficiarioCed == cedula):    #If owner's doc id is equal to new beneficiary doc Id, then change that beneficiary doc Id to avoid owner-beneficiary relation on same account
                beneficiarioCed =  str(r.choice(valorDocumentoIdentidadDelClienteList))
            beneficiario = ET.Element('Beneficiario'
                                    ,NumeroCuenta = str(r.choice(numeroCuentaList))
                                    ,ValorDocumentoIdentidadBeneficiario = beneficiarioCed
                                    ,ParentezcoId = r.choice(ParentezcoList)
                                    ,Porcentaje = str(r.randint(25,33))
                                    )
            beneficiarioList.append(beneficiario)
                                    
                                
                                
#first list of movements. This list is used to add at least one movement of each type to all accounts.
        movementsList = []

        numCuenta = str(numeroCuentaList[i])
        monto = str(r.randint(6000000,10000000))
        montoMovs = 0
        montoMovs += int(monto)
        hashCuenta[numCuenta] = montoMovs
        
        movementsList.append(ET.Element('Movimientos'
                                        ,Tipo = str(4)
                                        ,CodigoCuenta = numCuenta
                                        ,Monto = monto #6.000.000 is the minimum amount to ensure that in a scenario where all the movements were debits, the final balance (of this month) will be 0
                                        ,Descripcion = 'Banco Liga Pokemon'))
        for x in range(0,6):
            
            if(movementDescList[x] == 'Compra' or movementDescList[x] == 'Devolucion de Compra' ):
                Descripcion1 = r.choice(movementBusinessList)
            elif(movementDescList[x] in ["Retiro Ventana", "Deposito en ATM","Deposito Ventana", "Retiro ATM"]):
                Descripcion1 = 'Banco Liga Pokemon'
            else:
                Descripcion1 = movementDescList[x]
            

            montom = str(r.randint(100000,1000000))
            if x in (0, 1, 2):
                hashCuenta[numCuenta] -= int(montom)
            else:
                hashCuenta[numCuenta] += int(montom)
            
            movimiento = ET.Element('Movimientos'
            ,Tipo = str(x)
            ,CodigoCuenta = str(numeroCuentaList[i])
            ,Monto = montom
            ,Descripcion = Descripcion1
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
        
        for x in range(1,100):

            listacuentas = list(hashCuenta.keys())
            randCuenta = r.randint(0, len(listacuentas)-1)
            randTipo = r.randint(0,5)
            randMonto = str(r.randint(10000,500000))

            if(randTipo in (0, 1, 2)):
                hashCuenta[str(listacuentas[randCuenta])] -= int(randMonto)
            else:
                hashCuenta[str(listacuentas[randCuenta])] += int(randMonto)
            
            if(movementDescList[randTipo] == 'Compra' or movementDescList[randTipo] == 'Devolucion de Compra' ):
                Descripcion1 = r.choice(movementBusinessList)
            elif(movementDescList[randTipo] in ["Retiro Ventana", "Deposito en ATM","Deposito Ventana", "Retiro ATM"]):
                Descripcion1 = 'Banco Liga Pokemon'
            else:
                Descripcion1 = movementDescList[randTipo]
            
            movimiento = ET.Element('Movimientos'
            ,Tipo = str(randTipo)
            ,CodigoCuenta = str(listacuentas[randCuenta])
            ,Monto = randMonto
            ,Descripcion = Descripcion1)  
            
            movementsList2.append(movimiento)

        fechaOperacion.extend(movementsList2)

        nodesList.append(fechaOperacion)
         
    root.extend(nodesList)
    
#Writing XML File
    tree = ET.ElementTree(root)
    with open(fileName, 'wb') as files:
            tree.write(files)
        
GenerateXML('xmlTest.xml')
    


