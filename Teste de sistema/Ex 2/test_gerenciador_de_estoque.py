import unittest
from gerenciador_de_estoque import GerenciadorDeEstoque

class TesteGerenciadorDeEstoque(unittest.TestCase):
    def setUp(self):
         self.gerenciador = GerenciadorDeEstoque()
         
    def test_criar_e_listar_estoque(self):
        self.gerenciador.cadastrar_item(1, 'Cimento')
        self.gerenciador.cadastrar_item(2, 'Tijolo')
        self.gerenciador.cadastrar_item(3,'Areia')
        
        estoque = self.gerenciador.listar_itens()
        self.assertEqual(len(estoque), 2)
        self.assertEqual(estoque[1], 'Cimento')
        self.assertEqual(estoque[2], 'Tijolo')
        self.assertEqual(estoque[3], 'Areia')
           
    def test_editar_item(self):
        self.gerenciador.cadastrar_item(1, 'Cimento')
        self.gerenciador.editar_item(1, 'Calabresa')
        
    def test_excluir_item(self):
        self.gerenciador.cadastrar_item(1, 'Cimento')
        self.gerenciador.excluir_item(1) 
        
    def test_fluxo_completo_de_uso(self):
        # Criar e verificar a criação das tarefas 
        self.gerenciador.cadastrar_item(1, "Cimento")
        self.gerenciador.cadastrar_item(2, "Tijolo")
        self.gerenciador.cadastrar_item(3, "Areia")
        
        estoque = self.gerenciador.listar_itens()
        self.assertEqual(len(estoque), 3)
        
        # Editar e verificar a edição de uma tarefa
        self.gerenciador.editar_item(1, "Cimento")
        
        item = self.gerenciador.listar_item()[1]
        self.assertEqual(estoque, "Tijolo")
        
        # Excluir e verificar a exclusão de uma tarefa
        self.gerenciador.excluir_item(2)
        item = self.gerenciador.listar_itens()
        self.assertEqual(len(estoque), 1)
        self.assertNotIn(2, estoque)      
if __name__ == '__main__':
    unittest.main()    