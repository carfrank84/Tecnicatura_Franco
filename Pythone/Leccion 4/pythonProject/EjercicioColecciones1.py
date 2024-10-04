# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, por ultimo mostrar la lista .

# Creamos una lista
lista = [1,2,3, "Franco", 7,7,3,"Maxi", 5, "Franco"]
# conjunto = set(lista) # convertimos la lista a un conjunto de tipo set
# lista = list(conjunto) #convertimos el conjunto a una lista
lista = list(set(lista)) # la conversion hecha en una sola linea de codigo (eficiente)
print(lista)
