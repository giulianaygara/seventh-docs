import unittest
import banco_de_dados

class BancoDeDados(unittest.TestCase):
    def setUp(self):
        self.bancoDados = banco_de_dados()