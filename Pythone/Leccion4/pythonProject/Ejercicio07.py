# Ejercicio 7 juego adivina el número realizar un juego para adivinar un número.
# Para ello se debe generar un número aleatorio entre uno y un 100
# y luego ir pidiendo números indicando es mayor o es menor según sea mayor o menor con respecto a n .
# el proceso termina cuando el usuario es cierta y allí se debe mostrar el número de intentos.

import random
print("\t!!! Juego Adivina el Numero ¡¡¡")
aleatorio = random.randint(0,100) # toma de 0 a 100 literal, generamos un numero aleatorio
contador = 0
while True:
    numero = int(input(" Digite un numero: "))
    contador += 1
    if numero >  aleatorio:
        print("\tNo es el numero, digite un numero menor:")
    elif numero < aleatorio:
        print("\tNo es el numero, digite un numero mayor")
    else:
        print(f"Felicidades, acaba de adivinar el numero {aleatorio}")
        break # rompe el ciclo y el bucle

print(f"\n!!! Numeros de intentos: {contador} ¡¡¡")




