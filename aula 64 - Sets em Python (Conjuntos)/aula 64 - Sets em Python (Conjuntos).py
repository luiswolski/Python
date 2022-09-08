"""
add(adiciona),update(atualiza),clear,discard
union|(une)
intersection&(todos os elementos presentes nos dois sets)
difference(elementos apenas no set da esquerda)
symmetric_difference(Elementos que estão nos dois sets,mas não em ambos)
"""

l1 = ['Luis', 'Joao', 'Maria']
l2 = ['Joao', 'Maria', 'Maria', 'Luis', 'Luis', 'Luis', 'Luis']

if set(l1) == set(l2):
    print('L1 e igual a L2')
else:
    print('L1 e diferente de L2')