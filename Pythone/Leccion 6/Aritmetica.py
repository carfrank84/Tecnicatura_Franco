class Aritmetica:
    '''
    El nombre de este tipo de comentario es : DocString
    esto es documentacion de la clase Paython
    vamos a hacer en esta clase algunas operaciones de : suma, resta, multiplicacion y mas
    '''

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    # metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    # Metodo para restar
    def resta(self):
        return self.operandoA - self.operandoB
    # metodo para multiplicar
    def multiplicar(self):
        return self.operandoA * self.operandoB
    # metodo para dividir
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7, 9) # Le pasamos para los operandos
print(f'El resultado de la suma es :{aritmetica1.sumar()}')
print(f'El resultado de la resta es: {aritmetica1.resta()}')
print(f'El resultado de la multiplicacion es: {aritmetica1.multiplicar()}')
print(f'El resultado de la division es: {aritmetica1.dividir(): .2f}')







