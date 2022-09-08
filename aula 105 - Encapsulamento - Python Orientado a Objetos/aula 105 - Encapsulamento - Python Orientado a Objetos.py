"""
Em outra linguagens de programação tal qual C++
exitem diferentes classes para a proteção dos dados
public, protected, private

No python isso NÃO existe! Porem a algo que indica isso

_ -> protected
__ -> private
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados ['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Luis')
bd.inserir_cliente(2, 'Felipe')
bd.inserir_cliente(3, 'Wolski')
bd.inserir_cliente(4, 'Correa')

bd.__dados = 'Outra Coisa'
print(bd.__dados)
print(bd._BaseDeDados__dados)
bd.lista_clientes()