try:
    name = input("Nombre > ")
    edad = int(input("Edad de " + name + "> "))
    peso = float(input("Peso de " + name + "> "))

    print(name,"tiene",edad,"años y pesa",peso,"kg")
except:
    print("Parece que tienes algún errorcillo, pringui")