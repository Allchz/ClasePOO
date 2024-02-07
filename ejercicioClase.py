carreras = []
seguir = True

while seguir:
    print(carreras)
    print("++++++++++++++++ Menu ++++++++++++++++++")
    print("1. Crear carrera")
    print("2. Leer carrera")
    print("3. Actualizar carrera")
    print("4. Borrar carrera")
    print("5. Salir")
    print("6. Buscar Carrera")
    opcion = input("Ingrese su opcion: ")

    if opcion.isdigit():
      opcion= int(opcion)

      print("----------------------------------\n")
      if opcion == 1:
        print("Ingresar carrera")
        nombre = input("Nombre : ")
        dicCarrera = {}
        dicCarrera["carrera"] = nombre
        carreras.append(dicCarrera)
      elif opcion == 2:
        print("Leer (mostrar) carreras")
        for carrera in carreras:
            print("- Nombre :" + carrera["carrera"])
      elif opcion == 3:
        carreraActualizar = input("Ingrese nombre de la carrera : ")
        nuevoValor = input("Ingrese nuevo nombre de la carrera : ")

        indice = 0
        for carrera in carreras:
            if carrera["carrera"] == carreraActualizar:
                carrera["carrera"] = nuevoValor

      elif opcion == 4:
        carreraBorrar = input("Ingrese nombre de la carrera : ")
        indice = 0
        encontrado = False
        for carrera in carreras:
            if carrera["carrera"] == carreraBorrar:
                encontrado = True
                break
            else :
                indice = indice + 1

        if encontrado :
            carreras.remove(carreras[indice])
            print("Elemento borrado")
        else:
            print("No existe")
      elif opcion == 5:
        print("Hasta la proxima")
        seguir = False
      elif opcion == 6:
        carreraBuscar= input("Ingrese la Carrera que desea buscar ")

        indice=0
        encontrado = False
        for carrera in carreras:
            if carrera["carrera"] == carreraBuscar:
                encontrado = True
                break
            else:
                indice = indice + 1
        if encontrado:
            print(carreras[indice])

            while True:
                print("\n♦♦♦♦♦♦♦♦♦♦♦Menú♦♦♦♦♦♦♦♦♦♦♦\n")
                print("1. Agregar Clase")
                print("2. Mostrar Clases")
                print("3.Eliminar Clase")
                print("4. Actualizar Clases")
                print("5.Buscar Clase")
                print("6. Salir")
                opcion2=input("Ingrese una Opcion: ")

                if opcion2.isdigit():
                    opcion2=int(opcion2)

                    if opcion2==1:
                        clasenueva=input("Escriba la clase que desea: ")
                        dicClase={}
                        dicClase["Clase"] = clasenueva
                        carreras[indice].update(dicClase)
                        print(carreras)
                    if opcion2==2:
                        print("--------Clase---------")
                        print(carreras[indice]["Clase"])



                else:
                    print("Digite un numero, por favor ")






        else:
            print("No existe")
      print("----------------------------------")
    else:
     print(" Ingrese un numero, Por favor")