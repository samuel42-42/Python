from inspect import trace
from logging import error
#Iniciamos el método del menú capturando excepciones para la selección de opciones
def menu():
    while True:
        try:
            opcion = input("Introduce la opción: ")
            if opcion == "":
                print("Saliendo...")
                exit()
            else:
                opcion = int(opcion)
            if opcion>=6:
                opcion = int(input("La opción es invalida, prueba de nuevo: "))
            elif opcion<0:
                opcion = int(input("La opción es invalida, prueba de nuevo: "))
            else:
                return opcion
        except:
            print("La opción es invalida, prueba de nuevo: ")
listaQ = []
#Esto es la imagen del menú, inicia un bucle para el match de más abajo
while True:
    print("---------- MENÚ ----------")
    print("Opción 0: Añadir elemento químico por el final")
    print("Opción 1: Añadir elemento químico en una posición concreta")
    print("Opción 2: Borrar elemento químico")
    print("Opción 3: Eliminar elemento químico por la posición")
    print("Opción 4: Eliminar elemento químico por el nombre")
    print("Opción 5: Mostrar lista")
    print("Presiona enter para salir...")
    print("--------------------------")
    match menu():
        #Permite añadir un elemento al final de la lista
        case 0:
            listaQ.append(input("Introduce el nombre del elemento a añadir: ").upper())
        #Permite añadir un elemento a la lista en la posición deseada (si existen ese número de elementos)
        case 1:
            listaQ.insert(int(input("Introduce la posición del elemento: "))-1,input("Introduce el nombre del elemento a añadir: ").upper())
        #Permite borrar el último elemento(comprobando si existe alguno, esto se usa para todos los métodos de borrar)
        case 2:
            if len(listaQ) == 0:
                print("No hay elementos en la tabla")
            else:
                listaQ.pop()
                print("Opción 1: Eliminar en una posición determinada")
                print("Opción 2: Eliminar por nombre")
        # Permite borrar un elemento químico por su posición(si no existe lanzará un except hasta que borre uno que sí)
        case 3:
            if len(listaQ) == 0:
                print("No hay elementos en la tabla")
            else:
                while True:
                    try:
                        del listaQ[int(input("Introduce la posición del elemento: "))-1]
                        break
                    except:
                        print("Esa posición no existe")
        # Permite borrar un elemento por su nombre(si no existe te pedirá el nombre hasta que borre uno que existe)
        case 4:
            if len(listaQ) == 0:
                print("No hay elementos en la tabla")
            else:
                while True:
                    try:
                        listaQ.remove(input("Introduce el nombre del elemento:").upper())
                        break
                    except:
                        print("Ese elemento no existe")
        # Enseña la lista entera
        case 5:
            print(listaQ)