#Hago una matriz tridimensional con el día, la hora y el cuarto de la misma hora
MAX_D1 = 30
MAX_D2 = 24
MAX_D3 = 4

#Hago 3 bucles for in para hacer una lista vacía de pega, van a estar todos los valores en "0"
matriz=[[[0 for n in range(MAX_D3)]for s in range(MAX_D2)] for i in range(MAX_D1)]

#Función usada varias veces en el programa,
#pide un valor entero, permitiendo negativos para la temperatura
def pedirValor(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except:
            print("Opción incorrecta, debe ser un número")

#Como se verá a continuación todas las opciones son muy similares
def opciones(opcion):
    match opcion:
        #En la opción 1 hacemos 3 bucles, uno por dimesión
        #Haciendo que toda la matriz tenga el mismo valor
        case "1":
            valor= pedirValor("Introduce el valor de la temperatura:")
            for d in range(MAX_D1):
                for h in range(MAX_D2):
                    for m in range(MAX_D3):
                        matriz[d][h][m] = valor
            print("Se asignaron todos los valores en la matriz")
            print(matriz)
        #En la opción 2 especificamos el día
        #Entonces todas las temperaturas del día serán iguales
        case "2":
            while True:
                valor = pedirValor("Introduce el día:")
                if valor>MAX_D1 or valor<=0:
                    print("Está fuera del rango, vuelve a probar")
                else:
                    valor = valor -1
                    m = pedirValor("Introduce la temperatura:")
                    for d in range(MAX_D2):
                        for h in range(MAX_D3):
                            matriz[valor][d][h] = m
                    break
        # En la opción 3 especificamos el día y hora
        # Entonces todas las temperaturas de la hora del día serán iguales
        case "3":
            while True:
                valor = pedirValor("Introduce el día:")
                if valor>MAX_D1 or valor<=0:
                    print("Está fuera del rango, vuelve a probar")
                else:
                    valor2 = pedirValor("Introduce la hora:")
                    if valor2 >= MAX_D2:
                        print("Está fuera del rango, vuelve a probar")
                    else:
                        valor = valor -1
                        m = pedirValor("Introduce la temperatura:")
                        for d in range(MAX_D2):
                            for h in range(MAX_D3):
                                matriz[valor][valor2][h] = m
                        break
        # En la opción 4 especificamos el día y hora y el período
        # Así se asigna un único valor en la hora de un día de nuestra elección
        case "4":
            while True:
                valor = pedirValor("Introduce el día:")
                if valor>MAX_D1 or valor<=0:
                    print("Está fuera del rango, vuelve a probar")
                else:
                    valor2 = pedirValor("Introduce la hora:")
                    if valor2 >= MAX_D2:
                        print("Está fuera del rango, vuelve a probar")
                    else:
                        valor3= pedirValor("Introduce el cuarto de hora:")
                        if valor3>0:
                            valor3= valor3-1
                        if valor3>=MAX_D3:
                            print("Está fuera del rango, vuelve a probar")
                        else:
                            valor = valor -1
                            m = pedirValor("Introduce la temperatura:")
                            for d in range(MAX_D2):
                                for h in range(MAX_D3):
                                    matriz[valor][valor2][valor3] = m
                            break
        #En la opción 5, mostramos todas las temperaturas de un día
        #Para eso recorremos toda la matriz recogiendo y mostrando sus valores
        case "5":
            count= 0
            while True:
                valor = pedirValor("Introduce el día:")
                if valor>MAX_D1 or valor<=0:
                    print("Está fuera del rango, vuelve a probar")
                else:
                    valor = valor -1
                    print("-------------------- TEMPERATURAS --------------------")
                    for h in range(MAX_D2):
                        for c in range(MAX_D3):
                            print(f"{h:02}:{c*15:02} => {matriz[valor][h][c]}ºC", end="   ")
                            count += 1
                            if count % 4 == 0:
                                print("\n")
                                count = 0
                    print("------------------------------------------------------")
                    break
        #Esto es lo que pasa cuando se selecciona una opción incorrecta
        #Se reinicia el programa de opciones
        case _:
            print("La opción no existe, prueba de nuevo")
            menu()

#Menú para mostrar las opciones
def menu():
    while True:
        print("------ MENÚ ------")
        print("1. Insertar temperatura fija en toda la matriz")
        print("2. Insertar temperatura fija en día concreto")
        print("3. Insertar temperatura fija en hora de día concreto")
        print("4. Modificar temperatura de un periodo concreto")
        print("5. Mostrar tabla de temperatura del día concreto")
        print("6. Pulsa intro para salir")
        print("------------------")
        opcion = input("Ingresa la opcion del menu: ")
        if opcion == "":
           print("Saliendo...")
           print("Hasta luego!(No se guardan los datos)")
           break
        else:
            opciones(opcion)
menu()