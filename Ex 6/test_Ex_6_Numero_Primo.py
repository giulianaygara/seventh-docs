import unittest
from Ex_6_Numero_Primo import numero_primo

class TestNumeroPrimo (unittest.TestCase):
    
    def test_numeros_primos(self):
        numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        
        for numero in numeros_primos:
            self.assertTrue (numero_primo(numero))
            
    def test_numeros_nao_primos (self):
        numeros_nao_primos  = [4, 6, 8, 10, 12]
        
        for numero in numeros_nao_primos:
            self.assertFalse = (numero_primo(numero))
        
if __name__ == '__main__':
    unittest.main()             