from inspect import trace
from logging import error
def menu():
    while True:
        op = input("Introduce la opción: ")
        if op == "":
            print("Saliendo...")
            exit()
        else:
            opcion = int(op)
        try:
            if opcion>=3:
                opcion = int(input("La opción es invalida, prueba de nuevo :"))
            elif opcion<0:
                opcion = int(input("La opción es invalida, prueba de nuevo :"))
            elif opcion is None:
                exit()
            else:
                return opcion
        except:
            opcion = int(input("La opcion es invalida, prueba de nuevo"))

def op1():
    opcion = int(input("Introduce la opción: "))
    while True:
        try:
            if opcion >= 2:
                opcion = int(input("La opción es invalida, prueba de nuevo: "))
            elif opcion < 0:
                opcion = int(input("La opción es invalida, prueba de nuevo: "))
            else:
                return opcion
        except:
            opcion = int(input("La opcion es invalida, prueba de nuevo: "))

def op2():
    opcion = int(input("Introduce la opción: "))
    while True:
        try:
            if opcion >= 3:
                opcion = int(input("La opción es invalida, prueba de nuevo: "))
            elif opcion < 0:
                opcion = int(input("La opción es invalida, prueba de nuevo: "))
            else:
                return opcion
        except:
            opcion = int(input("La opcion es invalida, prueba de nuevo: "))

listaQ = []
while True:
    print("---------- MENÚ ----------")
    print("Opción 0: Añadir elemento químico")
    print("Opción 1: Borrar elemento químico")
    print("Opción 2: Mostrar lista")
    print("--------------------------")
    match menu():
        case 0:
            print("Opción 0: Añadirla por el final")
            print("Opción 1: Añadir en una posición determinada")
            match op1():
                case 0:
                    listaQ.append(input("Introduce el nombre del elemento a añadir: "))
                case 1:
                    listaQ.insert(int(input("Introduce la posición del elemento: ")),input("Introduce el nombre del elemento a añadir: "))
        case 1:
            if len(listaQ) == 0:
                print("No hay elementos en la tabla")
            else:
                print("Opción 0: Eliminar el último valor")
                print("Opción 1: Eliminar en una posición determinada")
                print("Opción 2: Eliminar por nombre")
                match op1():
                    case 0:
                        listaQ.pop()
                    case 1:


                        while True:
                            try:
                                del listaQ[int(input("Introduce la posición del elemento: "))]
                                break
                            except:
                                print("Esa posición no existe")
        case 2:
            print(listaQ)