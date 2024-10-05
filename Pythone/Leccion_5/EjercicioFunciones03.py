# Ejercicio 3: Funcion recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# puede ser cualquier valor positivo, por ejemplo , si pasamos el
# valor de 5 , debe imprimir :
# 5
# 4
# 3
# 2
# 1
# si se ingresan numeros negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1: # caso base
        print(numero)
        imprimir_numeros_recursivos(numero -1) # caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto...')

#imprimir_numeros_recursivos(5) # Tarea que el numero lo ingrese el usuario
# Pedir al usuario que ingrese un número
numero_usuario = int(input("Ingresa un número : "))

# Llamar a la función y mostrar el resultado
resultado = imprimir_numeros_recursivos(numero_usuario)





