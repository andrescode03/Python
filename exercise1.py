print("----" * 10)

usuarios = {
    "user1": "123",
    "user2": "456",
    "user3": "968"
}


def validar_usuario():
    while True:
        print("----" * 10)
        value_user = input("Ingrese su nombre de usuario: ")
        value_password = input("Ingrese su contraseña: ")
        if value_user in usuarios and usuarios[value_user] == value_password:
            print("Usuario válido. Bienvenido.")
            return True
        else:
            print("Usuario inválido. Intente de nuevo.")


# Primero validamos el usuario
if validar_usuario():
    cajero = {
        "saldo": 3000,
    }

    while True:
        print("----" * 10)
        print("Elige una opción dentro del cajero")
        print("----" * 10)
        print("Elige 1 para revisar tu saldo")
        print("Elige 2 para hacer un retiro")
        print("Elige 3 para consignar")
        print("Elige 4 para salir")
        print("----" * 10)

        option = input("Ingrese la opción que desea realizar: ")

        if option == "1":
            print(f"Tu saldo es: {cajero['saldo']}")

        elif option == "2":
            retiro = int(input("¿Cuánto quiere retirar?: "))
            if retiro <= cajero["saldo"]:
                cajero["saldo"] -= retiro
                print(f"Retiraste: {retiro}")
            else:
                print("Fondos insuficientes")

        elif option == "3":
            consignacion = int(input("Ingrese cuánto desea consignar: "))
            cajero["saldo"] += consignacion
            print(f"Consignaste: {consignacion}")
            print(f"Tu saldo actual es: {cajero['saldo']}")

        elif option == "4":
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break

        else:
            print("Opción incorrecta")
