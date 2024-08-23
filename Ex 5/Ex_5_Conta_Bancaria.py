# 5 - Desenvolva um arquivo de teste para o 
# seguinte programa:

class ContaBancaria:
    def __init__(self, titular):
        self.saldo = 0
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            raise Exception('O valor do saque é maior que o saldo!')
        
conta = ContaBancaria("João")
conta.depositar(1000)
conta.sacar(500)
conta.sacar(700)
print("Saldo final: R$ {:.2f}".format(conta.saldo))
    
            
        