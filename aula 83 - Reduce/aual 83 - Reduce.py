from dados import produtos, pessoas, lista
from functools import reduce

soma_precos = round(reduce(lambda ac, p: p['preco'] + ac, produtos, 0), 2)
print(soma_precos / len(produtos))