class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Metodo Getter
        print('Estamos utilizando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # Metodo Getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Metodo setter
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # Metodo Getter
        return self._edad

    @edad.setter
    def edad(self, edad):  # Metodo setter
        self._edad = edad

    def __del__(self):
        print(f'Persona2:{self._nombre} {self._apellido} {self._edad}')
# Pruebas
if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre)  # Llamamos al metodo Getter
    print(persona1.apellido)  # Llamamos al metodo Getter
    print(persona1.edad)  # Llamamos al metodo Getter

    persona1.nombre = 'Juan Pablo'
    print(persona1.nombre)

    persona1.apellido = 'González'
    print(persona1.apellido)

    persona1.edad = 30
    print(persona1.edad)

    print(persona1.mostrar_detalles()) # Llamamos al metodo mostrar detalles
    # atributo read-only seria la edad por que no tiene el metodo setter
    print(persona1.edad)

    #tarea crear tyres objetos mas utilizando los metodos getter and setter
    # para modificar, y mostar los cambios

    # objeto N° 1
    persona2 = Persona2('Nicole', 'Riveros', 33)
    persona2.nombre = 'Marcela'
    persona2.apellido = 'Padilla'
    persona2.edad = 30
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalles())

    # Objeto N° 2
    persona3 = Persona2('Rocio', 'Poblete', 10)
    persona3.nombre = 'Abril'
    persona3.apellido = 'Riveros'
    persona3.edad = 8
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalles())

    # Objeto N° 3
    persona4 = Persona2('Emma', 'Riveros', 9)
    persona4.nombre = 'Victoria'
    persona4.apellido = 'Poblete'
    persona4.edad = 6
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalles())

    print(__name__)
