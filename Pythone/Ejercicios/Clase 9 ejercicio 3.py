positivos = 0
negativos = 0
neutros = 0

# Leer 10 números
for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))

    # Clasificar el número
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

# Imprimir resultados
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números neutros (cero): {neutros}")