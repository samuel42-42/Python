sistema = {}
Perfil = ("Sin acceso","Acceso básico","Acceso estándar","Acceso Premium","Administrador")
user = input("Nick?: ")
while True:
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

        user_dic = {"Login": nick, "Password": password, "Perfil": user_perf}
        sistema[nick]=user_dic
        salir = input("Quieres salir?(Se borran los datos) [y/n]")

        if salir == "y":
            break