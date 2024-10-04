# Solicitar al usuario la cantidad de números a ingresar
N = int(input("Ingrese la cantidad de números: "))

# Inicializar contadores y acumuladores
cantidad_pares = 0
suma_impares = 0
cantidad_impares = 0

# Inicializar contador para el bucle
contador = 0

# Leer N números usando un bucle while
while contador < N:
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        cantidad_pares += 1
    else:
        suma_impares += num
        cantidad_impares += 1
    contador += 1  # Incrementar el contador

# Calcular el promedio de los números impares
if cantidad_impares > 0:
    promedio_impares = suma_impares / cantidad_impares
else:
    promedio_impares = 0

# Mostrar resultados
print("Cantidad de números pares:", cantidad_pares)
print("Promedio de números impares:", promedio_impares)
