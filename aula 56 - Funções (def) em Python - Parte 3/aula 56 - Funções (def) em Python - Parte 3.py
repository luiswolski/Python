"""
Funcao def - *args **kwargs
"""


def funca(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('idade nao existe')

    nome = kwargs.get('nome')

    sobrenome = kwargs.get('sobrenome')
    print(nome, sobrenome)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
funca(*lista, *lista2, nome='Luis', sobrenome='Wolski', idade=30)
