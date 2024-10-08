class Cubo:

    '''
    Ejercicio crear la clase cubo con los atributos ,
    ancho, alto y profundidad con un metodo calcular_volumen que tendra la formula :
    volumen = ancho * altura * profundidad, y que el usuario ingrese los valores
    '''
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad


def crear_cubo():
    ancho = int(input('Ingrese en cm el ancho del cubo: '))
    alto = int(input('Ingrese en cm la altura del cubo: '))
    profundidad = int(input('Ingrese en cm la profundidad del cubo: '))
    return Cubo(ancho, alto, profundidad)


cubo = crear_cubo()
volumen = cubo.calcular_volumen()
print(f'El volumen del cubo es: {volumen} cm³')
