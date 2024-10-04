'''
# miVariable = 3
# print(miVariable)
# miVariable = "hola a todos los alumnos de la tecnicatura"
# print(miVariable)
# miVariable = 3.5
# print(miVariable)
# x = 10
# y = 2
# z = x + y
# print(z)
# print(id(x))
# # las literales se escriben X584
# print(id(y))
# print(id(z))
# # la literal Y328
# # la literal Z648
#
# # Tipos int, float, string, bool
# a = 10
# print(a)
# print(type(a))
# b = 10.5
# print(b)
# print(type(b))
# c = " hola a todos"
# print(c)
# print(type(c))
# d = True
# print(d)
# print(type(d))
# e = False
# print(e)
# print(type(e))
#
# # Manejo de Caracteres
# miGrupoFavorito="Derribando Fronteras:"
# caracteristicas= " La Mejor Banda de Folklore"
# print("Mi Grupo Favorito es :", miGrupoFavorito, caracteristicas)
#
# numero1 = "7"
# numero2 = "8"
# print(int(numero1) + int(numero2))
#
# # Tipos Booleanos (Bool)
# miBooleano = 3 > 2
# print(miBooleano)
#
# if miBooleano:
#     print(" El Resultado es Verdadero")
# else:
#     print("El Resultado es Falso")

# Procesar la entrada del usuario
# funcion input
#resultado=input(" Digite un numero:")  # la funcion input regresa un dato tipo string
#print(resultado)

# conversion de la entrada de datos

 # numero1 = int(input("Escribe el primer numero: "))
# numero2 = int(input("Escribe el segundo numero: "))
# resultado= numero1 + numero2
# print(" El resultado de la suma es:", resultado)
# -----------------------------------------------------------------
# Ejercicio N° 1 Califica tu dia
# Como estuvo tu dia del 1 al 10?

# print(" Como estuvo tu dia del 1 al 10:")
# tuDia=int(input("Digita un numero :"))
# print("Mi dia estuvo : ", tuDia , "puntos")
# --------------------------------------------------------------
# Ejercicio 2:
# Se solicita incluir la siguiente información acerca de un libro:
# título
# autor
# Debes imprimir la información en el siguiente formato:
# Proporciona el título:
# Proporciona el autor:
# <título> fue escrito por <autor>
# titulo=input(" Escribe el Titulo de tu Libro Favorito:")
# autor=input(" Escribe el Autor:")
# print(" El libro", titulo, "fue ecrito por ", autor )
# -----------------------------------------------------------
'''

# operadores en Pythone
'''
operandoA= 8
operandoB= 5
suma = operandoA + operandoB
# print(" Resultado de la suma:", suma)
print(f'El resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f'el resultado de la resta es:{resta}')

multiplicacion= operandoA * operandoB
print(f' El resultado de la Multiplicacion:{multiplicacion}')

division= operandoA / operandoB
print(f'El resultado de la Division es : {division}')
division= operandoA // operandoB
print(f"El Resultado de la division (int) es : {division}")

modulo = operandoA % operandoB
print(f" El resultado de la Division o residuo (modulo) es: {modulo}")

exponente= operandoA ** operandoB
print(f"El resultado del exponente es:{exponente}")
'''
# Ejercicio Rectangulo
'''
alto=int(input("Proporciona el alto del rectangulo:"))
ancho=int(input("Proporciona el ancho del rectangulo"))
area=  alto * ancho
perimetro= (alto + ancho)*2
print(f"El Area es : {area}")
print(f"El Perimetro es : {perimetro}")
'''
'''
miVariable3=10
print(miVariable3)
# operadores de reasignacion

miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 -2
miVariable3 -=2
print(miVariable3)
# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)
# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# operadores de comparacion

d = 4
b = 2
resultado = d == b # comprobamos si son iguales
print(resultado)

# operador diferente
resultado = d != b
print(resultado)

# operador mayor que
resultado = d > b
print(resultado)

#  operador menor que
resultado = d < b
print(resultado)

#  operador menor o igual que
resultado = d <= b
print(resultado)

#  operador mayor o igual que
resultado = d >= b
print(resultado)
'''
'''
# Ejercicio numero par o impar

print(" ***Para Saber si es par o impar***")
num = int(input(" Digite un numero:"))
print(f" El residuo de la division es: {num%2}")
if num % 2 == 0:
    print("Es un numero par")
else:
    print(" Es un numero Impar")
'''

# Ejercicio Mayor de edad
'''
num = int(input(" Digite su edad:"))
if num >= 18 :
    print(f"con {num} años Eres Mayor de edad")
else: print(f"con {num} años Eres Menor de edad")
'''
'''
# operador and
a = False
b = False
resultado = a and b
print(resultado)

# operador or
resultado = a or b
print(resultado)
# operador not
resultado = not a
print(resultado)
'''
'''
valor = int(input("Digite un numero:"))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f' El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} no esta dentro del Rango')
'''
'''''
# Ejercicio con el operador OR

print(" Vamos a verificar si un padre e asistir al juego de su hijo")
print("responda lo siguente:")
vacaciones = False
diaLibre = False
if not (vacaciones or diaLibre):
    print(" Tiene trabajo que hacer : ")
else:
    print("puede asistir al juego")
'''
'''''
# Ejercicio Rango entre 20 y 30 años

edad = int(input("Digite su edad:"))
#veinte = edad >= 20  and edad > 30
#treinta = edad >= 30 and edad < 40
#print(treinta)

#    if veinte:
#        print(" estas dentro del rango de los (20\'0) años ")
#    elif treinta :
#        print(" Estas dentro del rango de los (30'0) años")
#    else:
#        print(" no estas dentro del rango")
# sintaxis simplificada del operador and
if (20 <= edad < 30) or (30 <= edad < 40):
    print(" Estas dentro del rango de los (20) a los (30) años")
#if veinte or treinta :
else:
    print(" No estas dentro del rango de los (20) a los (30) años")
'''
'''
numero1 = int(input(" Digite el valor para el numero 1:"))
numero2 = int(input(" Digite el valor para el numero 2:"))

if numero1 > numero2:
    print(" El numero 1 es mayor")
else:
    print("El numero 2 es mayor")
'''

# Ejercicio tienda de libros

print(" Digite los siguientes datos del libro")
nombre = input(" Digite el nombre del libro: ")
id = int(input(" Digite el ID del libro: "))
precio = float(input( " Digite el precio del libro: "))
envioGratuito = input(" Indicar si el envio es gratuito (True/false): ")
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito= False
else:
    envioGratuito = " El Valor es incorrecto, debe escribir True/False"
print(f'''
        Nombre: {nombre}
        ID: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}
''')



