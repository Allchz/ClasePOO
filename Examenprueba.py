def validarentero():

    while True:
        variable = input("Ingrese la opcion:")
        if variable.isdigit():
            return int(variable)
        else:
            print("Ingrese un numero ")


def menu():
    print("---Elija el estado de contrato---")
    print("1.En Espera")
    print("2. En Proceso")
    print("3. Finalizado")

def informacion():
    dicontrat={}
    print("--CONTRATO")
    dicontrat["Empleado"]= input("Ingrese el nombre ")
    dicontrat["Metros de Aseao"]= input("Ingrese la cantidad de metros se aseo ")
    dicontrat["Cliente"]=input(" Clinte (Nombre completo por favor) ")
    dicontrat["DNI"]=input("Ingrese el DNI del cliente ")
    dicontrat["Precio"]=input("Ingrese el precio ")

    menu()
    opcion= validarentero()

    if opcion==1:
        dicontrat["Estado Contrato"]="En Espera"
        print("Contrato en Espera")
    elif opcion==2:
        dicontrat["Estado Contrato"] = "En Proceso"
        print("Contrato en Proceso")
    elif opcion==3:
        dicontrat["Estado Contrato"] = "Finalizado"
        print("Contrato Finalizado")
    else:
        print("Opcion invalida")

    return dicontrat

def menuvisualizar():
    print("----VISUALIZAR CONTRATOS------")
    print("1. Visualizar Todos los contratos")
    print("2. Visualizar contrato en especficico")

contratos=[]

while True:

    contrato = informacion()

    contratos.append(contrato)

    continuar= input("Desea agregar Mas contratos "
                     "Si /No\n:  ")
    if continuar.upper()=="NO":
        break

menuvisualizar()
opcion= validarentero()

if opcion==1:
    for contrato in contratos:
        print("-------------------------------------")
        for x,y in contrato.items():
            print(x,y)

if opcion==2:
    estado=input("Ingrese el estado del contrato: ")
    encontrado= False

    for contrato in contratos:
        if contrato.get("Estado Contrato")==estado:
            encontrado=True
            print("Contrato encontrado")
            for x, y in contrato.items():
                print("-------------")
                print(x,y)

        else:
            print("Contrato no encontrado")








