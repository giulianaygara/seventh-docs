import unittest
from desenvolvedor import Desenvolvedor

class TesteDesenvolvedor(unittest.TestCase):
    def setUp(self):
        self.dev1 = Desenvolvedor('Giulia', 'Naygara', 10000, 'Python', 'Junior')
        
    def test_aumentar_salario(self):
        self.assertEqual(self.dev1.nome, 'Giulia')
        self.assertEqual(self.dev1.sobrenome, 'Naygara')    
        self.assertEqual(self.dev1.salario, 10000)
        self.assertEqual(self.dev1.linguagemProgramação, 'Python')
        self.assertEqual(self.dev1.senioridade, 'Junior')
        self.dev1.aumentar_salario()
        self.assertEqual (self.dev1.salario, 10500)
 
if __name__ == '__main__': 
  unittest.main()      