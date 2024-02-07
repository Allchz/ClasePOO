def Menu(tema):
    print("+++++++++Menú+++++++++")
    print("1. Crear "+tema)
    print("2. Mostra "+tema)
    print("3. Actualizar " + tema)
    print("4. Borrar "+tema)
    print("5. Salir ")

def Ingresar(lista,tema):
    print("--INGRESAR --")
    variable= input("Ingresa el nombre: ")
    diccionario={}
    diccionario[tema]=variable
    lista.append(diccionario)
    print(diccionario)

def Mostrar(tema, lista):
    print("----Mostrar--- ")
    for tema in lista:
        print("- Nombre :" + lista[tema])

    


carreras = []
seguir = True
while seguir:
    Menu("Carrera")
    opcion = input("Ingrese su opcion: ")

    if opcion.isdi


    


    


