num = -1
i = 0
factorial = 1

# Repetir hasta que num sea mayor o igual a 0
while num < 0:
    num = int(input("Digite un numero: "))

# Inicializar i y factorial
i = 1
factorial = 1

# Mientras i sea menor o igual a num
while i <= num:
    factorial *= i
    i += 1
print("El Factorial es:", factorial)