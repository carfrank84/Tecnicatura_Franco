# ejercicio 3: Insertar elementos y ordenarlos
#pedir numeros y meterlos en una lista, cuando el usuario
# introduzca un numero 0, nuestro programa dejaria de inseretar .
# por ultimo , mostrar los numeros ordenados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()# La lista esta ordenada con esta funcion
print(f'\nLista Ordenada: \n{lista}')