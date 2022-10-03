"""
Split,Join,Enumerate em Python
*Split-Dividir uma string#str
*Join Juntar uma lista#str
*Enumerate-Enumerar elementos da lista #iteráveis
"""

string = "Vou aprender a utilizar as funções de lista, será que vai dar bom."
lista_split = string.split(' ')
lista_join = ' '.join(lista_split)

var1 = None
var2 = None

for indice, valor in enumerate(lista_split):
    print(indice, valor)

print(f'O total de elementos desta lista é: {len(lista_split)}')
print('\n\n')
print(string)
print(lista_split)
print(lista_join)