# Ejercicio 6 : tabla de multiplicar
# hacer un programa que pide un número por teclado y guarde en una lista
# su tabla de multiplicar hasta el 10 por ejemplo: si digita el 5 la lista
# tendrá 5 10 15 20 25 30 35 40 45 50

numero = int(input("Digite un número: "))
print(f'\nTabla de multiplicar del {numero}:')
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')


