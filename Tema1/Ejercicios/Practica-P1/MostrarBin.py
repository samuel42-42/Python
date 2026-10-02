finalizar = False
while not finalizar:
    try:
        valor=int(input("Introduce el valor del número, el máximo posible son 16 bits:"))
        while valor >65535:
            valor=int(input("El valor es demasiado alto, introdúcelo de nuevo: "))
        print("Valor binario: "+f"{valor:b}")
        print("Valor hexadecimal:"+f"{valor:X}")
        print("Carácter ascii del número:"+f"{valor:c}")
        print("Chao!")
        finalizar = True
    except ValueError:
        print("Eso no es un número, toma, empecemos de nuevo")