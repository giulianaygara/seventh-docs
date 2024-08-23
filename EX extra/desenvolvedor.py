import funcionario
class Desenvolvedor(funcionario):
    def __init__(self, nome, sobreNome, salario, linguagemProgramacao, senioridade):
        super().__init__(nome, sobreNome, salario)
        self.linguagemProgramacao = linguagemProgramacao
        self.senioridade = senioridade
        
    def mostrar_linguagem_e_senioridade(self):
        print('---------- Mostrando dados -----------')
        print('linguagem de Programacao: ', self.linguagemProgramacao)
        print('Senioridade: ', self.senioridade)

"""    
funcionario1 = Funcionario('Anderson', 'Lima', 3000)
funcionario1.mostrar_dados()

funcionario1.aumentar_salario()
funcionario1.mostrar_dados()

dev1 = Desenvolvedor('William', 'Silva', 5000, 'Python', 'Pleno')
dev1.mostrar_dados()

dev1.aumentar_salario()
dev1.mostrar_dados()
dev1.mostrar_linguagem_e_senioridade() 
"""    