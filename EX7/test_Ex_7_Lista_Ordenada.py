import unittest
import Ex_7_Lista_Ordenada

class TestLista(unittest.TestCase):
    
    def test_lista(self):
        lista = [1, 2, 3, 4, 5]
         
        self.assertTrue(Ex_7_Lista_Ordenada.ListOrdenada(lista))
         
    def test_2_lista(self):  
        lista = [5, 7, 6, 8]
        
        self.assertFalse(Ex_7_Lista_Ordenada.ListOrdenada(lista))
        
if __name__ == '__main__':
    unittest.main()         
