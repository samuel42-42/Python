
# Listas para almacenar la información
nombres = []
moviles = []
correos = []

# Bucle para recoger datos
continuar = "s"
while continuar == "s":
    nombre = input("Introduce el nombre: ")
    movil = input("Introduce el móvil: ")
    correo = input("Introduce el correo electrónico: ")

    # Se usa .append()
    nombres.append(nombre)
    moviles.append(movil)
    correos.append(correo)

    continuar = input("¿Quieres introducir más contactos? (s/n): ")

# Formato de la agenda tabulada
print("\n" + "=" * 75)
print(f"{'Nombre':<20} | {'Móvil':<9} | {'Correo electrónico':<40}")
print(f"{'_' * 20} | {'_' * 9} | {'_' * 40}")

# Mostrar los contactos guardados
for i in range(len(nombres)):
    print(f"{nombres[i]:<20} | {moviles[i]:<9} | {correos[i]:<40}")
