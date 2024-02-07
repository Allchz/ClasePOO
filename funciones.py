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

def Mostrar(lista):
    print("----Mostrar--- ")
    print(lista)
def Actualizar(tema,lista):
    actualizar =input("Ingrese nombre de la "+" "+tema)
    nuevovalor = input("Ingrese el nuevo nombre de la "+" "+tema)

    indice=0
    for elemento in lista:
        if elemento[tema] == actualizar:
            elemento[tema] = nuevovalor
        print(elemento)

def Borrar(lista, tema):
    borra=input(" ingrese el elemento que desea borrar: ")
    indice=0
    encontrado= True

    for elemento in lista:
        if elemento[tema]== borra:
            encontrado=False
            break
        else:
            indice= indice+1
    if encontrado:
        lista.remove(lista[indice])
        print("Elemento Borrado")
    else:
        print("No existe")




carreras=[]

while True:
    Menu("Carrera")
    opcion= input(" ingrese su opcion: ")

    if opcion.isdigit():
        opcion=int(opcion)

        print("-------------------------------\n")
        if opcion==1:
            Ingresar(carreras,"carrera")
        elif opcion==2:
            Mostrar(carreras)
        elif opcion==3:
            Actualizar("carrera",carreras)
        elif opcion==4:
            Borrar(carreras,"carrera")
        elif opcion==5:
          print("Nos vemos")
          seguir= False
        print("------------------\n")
    else:
        print(" Ingrese un numero valido por favor")

    


    


