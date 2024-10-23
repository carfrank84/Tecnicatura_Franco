# Ejercicio 2: funcion *args para multiplicar
# crear una funcion para multiplicar los valores recibidos
#de tipo numerico utilizando argunentos variables *args
# como parametro de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados como argumentos

# definimos la funcion para multiplicar
def multiplicar_valores(*args): # El mas utiliizado es *args
    resultado = 1 # el cero no nos ayuda a multiplicar
    for numero in args:
        resultado *= numero
    return resultado
# llamamos la funcion
print(multiplicar_valores(3 ,5 , 15, 3)) # le pasamos los argumentos