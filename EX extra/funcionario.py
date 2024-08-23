class Funcionario:
    taxa_incrementar_salario = 1.05

    def __init__(self, nome, sobreNome, salario):
        self.nome = nome
        self.sobreNome = sobreNome
        self.salario = salario
        self.email = nome + '.' + sobreNome + '@email.com'
    
    def aumentar_salario(self):
        self.salario = int(self.salario * self.taxa_incrementar_salario)

