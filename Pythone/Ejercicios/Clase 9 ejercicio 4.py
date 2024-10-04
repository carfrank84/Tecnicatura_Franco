suma_calificaciones = 0
calificacion_minima = float('inf')

# Leer las calificaciones de 10 alumnos
for i in range(10):
    calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))

    # Sumar la calificación actual a la suma total
    suma_calificaciones += calificacion

    # Actualizar la calificación mínima
    if calificacion < calificacion_minima:
        calificacion_minima = calificacion

# Calcular el promedio
promedio = suma_calificaciones / 10

# Imprimir resultados
print(f"Calificación promedio: {promedio}")
print(f"Calificación más baja: {calificacion_minima}")