"""

"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# colocando a lista em outra lista
ex1 = [variavel for variavel in l1]
# passsando a lista porem multiplicando os elementos por 2
ex2 = [v * 2 for v in l1]
# passando a lista e adicionando elementos, lista dentro de lista
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
# alterando elementos dentro de itens da lista
l2 = ['luis', 'wolski', 'correa']
ex4 = [v.replace('a', '@') for v in l2]
# alterando os valores de tuplas
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
)
ex5 = [(y, x) for x, y in tupla]
# transformando em dicionario
ex5 = dict(ex5)
# filtrando lista
l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
# como usar o else, usando o if invertido
ex7 = [v if v % 3 == 0 else 'X' for v in l3]
print(ex7)
