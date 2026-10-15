nombre = "Ana"
edad = 25
mensaje = "Hola, me llamo {} y tengo {}"
print("Salida 1:",mensaje)
print("Salida 2:", mensaje.format(nombre,edad))
mensaje="Hola, me llamo {i1} y tengo {i2}"
print("Salida 3:",mensaje.format(i1=nombre,i2=edad))
mensaje= "Hola, me llamo %s y tengo %d,"%(nombre,edad)
print("Salida 4:",mensaje)