class Calculadora():
    def soma(x, y):
        return x + y
    
    def subtracao(x, y):
        return x - y
    
    def multiplicacao(x, y):
        return x * y
    
    def divisao(x,y): 
        if y == 0:
            raise ValueError('Can not be divivide by zero')
        return x/y