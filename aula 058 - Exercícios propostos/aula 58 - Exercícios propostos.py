"""
1-Crie uma função1 que recebe uma função 2 como parâmetro e retorne o valor da
função 2 executada.


def funcao_secundaria():
    return 'ola mundo'


def funcao(funcao):
    return funcao()


exect = funcao(funcao_secundaria)
print(exect)
"""

"""
2-Crie uma função 1 que recebe uma função 2 como parâmetro e retorne o valor da
função 2 executada. Faça a função 1 executar duas funções que recebam um número
diferente de argumentos.
"""


def dados1(nome):
    return f'O {nome}'


def dados2(altura, idade):
    return f'tem {altura}cm de altura e {idade} anos de idade.'


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


imprimindo = mestre(dados1, 'luis')
imprimindo2 = mestre(dados2, 172, 22)
print(imprimindo, imprimindo2)
