def cedula_ciudadania():

    while True:
        bienvenida = input("Bienvenido al sistema de validacion de cedula, desea ingresar su numero de cedula? (si/no): ")

        if bienvenida.lower() == "si":
            cedula = input("Ingrese su numero de cedula: ")
            if len(cedula) != 10:
                print("numero de cedula no valido")
                break
    #            return cedula_ciudadania()  # Vuelve a pedir la cédula si no es válida
            elif cedula.isdigit():
                print("numero de cedula valido\n")
            else:
                print("numero de cedula no valido, debe contener solo numeros")
                break
        elif bienvenida.lower() == "no":
            print("gracias por usar el sistema de validacion de cedula")
            break
        else:
            print("opcion no valida, por favor ingrese 'si' o 'no'")
        
        for i in range(1, 2):  contraseña = input("Ingrese su contraseña: ")
        if contraseña == "1234":
            print("contraseña correcta")
        else:        
            print("contraseña incorrecta")
        saldo = 1000
        print("bienvenido al cajero automatico")

        operaciones = int(input("cuantas operaciones deseas realizar hoy:\n"))
        while operaciones > 0:

                print("1. consultar el saldo")

                print("2. retirar dinero")

                print("3. depositar dinero")

                print("4. sal si no te gusta")

                opcion = int(input("seleccione una opcion:\n"))
                print("\n")
                if opcion == 1:
                    print(f"su saldo actual es: {saldo}")

                elif opcion == 2:
                    print(f"La cantidad de dinero que tiene en su cuenta es: {saldo}")
                    monto_retirar = int(input("ingrese el monto a retirar:\n"))
                    if monto_retirar > saldo:
                        print("fondos insuficientes")

                    else:
                        saldo -= monto_retirar
                        print(f"ha retirado: {monto_retirar}. su nuevo saldo es: {saldo}")
                elif opcion == 3:
                        monto_depositar = int(input("ingrese el monto a depositar:"))
                        saldo += monto_depositar
                        print(f"ha depositado: {monto_depositar}. su nuevo saldo es: {saldo}")
                else:
                    print("opcion no valida")
                    operaciones += 1
                operaciones -= 1
                break
        print("gracias por usar el cajero automatico")
cedula_ciudadania()
