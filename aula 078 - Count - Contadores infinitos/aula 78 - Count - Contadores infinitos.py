"""
cout - intertools
"""
from itertools import count

contador = count(start=5, step=-0.5)

for valor in contador:
    print(round(valor, 2))

    if valor >= 100 or valor <= -10:
        break

#------------------------------------------------

indice = count(start=1)
lista = ['luis', 'joao', 'maria']

lista = zip(indice, lista)
print(list(lista))