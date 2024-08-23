import unittest
from ex0ball import Bola

class TesteBola(unittest.TestCase):
    
    def setUp (self):
        self.bola = Bola("Vermelha", "20cm", "Borracha")
    
    def test_trocaCor(self):
       self.bola.trocaCor("Verde")
       self.assertEqual( self.bola.cor,"Verde")
        
if __name__ == '__main__':
    unittest.main()           
     