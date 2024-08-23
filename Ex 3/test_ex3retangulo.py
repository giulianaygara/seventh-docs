import unittest
from ex3retangulo import Retangulo

class TesteRetangulo(unittest.TestCase):
    
    def  test_calcular_area (self):
        retangulo = Retangulo (5, 3)
        
        self.assertEqual(retangulo.largura, 5)
        self.assertEqual(retangulo.altura, 3)
        
        area = retangulo.calcular_area()
        self.assertEqual (area, 15)
        
if __name__ =='__main__':
    unittest.main()        