class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, dni,  edad, *args, **kwargs):  # se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad} años ,  la direccion es:  {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Ariel', 'Betancud', 30672841, 40)  # Necesitamos enviar argumentos
print(f'El Objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad} años')

persona2 = Persona('Osvaldo', 'Giordanini', 616161, 45)
print(f'El Objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad} años')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(
    f'El Objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad} años')

# Los atributos son : caracteristicas
# los metodos son : el comportamiento que van a tener los objetos
persona1.mostrar_detalle() # la referencia se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle() # debemos pasarle una referencia para el self o dara error
persona1.telefono = '2616661061'
print(f'Este es el telefono: {persona1.nombre} {persona1.telefono}') # Hemos creado un atributo de un objeto

# print(persona2.telefono) # el objeto persona2 no tiene este atributo, da error
persona3 = Persona('Rogelio', 'Romero',3613626163,  22, 'Telefono', '2616632215', 'Calle Aconcagua', 22, 'Manzana', 77,'casa', 2, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021 )
persona3.mostrar_detalle()
persona4 = Persona('Franco', 'Poblete', 22 , 'Telefono: ', '2616632215', 'Barrio Jardin el Challao', 'Manzana:', 'C','casa: ', 5, Altura=1.80, Peso=150, CFavorito='Verde', Auto='Honda', Modelo=2024 )
persona4.mostrar_detalle()
# print(persona3._dni) # esto no se debe utilizar(esta encapsulado), esto dice que lo desconocemos
# persona3.__nombre # esta totalmente encapsulado no se puede mostrar


