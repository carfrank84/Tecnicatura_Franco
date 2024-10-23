# Lista = Franco , Maxi, irene, eze
# Colecciones en Pyton
# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores
nombres = ["Franco", "Maxi", "Irene", "Eze"]
print(nombres)
print(nombres[0:2])#  solo muestra el indice 0,1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])# indices a mostrar 0,1,2
#desde el indice indicado hasta el final
print(nombres[1:])
# modificamos un valor
nombres[2]= " felipe"
nombres[0]= "valentin"
print(nombres)
# iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista ")

# preguntamos cuantos elementos tiene
print(len(nombres))# le pasamos como parametro la lista

# agregamos un elemento

nombres.append("julian")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4 , 5])
nombres.append(7)
print(nombres)

# insertar un nuevo elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3, "Nicole")
print(nombres)

# eliminamos un elemento

nombres.remove("Alberto")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# eliminamos un indice especifico
del nombres[2] # del significa delete (eliminar)
print(nombres)
# elimninar borrar o limpiar todos los elementos del la lista
nombres.clear()
print(nombres)

# eliminar la lista
del nombres
#print(nombres) # aqui nos mostrara un error

# definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))

# acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# mostrar de la manera inversa
print(cocina[-1])

# como acceder a un rango
print(cocina[0:2])
# amodo de ejemplo
verduras = ("papa",)# una tupña necesitta , un que sea de un solo elemento la coma
# de lo contrario solo seria un tipo string cadena

# recorrer los elementos de la tupla

for cocinar in cocina:# print ersta usando \n para saltos de linea
    print(cocinar, end=" ") # usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print("\n", cocina)
#del cocina
#print(cocina) # muestra el error por que se borro la tupla

# Tipo set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas)) # usamos la funcion len = length significa largo
# revisar si un elemento existe dentro de set
print('Marte' in planetas)

# agregar un elemento
planetas.add('Tierra')# add es una funcion
print(planetas)
# Eliminar elemento, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter') # esta funcion ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard('Tierra')# esta funcion no nos presenta ningun tipo de error
print(planetas)
# limpiar set
planetas.clear()
print(planetas)
#eliminar set o conjunto
del planetas
#print(planetas) # al eliminar nos muestra error

# Diccionarios: 'Maradona':10 un diccionario esta compuesto
# por dos elementos
#UNA LLAVE Y UN VALOR
# dict(key, value)
diccionario = {
    'IDE' : 'Integrated Development Environment',
    'POO' : 'Programacion Orientada a Objetos',
    'SABD' : 'Sistema de Administracion de Base de Datos'
}
# verificar la cantidad de elemenrtos del diccionario
print(len(diccionario))
print(diccionario)

# acceder al diccionario con la llave (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = " Entorno de Desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)
# necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

   # OTRAS MANERAS DE ACCEDER A UN DICCIONARIO
for termino in diccionario.keys(): # estamos usando una funcion
    print(termino) # muestra solo las llaves

for valor in diccionario.values(): # usamos una funcion para acceder a un valor
    print(valor)

# comprobar la existencia de un elemento
print('IDE' in diccionario) # devuelve un booleano

# agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# vaciar un diccionario
diccionario.clear()

# eliminar diccionario
del diccionario
#print(diccionario)

# concatenar listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 # concatenamos
print(lista3)

lista3.extend([7, 8, 9, 1]) # funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) #esto daria un error por no ser el elemento parte de la lista

# como saber cuantos elementos repetidos hay en una lista
print(lista3.count(1))# cuenta cuantos valores iguales hay dentro de la lista

# para poner al reves la lista
lista3.reverse()
print(lista3)

# Para que la lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse = True) # Ordena descendentemente
print(lista3)

# Repaso de Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
# En tuplas se puede convertir de tupla a lista y de lista a tupla.

#repaso de set o conjunto
# para definir un conjunto
conjunto2 = set ()
conjunto1 = {'bye'}
conjunto2.add(7)
conjunto2.add("Hola ")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) # preguntamos si el numero 3 no esta en el conjunto1

# como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # nos devuelve como respuesta un booleano

# operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La Linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # asigna el valor que esta en el conjunto 1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto2.issubset(conjunto3)) # aqui preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto1.issubset(conjunto3)) # si es verdadero quiere decir que  el conjunto3 es superconjunto
print(conjunto2.issubset(conjunto3))

# como saber si ambos conjuntos son disconexos esto es si no comparten elementos en comun

print(conjunto1.isdisjoint(conjunto2)) # no hay cosas en comun

# convertir un conjunto totalemte en inmutable
conjunto1 = frozenset # esto hace que el conjunto sea totalmente inmutable
# no se puede agregar , modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = { 'Azul': 'Blue', 'Rojo' : 'Red' , 'Verde' : 'Green', 'Amarillo' : 'Yellow'}
print(diccionarioNuevo)

# como eliminar
del(diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = { 'Franco' : {'Edad': 40, 'Altura' : 1.83}, 'Maxi' : [ 45, 1.85], 'Agustin' : [35, 1.67] }
print(diccionario2)

# Ejercicio Seleccion Argentina

seleccionArgentina = {
    10 : {'Nombre' : 'Lionel Messi', 'Edad' : 35, 'Altura' : 1.70, 'Precio' : ' 50 millones', 'Posicion' : "Extremo Derecho"},
    11 : {'Nombre' : 'Angel Di Maria', 'Edad' : 34, 'Altura' : 1.80, 'Precio' : ' 12 millones', 'Posicion' : "Extremo Derecho"},
    24 : {'Nombre' : 'Paulo Dybala', 'Edad' : 28, 'Altura' : 1.77, 'Precio' : ' 35 millones', 'Posicion' : "Media Punta"},
    19 : {'Nombre' : 'Nicolas Otamendi', 'Edad' : 34, 'Altura' : 1.83, 'Precio' : ' 3.5 millones', 'Posicion' : "Defensa Central"},
    1: {'Nombre' : 'Franco Armani', 'Edad' : 35, 'Altura' : 1.89, 'Precio' : ' 3.5 millones', 'Posicion' : "Portero"},
    }
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print(len(seleccionArgentina))


# Pilas Usando listas
pila = [1, 2, 3]

# Agregamos elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el ultimo elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La Pila ahora quedo asi:{pila} ')

# colas con listas
# Estructura de datos de tipo fifo(first input / first output)
cola = ['Franco', 'Maxi', 'Irene', 'Valentin']

# Agregamos elementos al final de la cola
cola.append('Felipe')
cola.append('Agustin')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(' Ya no quedan clientes en la fila')


# Seguimos mostrando como recorrer un diccionario con el ciclo for

for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')


# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+''+lastName)
person = ['Franco','Poblete ']
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anterior pero lo pasamos todo junto
person2 = ('Maxi', 'Montenegro') # Desempaquetamos a travez de una tupla
show(*person2)
person3 = {'LastName' : 'Machuca', 'Name':'Machuca'}
show(*person3)

numbers = [1,2,3,4,5] # Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # esta es la unica manera para que no se ejecute el else
else:
    print(' Esto se termino')

# List comprehension, Lista de Comprension
names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe']
alongP = [p for p in names if p[0] == 'P'] # Esto regresa una nueva lista
print(alongP)

bottleC = [{'Name': 'Quilmes', 'Country': 'Arg'},
           {'Name': 'Corona', 'Country':'Mx'},
           {'Name':'Stella Artois', 'Country':'Belgium'},
           ]
Arg = [b for b in bottleC if b['Country'] == 'Arg']
print(Arg)
print(bottleC)

# Paso de argumentos (funciones)
def mifuncion2(name, lastName):
    print('Saludos a todos lo que ven a traves del canal de youtube')
    print(f'Nombre: {name}, apellido: {lastName}')
mifuncion2('Jorge','Lucero')
mifuncion2('Ariel', 'Betancud')
mifuncion2('Analia', 'Pedrosa')

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a,b):
    return a + b
#resultado = sumar(78,22)
#print(f"El resultado de la suma es : {resultado}")
print(f"El reultado de la suma es: {sumar(55,45)}")

def sumar2(a =0, b = 0):# le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22,66)}')

# Argumentos, variables en funciones
def listarNombres (*nombres) -> object: # normalmente se utiliza: *args
    for nombre in nombres: # se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa' , 'Maria')
listarNombres('Marcos', 'Daniel','Romina', 'Pepe', 'Marcela', 'Carlos')

def listarTerminos(**terminos):#Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): # kwargs significa: key word argument
        print(f'{llave} : {valor}')

listarTerminos()# no recibe nada nada se va a mostrar
listarTerminos(IDE='Integrated Development Enviroment', pk= 'Primary Key')
listarTerminos(Nombre='Leonel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 =['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# DesplegarNombres(10,11) # no es un objeto iterable
desplegarNombres((10,11)) # La convertimnos en una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22,55]) # La convertimos a una Lista

# Funciones recursivas
def factorial(numero):
    if numero == 1: # caso base
        return 1
    else:
        return numero * factorial(numero -1) # Caso Recursivo
# resultado = factorial(5) # Lo hacemos en codigo duro
# print(f'El factorial del numero 5 es : {resultado}') # Tarea que el usuario ingrese el numero para realizar el factorial

# Pedir al usuario que ingrese un número
numero_usuario = int(input("Ingresa un número para calcular su factorial: "))

# Llamar a la función y mostrar el resultado
resultado = factorial(numero_usuario)
print(f'El factorial del número {numero_usuario} es: {resultado}')












