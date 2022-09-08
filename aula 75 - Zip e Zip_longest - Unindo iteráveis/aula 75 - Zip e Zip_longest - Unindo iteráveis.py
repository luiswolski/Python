"""
Zip - Unindo iteráveis
Zip - longest - Itertools
"""
from itertools import zip_longest, count #so o zip não iria apresentar monte belo

indice = count()
cidades=['São Paulo','Belo Horizonte','Salvador','Monte Belo']
estados=['SP','MG','BA']

cidades_estados=zip(
    indice,
    estados,
    cidades,
)

for valor in cidades_estados:
    print(valor)
   # print(indice, estados, cidades)