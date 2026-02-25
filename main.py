def cajero_automatico():
    saldo = 1000
    print("bienvenido al cajero automatico")

    
    operaciones = int(input("cuantas operaciones desea realizar? "))
    for i in range(operaciones):
        print("1. consultar saldo")
        print("2. retirar dinero")
        print("3. depositar dinero")
        opcion = int(input("seleccione una opcion: "))

        if opcion == 1:
            print(f"su saldo actual es: {saldo}")
        elif opcion == 2:
            monto_retirar = int(input("ingrese el monto a retirar: "))
            if monto_retirar > saldo:
                print("fondos insuficientes")
            else:
                saldo -= monto_retirar
                print(f"ha retirado: {monto_retirar}. su nuevo saldo es: {saldo}")
        elif opcion == 3:
            monto_depositar = int(input("ingrese el monto a depositar: "))
            saldo += monto_depositar
            print(f"ha depositado: {monto_depositar}. su nuevo saldo es: {saldo}")
        else:
            print("opcion no valida")
cajero_automatico()