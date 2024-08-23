import unittest
from conta_bancaria import ContaBancaria

class TesteDeAceitaçãoContaBancaria(unittest.TestCase):
    def test_fluxo_completo_de_uso(self):
        conta = ContaBancaria('João', saldo_inicial=100)
        self.assertEqual(conta.verificar_saldo(), 100)
        
        conta.depositar(50)
        self.assertEqual(conta.verificar_saldo(), 150)
        conta.sacar(30)
        self.assertEqual(conta.verificar_saldo(), 120)
        
        with  self.assertRaises(ValueError):
            conta.sacar(200)
            
        self.assertEqual(conta.verificar_saldo(), 120)    
        
if __name__=='__main__':  
   unittest.main()
        