import unittest
from ex_1_Calculadora import Calculadora



class test_calculadora(unittest.TestCase):
         
    def test_soma (self):
        self.assertEqual(Calculadora.soma(2,3) ,5)
        self.assertEqual(Calculadora.soma(-1,-1) ,-2)
        self.assertEqual(Calculadora.soma(-1,1) ,0)
        self.assertEqual(Calculadora.soma(0,0) ,0)
        self.assertEqual(Calculadora.soma(22,22) ,44)
        
    def test_subtracao (self):
        self.assertEqual(Calculadora.subtracao(1,1) ,0)
        
    def test_multiplicacao (self):
        self.assertEqual(Calculadora.multiplicacao(5,2) ,10)
        
    def test_divisao (self):
        self.assertEqual(Calculadora.divisao(15,5) ,3)            
        
    
if __name__=='__main__':
    unittest.main()
         