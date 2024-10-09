class Carrinho:
    def __init__(self):
        self._produtos = []
    
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produto(self, *produtos):
        #self._produtos += produtos -> outra forma de add
        #self._produtos.extend(produtos) -> outra forma de add
        
        for produto in produtos:
            self._produtos.append(produto)

    def listar_protudos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


compras = Carrinho() # Não é preciso passar atributos aqui pois no init não tem atributos declarados
p1, p2 = Produto('Maionese', 13), Produto('Mangá One Piece', 30) #poderia ser feito individualmente 
#(cada um em uma linha)

compras.inserir_produto(p1, p2) # momento em que a agregação é feita
compras.listar_protudos()
print(compras.total())
