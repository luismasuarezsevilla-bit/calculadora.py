def cajero_automatico():
    saldo = 1000
    print("bienvenido al cajero automatico")

    operaciones = int(input("cuantas operaciones deseas realizar hoy"))
    while operaciones > 0:

        print("1. consultar el saldo")

        print("2. retirar dinero")

        print("3. depositar dinero")

        print("4. sal si no te gusta")

        opcion = int(input("seleccione una opcion:"))
        if opcion == 1:
            print(f"su saldo actual es: {saldo}")

        elif opcion == 2:
            monto_retirar = int(input("ingrese el monto a retirar:"))
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
cajero_automatico()
