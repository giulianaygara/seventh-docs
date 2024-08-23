class Item:
    def __init__(self, NomeDoItem):
         self.NomeDoItem = NomeDoItem
         
class GerenciadorDeEstoque:
    def __init__(self):
            self.estoque ={} 
                
    def cadastrar_item(self, id_item, NomeDoItem):
        if id_item in self.estoque:
            raise ValueError("Item, com esta ID já existe")  
        self.estoque[id_item] = Item(NomeDoItem)
        
    def listar_itens(self):
        return{id_item: item.NomeDoItem for id_item, item in self.estoque.items()}
    
    def editar_item(self, id_item, novo_NomeDoItem):
        if id_item not in self.estoque:
            raise ValueError("Item não cadastrado no estoque")
        self.estoque[id_item].NomeDoItem = novo_NomeDoItem
        
    def excluir_item(self, id_item):
        if id_item not in self.estoque:
            raise ValueError("Item Não cadastrado no estoque")
        del self.estoque[id_item]
                
                      
             