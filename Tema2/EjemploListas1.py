from inspect import trace
from logging import error
def menu():
    opcion= int(input("Introduce la opción: "))
    while True:
        try:
            if opcion>=3:
                opcion = int(input("La opción es invalida, prueba de nuevo :"))
            elif opcion<0:
                opcion = int(input("La opción es invalida, prueba de nuevo :"))
            else:
                return opcion
        except:
            opcion = int(input("La opcion es invalida, prueba de nuevo"))

def op1():
    opcion = int(input("Introduce la opción: "))
    while True:
        try:
            if opcion >= 2:
                opcion = int(input("La opción es invalida, prueba de nuevo :"))
            elif opcion < 0:
                opcion = int(input("La opción es invalida, prueba de nuevo :"))
            else:
                return opcion
        except:
            opcion = int(input("La opcion es invalida, prueba de nuevo"))

listaQ = ["Hierro", "Magnesio"]
repetir = True
while repetir:
    print("---------- MENÚ ----------")
    print("Opción 0: Añadir elemento químico")
    print("Opción 1: Borrar elemento químico")
    print("Opción 2: Mostrar lista")

    match menu():
        case 0:
            print("Opción 0: Añadirla por el final")
            print("Opción 1: Añadir en una posición determinada")
            match op1():
                case 0:
                    listaQ.append(input("Introduce el nombre del elemento a añadir: "))
                case 1:
                    listaQ.insert(int(input("Introduce la posición del elemento")),input("Introduce el nombre del elemento a añadir"))

        case 1:
            try:
                listaQ.pop()
                print(listaQ)
                print()
            except IndexError:
                print("No hay elementos en la tabla")
        case 2:
            print(listaQ)
