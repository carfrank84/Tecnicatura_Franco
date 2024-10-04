while True:
    anio = int(input("Ingrese un año: "))

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"El año {anio} es bisiesto.")
    else:
        print(f"El año {anio} no es bisiesto.")

    repetir = input("¿Desea verificar otro año? (s/n): ").strip().lower()
    if repetir != 's':
        print("Gracias por usar el programa.")


