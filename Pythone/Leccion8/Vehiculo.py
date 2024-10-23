class Vehiculo:
    '''
    Definir una clase padre llamada vehiculo y dos clases hijas llamdas
    Auto y Bicicleta, las cuales heredan de la clase padre vehiculo.
    La Clase padre debe tener los siguientes atributos y metodos:

    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Metodos(__init__() y __str__())

    Auto(clase hija de vehiculo)
    -Atributos (Velocidad(Km/h))
    -Metodos(__init__()) y (__str())

    Bicicleta(clase hija de vehiculo)
    -Atributos (tipo(urbana/montaña/etc.)
    -Metodos(__init__() y __str__())

    Crear un objeto de cada clase
    '''

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'color: '+self.color+', Ruedas: '+ str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color , ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return  super().__str__() + ', Velocidad(Km-hr): '+ str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+', Tipo: '+self.tipo
# Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

# segundo objeto
auto = Auto('Amarillo', 4, 120)
print(auto)

# tercer objeto, el ultimo de la clase hija Bicicleta
bici = Bicicleta('Azul', 2, 'Urbana')
print(bici)

