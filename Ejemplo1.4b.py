lista = [1,2,3,4,5,6]
print(lista)
numero= "5"*2
try:
    while True:
        size = len(lista)
        assert size>=2
        print("Elemento a borrar:", lista[size-1])
        lista.pop()
        print(lista)
except:
    print("ZEHAHAHAHA!!!")