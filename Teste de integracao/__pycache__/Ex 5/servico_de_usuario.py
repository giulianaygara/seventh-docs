class ServicoDeUsuario:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados
        
    def criar_usuario(self,id_usuario, nome):
        if self.banco_de_dados.buscar_usuario(id_usuario):
            raise ValueError("Usuário já existe")
        self.banco_de_dados.adicionar_usuario (id_usuario, nome)
        
    def obter_usuario (self, id_usuario):
        usuario = self.banco_de_dados.buscar_usuario(id_usuario)
        if not usuario:
            raise ValueError("Usuário não encntrado")
        return usuario
    
    def deletar_usuario(self, id_usuario):
        if not self.banco_de_dados.buscar_usuario(id_usuario):
            raise ValueError("Usuário não encontrado")
        self.banco_de_dados.remover_usuario (id_usuario)
        
         
            