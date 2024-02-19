def validarentero():
    variable=input("Ingrese la opcion:")

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
    orden={}
    print("--CONTRATO")
    orden["Empleado"]= input("Ingrese el nombre")
    orden["Metros de Aseao"]= input("Ingrese la cantidad de metros se aseo")
    orden["Cliente"]=input(" Clinte (Nombre completo por favor)")
    orden["DNI"]=input("Ingrese el DNI del cliente")
    orden["Precio"]=input("Ingrese el precio")

    menu()
    opcion= validarentero()

    if opcion==1:
        orden["Estado Contrato"]="En Espera"
    elif opcion==2:
        orden["Estado Contrato"] = "En Proceso"
    elif opcion==3:
        orden["Estado Contrato"] = "Finalizado"
    else:
        print("Opcion invalida")



ordenes=[]

while True:
    informacion()






