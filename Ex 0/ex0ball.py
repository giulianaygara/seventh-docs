class Bola():
   def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

   def mostraCor(self):
       print('A cor da bola é: ', self.cor )
   def trocaCor(self, novaCor):
       self.cor = novaCor
       print('Nova cor da bola: ', self.cor )


bola = Bola('Vermelha', '20cm', 'Borracha')
bola.mostraCor()      

bola.trocaCor('azul')
bola.mostraCor()
