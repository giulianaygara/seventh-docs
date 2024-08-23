import unittest
from calculadora import Calculadora

class TesteCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculo = Calculadora(1,2)
        
    def test_dividir_numeros_positivos(self):
        resultado = self.calculo.dividir(10,2)
        self.assertEqual(resultado, 5)
    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calculo.dividir(10,0)
            
    def test_divisao_de_zero_por_numero(self):
        resultado = self.calculo.dividir(10,0)
        self.assertEqual(resultado, 0)      #ou self.assertEqual(self.calculo.dicidir(50,10),5)   
        
if __name__ == '__main__':
    unittest.main()       