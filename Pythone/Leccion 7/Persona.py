# Clase base Persona
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor
    def __str__(self): # Override = sobreescribir
        return f'Persona: [Nombre: {self.__nombre}, Edad: {self.__edad}]'

# Clase hija Empleado
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.__sueldo = sueldo

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, valor):
        self.__sueldo = valor
    def __str__(self):
        return f'Empleado: [ Sueldo: {self.__sueldo}] {super().__str__()}'

# Creación de los objetos Empleado
empleado1 = Empleado('Franco', 40, 75000)
empleado2 = Empleado('Laura', 35, 68000)

# Mostrar datos de empleado1 y empleado2
print(f"Nombre: {empleado1.nombre}")
print(f"Edad: {empleado1.edad}")
print(f"Sueldo: {empleado1.sueldo}")

print(f"\nNombre: {empleado2.nombre}")
print(f"Edad: {empleado2.edad}")
print(f"Sueldo: {empleado2.sueldo}")

# Modificación de datos de empleado1 usando los setters
empleado1.nombre = 'Maxi'
empleado1.edad = 33
empleado1.sueldo = 100000

# Modificación de datos de empleado2 usando los setters
empleado2.nombre = 'Carla'
empleado2.edad = 37
empleado2.sueldo = 72000

# Mostrar nuevamente los datos modificados de empleado1 y empleado2

# Empleado 1
print("\nDatos modificados del primer empleado:")
print(f"Nombre: {empleado1.nombre}")
print(f"Edad: {empleado1.edad}")
print(f"Sueldo: {empleado1.sueldo}")

# Empleado 2
print("\nDatos modificados del segundo empleado:")
print(f"Nombre: {empleado2.nombre}")
print(f"Edad: {empleado2.edad}")
print(f"Sueldo: {empleado2.sueldo}")
