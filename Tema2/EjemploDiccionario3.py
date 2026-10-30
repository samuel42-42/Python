
sistema = {}
Perfil = ("Sin acceso","Acceso básico","Acceso estándar","Acceso Premium","Administrador")
def opcion2():
    user = input("Nick?: ")
    nick = input(f"¡Hola {user}! Introduce el login de usuario: ")
    if len(sistema)!=0:
        while True:
            if nick in sistema:
                nick = input(f"> {user}, ese login ya existe, prueba de nuevo: ")
            else:
                break

    password = input(f"> {nick}, Introduce la contraseña: ")
    while True:
        try:
            print(f"Las opciones de permisos que puedes implementar son estos:"
            f"\n{Perfil[0]}: 0\n{Perfil[1]}: 1\n{Perfil[2]}: 2\n{Perfil[3]}: 3\n{Perfil[4]}: 4")
            user_perf = Perfil[int(input("Introduce los permisos que tendrá el usuario: "))]
            break
        except:
            print("Esa opción no está")

    user_dic = {"nick": user, "Login": nick, "Password": password, "Perfil": user_perf}
    sistema[nick]=user_dic

def opcion(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except:
            print("Opción incorrecta, debe ser un número")

def menu():
    while True:
        print("---------- MENÚ ----------")
        print("1. Mostrar contenido del diccionario global")
        print("2. Introducir un usuario nuevo")
        print("3. Eliminar un usario")
        print("4. Estadísticas de los perfiles")
        opt = input("Introduce la opción:")
        match opt:
            case "1":
                print("Usuarios:")
                for i, j in sistema.items(): print("Usuario:"sistema.get(i).get("Login",j)+""+sistema.get(i).get("nick",j))
                for i, j in sistema.items(): print(sistema.get(i).get("Nick", j))
                for i, j in sistema.items(): print(sistema.get(i).get("Login", j))
                for i, j in sistema.items(): print(sistema.get(i).get("Login", j))
                for i, j in sistema.items(): print(sistema.get(i).get("Login", j))
            case "2":
                opcion2()
            case "3":
                print("cosas")
            case "4":
                print("cosas")
            case _:
                print("La opción no existe, prueba de nuevo")
menu()