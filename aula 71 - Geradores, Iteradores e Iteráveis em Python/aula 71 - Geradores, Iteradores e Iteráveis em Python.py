import sys
import time

"""
ESSA FUNCAO DIZ QUANTO DE MEMORIA A LISTA ESTA OCUPANDO

lista = list(range(10))
print(sys.getsizeof(lista))

-----------------------------------------------------

l1 = [x for x in range(1000)] -> Isso é uma lista que ocupa 2400 na memoria
l1 = (x for x in range(1000)) -> Isso é um gerador que ocupa 88 na memoria
"""
def gera():
    for n in range(100):
        yield n     #apresenta os elementos do gerador assim que os mesmos são gerados
        time.sleep(0.1)

g = gera()

for v in g:
    print(v)
