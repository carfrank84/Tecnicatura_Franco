#Sistema de clasificaciones

valor = float(input("Ingresa un valor del 1 al 10: "))

if 9 <= valor <= 10:
    calificacion = "A"
elif 8 <= valor < 9:
    calificacion = "B"
elif 7 <= valor < 8:
    calificacion = "C"
elif 6 <= valor < 7:
    calificacion = "D"
elif 0 <= valor < 6:
    calificacion = "F"
else:
    calificacion = "El valor ingresado es incorrecto"

print(f"La calificación correspondiente al valor ingresado es: {calificacion}")