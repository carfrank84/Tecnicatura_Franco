class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura


def crear_rectangulo(num):
    print(f'\nDatos del rectángulo {num}:')
    altura = int(input(f'Ingrese en cm la altura del rectángulo {num}: '))
    base = int(input(f'Ingrese en cm la base del rectángulo {num}: '))
    return Rectangulo(altura, base)


rectangulo1 = crear_rectangulo(1)
rectangulo2 = crear_rectangulo(2)
rectangulo3 = crear_rectangulo(3)

print(f'\nEl cálculo del área del rectángulo 1 es: {rectangulo1.calcular_area()} cm²')
print(f'El cálculo del área del rectángulo 2 es: {rectangulo2.calcular_area()} cm²')
print(f'El cálculo del área del rectángulo 3 es: {rectangulo3.calcular_area()} cm²')
