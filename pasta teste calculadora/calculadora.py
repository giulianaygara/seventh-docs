class Calculadora:
    def __init__(self, numerador, denominador): #se for realmente um teste, não é necessário
        self.numerador = numerador #linha 1-4 é classe construtora
        self.denominador = denominador
        
    def dividir(self, numerador, denominador):
        if denominador == 0:
            raise ValueError('Não é possível dividir por 0')
        print(self.numerador/self.denominador)
        return numerador / denominador
divisao = Calculadora(10,2)    
divisao.dividir(10,2)