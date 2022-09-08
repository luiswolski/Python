class CarrinhoDeCompras:
    def __init__(self):
        self.produto = []

    def inserir_produto(self, prpoduto):
        self.produto.append(prpoduto)

    def lista_produto(self):
        for produto in self.produto:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produto:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
