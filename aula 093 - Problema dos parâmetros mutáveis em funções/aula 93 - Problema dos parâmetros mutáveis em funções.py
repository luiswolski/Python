# Mutáveis: Listas, dicionários
# Imutáveis: Tuplas, strings, números, True, False, None

def lista_de_clientes(clientes_iteraveis, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteraveis)
    return lista

clientes1 = lista_de_clientes(['joao', 'maria', 'carlos'])
clientes2 = lista_de_clientes(['eduardo', 'debora', 'kezia'])
clientes3 = lista_de_clientes(['luis'])

print(clientes1)
print(clientes2)
print(clientes3)