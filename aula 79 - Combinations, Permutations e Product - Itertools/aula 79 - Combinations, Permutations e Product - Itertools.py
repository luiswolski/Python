"""
Combinations,PermutationseProduct-Itertools
Combinação-Ordem não importa
Permutação-Ordem importa
Ambos não repetem valores únicos
Produto-Ordem importaerepete valores únicos                  I
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']
for grupo in combinations(pessoas, 2):
    print(grupo)
