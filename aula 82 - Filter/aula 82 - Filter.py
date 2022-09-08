from dados import produtos, pessoas, lista

def filtra(produto):
    if produto['preco'] > 50:
        return True

nova_lista = filter(filtra, produtos)
#nova_lista = filter(lambda p: p['preco'] > 50, produto)
#nova_lista = [x for x in lista if x > 50]

for produto in nova_lista:
    print(produto)