# Ejercicio 5: convertidor de temperaturas
# realizar dos funciones para convertir de grados celcius
# a fahrenheit y viceversa.
# investigar las formulas

# Funcion convierte de celcuis a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 #La presedencia: multiplicacion, division y suma
# funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # Respetar la presedencia utilizando parentesis
celsius = float(input('Digite el valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C - > {resultado:.2f}')







