alumno1 = {"Nombre": "Juan", "Edad":28, "Curso": "DAM2"}
alumno2 = {}
alumno2["Nombre"] = "Ana"
alumno2["Edad"] = 25

alumno3 = dict(Nombre = "Sara", Edad= 35, Curso = "DAM1")
print(alumno1)
print(alumno2)
print(alumno3)
clase = {'12345678Z': alumno1, '87654321Z': alumno2, '11111111K': alumno3}
acabar = True
while acabar:
    try:
        dni = input("Introduce el dni:")
        print(f"El nombre del alumno es: {clase.get(dni).get("Nombre",dni)}")
        acabar = False
    except:
        print("no no no, eso no es")