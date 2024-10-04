while True:
    # Solicitar al usuario que ingrese un número entero positivo
    n = int(input("Ingrese un número entero positivo: "))

    # Inicializar la suma
    suma = 0

    # Calcular la suma de los primeros n números
    for i in range(1, n + 1):
        suma += i

    # Mostrar el resultado
    print(f"La suma de los primeros {n} números es: {suma}")

    # Preguntar al usuario si desea calcular la suma de otro número
    repetir = input("¿Desea calcular la suma de otro número? (s/n): ").strip().lower()

    # Salir del ciclo si el usuario no desea continuar
    if repetir != 's':
        print("Gracias por usar el programa.")
        break