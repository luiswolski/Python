"""
def funcao(n1, n2):
    return n1 * n2


print(funcao(2, 2))

************ ESSAS DUAS COISAS SÃO A MESMA COISA *************

a = lambda x, y: x * y

print(a(2, 2))

"""

lista = [
    ['P1', 144],
    ['P2', 14],
    ['P3', 17],
    ['P4', 1],
    ['P5', 42],
    ['P6', 21]
]

print(sorted(lista, key=lambda i: i[1], reverse=True))
