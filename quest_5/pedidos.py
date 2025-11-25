# 5) Sistema de E-commerce Em um sistema de pedidos online, um Pedido contém vários ItensDePedido. 
# Cada ItemDePedido representa um produto e a quantidade (ex: "2x Teclado Gamer") e só existe no contexto daquele pedido específico. 
# Se o Pedido for cancelado e excluído, todos os seus ItensDePedido também devem ser. 
# Implemente as classes Pedido e ItemDePedido, aplicando o relacionamento correto entre elas.

class ItemDePedido:
    def __init__(self, produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.quantidade} x {self.produto}"


class Pedido:
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente
        self.itens = []   

    def adicionar_item(self, produto, quantidade):
        item = ItemDePedido(produto, quantidade)
        self.itens.append(item)

    def remover_item(self, produto):
        self.itens = [item for item in self.itens if item.produto != produto]

    def excluir_pedido(self):
       
        self.itens.clear()
        print("Pedido excluído e todos os itens removidos.")

    def listar_itens(self):
        print(f"Itens do pedido de {self.nome_cliente}:")
        for item in self.itens:
            print(" -", item)

pedido = Pedido("João")

pedido.adicionar_item("Teclado Gamer", 3)
pedido.adicionar_item("Mouse RGB", 1)

pedido.listar_itens()

pedido.remover_item("Mouse RGB")
pedido.listar_itens()

pedido.excluir_pedido()
pedido.listar_itens()
