
try:
    repetir = True
    while repetir:
        dia = int(input("Dia >"))
        mes= int(input("Mes >"))
        ano = int(input("Año >"))
        print("Fecha:",end=" ")
        day= str(dia)
        m= str(mes)
        a= str(ano)
        if dia<10:
            day="0"+day
        if mes<10:
            m="0"+m
        if ano<10:
            a= "000"+a
        elif ano<100:
            a = "00" + a
        elif ano<1000:
            a = "0" + a
        print(day,m,a,sep="/")
        respuesta = input("¿Quieres repetirlo?[y/n]: ")
        while respuesta!= "n" and respuesta!= "y":
            respuesta = input("Eso no es una opcion valida, ponla de nuevo: ")
        if respuesta == "y":
            repetir = True
        elif respuesta == "n":
            repetir = False

except:
    print("Ha habido un error")