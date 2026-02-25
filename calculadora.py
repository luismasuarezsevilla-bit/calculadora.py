def calculadora():
    while True:
        print("bienvenido a la calculadora")
        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. division")
        print("5. raiz cuadrada")
        print("6. potencia")
        print("7. porcentaje")
        print("8. modulo %")
        print("9.promedio")
        print("10. desea continuar? (si/no)")

        opcion = int(input("seleccione una opcion:"))
        if opcion == 1:
            num1 = int(input("ingrese el primer numero:"))
            num2 = int(input("ingrese el segundo numero:"))
            resultado = num1 + num2
            print(f"el resultado de la suma es: {resultado}")
        elif opcion == 2:
            num1 = int(input("ingrese el primer numero:"))
            num2 = int(input("ingrese el segundo numero:"))
            resultado = num1 - num2
            print(f"el resultado de la resta es: {resultado}")
        elif opcion == 3:
            num1 = int(input("ingrese el primer numero:"))
            num2 = int(input("ingrese el segundo numero:"))
            resultado = num1 * num2
            print(f"el resultado de la multiplicacion es: {resultado}")
        elif opcion == 4:
            num1 = float(input("ingrese el primer numero:"))
            num2 = float(input("ingrese el segundo numero:"))
            if num2 == 0:
                print("no se puede dividir por cero")
            else:
                resultado = num1 / num2
                print(f"el resultado de la division es: {resultado}")
        elif opcion == 5:
            num = float(input("ingrese el numero:"))
            if num < 0:
                    print("no se puede calcular la raiz cuadrada de un numero negativo")
            else:
                resultado = num ** 0.5
                print(f"el resultado de la raiz cuadrada es: {resultado}")
        elif opcion == 6:
            num1 = float(input("ingrese el primer numero:"))
            num2 = float(input("ingrese el segundo numero:"))
            resultado = num1 ** num2
            print(f"el resultado de la potencia es: {resultado}")
        elif opcion == 7:
            num1 = float(input("ingrse el numero:"))
            num2 = float(input("ingrese el porcentaje a calcular:"))
            resultado = (num1 * num2) / 100
            print(f"el resultado del porcentaje es: {resultado}")
        elif opcion == 8:
            num1 = float(input("ingrese el primer numero:"))
            num2 = float(input("ingrese el segundo numero:"))
            resultado = num1 % num2
            print(f"el resultado del modulo es: {resultado}")
        elif opcion == 9:
            num1 = float(input("ingrese el primer numero:"))
            num2 = float(input("ingrese el segundo numero:"))
            resultado = (num1 + num2) / 2
            print(f"el resultado del promedio es: {resultado}")
        elif opcion == 10:
            continuar = input("desea continuar? (si/no):")
            if continuar.lower() == "no":
                print("gracias por usar la calculadora buen dia / noche / tarde")
                break
            else:                continue
        else:           print("opcion no valida")
        calculadora()
calculadora()