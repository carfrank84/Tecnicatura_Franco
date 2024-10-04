# Ejercicio 8:menú interactivo cajero automático
# hacer un programa que simule un cajero automático con un saldo inicial de $ 1000
# y tendrá el siguiente menú de opciones:
# 1- ingresa dinero en la cuenta
# 2- retirar dinero de la cuenta
# 3- mostrar dinero disponible
# 4- salir

saldo = 1000
while True:
    print("\t.:MENU:.")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opcion de menu:"))
    print()
    if opcion == 1:
        extra = float(input(" Cuanto dinero desea ingresar --> "))
        saldo += extra
        print(f"Dinero en la cuenta al momento:  ${saldo}")
    elif opcion == 2:
        retirar = float(input(" Cuanto dinero desea retirar  -->"))
        if retirar > saldo:
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 3:
        print(f"Dinero en la cuenta al momento: $ {saldo}")
    elif opcion == 4:
        print(f"Gracias por utilizar el cajero automatico, vuelva pronto")
        break
    else:
        print("Error, se equivoco de opcion de menu")
        print()

