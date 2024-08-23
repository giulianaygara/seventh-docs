class Funcionario():
    
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.email  = nome + sobrenome + '@gmail.com'
        
    def salario_aumento(self):
        print('------------aumento de salario ------------')
        self.salario  = self.salario * 1.05
        return self.salario
    
    def mostrar_dados(self):
        print('nome: ', self.nome)
        print('sobrenome: ', self.sobrenome)
        print('salario: ', self.salario)
        

          
class Desenvolvedor(Funcionario):
    
    def __init__(self, nome, sobrenome, salario, linguagem, senioridade):
        super().__init__(nome, sobrenome, salario)
        
        self.linguagem = linguagem
        self.senioridade = senioridade
                
funcionario = Funcionario('Ricardão', 'Cariani', 6000)