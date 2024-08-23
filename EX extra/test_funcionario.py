import unittest
from funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    def setUp(self):
        self.funcionario1 = Funcionario('Oto', 'Lima', 3000)
        
    def test_aumentar_salario(self):
      self.assertEqual(self.funcionario1.nome, 'Oto')
      self.assertEqual(self.funcionario1.sobreNome, 'Lima') 
      self.assertEqual(self.funcionario1.salario, 3000)
      self.assertEqual(self.funcionario1.email, 'Oto.Lima@email.com')
      
      self.funcionario1.aumentar_salario()
      self.assertEqual(self.funcionario1.salario, 3150)
      
if __name__ == '__main__':
     unittest.main()    