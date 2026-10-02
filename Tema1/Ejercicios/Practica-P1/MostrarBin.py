finalizar = False
while not finalizar:
    try:
        valor=int(input("Introduce el valor del número, el máximo posible son 16 bits:"))
        while valor >65355:
            valor=int(input("El valor es demasiado alto, introdúcelo de nuevo: "))
        print(f"{valor:b}")
        finalizar = True
    except ValueError:
        print("Eso no es un número, toma, empecemos de nuevo")