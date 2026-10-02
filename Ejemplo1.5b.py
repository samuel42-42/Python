try:
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
        a= "0"+a
    print(day,m,a,sep="/")
except:
    print("PRINGUI PRINGUI PRINGUI JAJAJAJAJA")