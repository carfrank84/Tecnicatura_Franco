# Ejercicio 1:
# Escribir la siguiente Expresion en forma de
# expresion algoritmica.
# a3 x (b2-2ac)/2b
# 1. Pedimos al usuario 3 valores = a,b,c
# 2. Pedimos el resultado final

a = float(input(" Ingrese un valor para a:"))
b = float(input(" Ingrese un valor para b:"))
c = float(input(" Ingrese un valor para c:"))

resultado = (a**3*(b**2)-(2*a*c)) / (2*b)
print(f"el resultado es :{resultado}")
