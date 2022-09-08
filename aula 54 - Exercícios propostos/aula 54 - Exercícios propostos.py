"""
1-Crie uma função que exibe uma saudação com os parâmetros saudação e nome.

def funcao (saudacao, nome):
    print(saudacao, nome)
    return


n1 = input('digite um saudacao: ')
n2 = input('digite seu nome: ')

funcao(n1, n2)
"""


"""
2–Crie uma função que recebe 3 números como parâmetros e exiba a soma entre
eles.


def soma(n1, n2, n3):
    return n1 + n2 + n3


print(soma(12, 13, 14))
"""


"""
3-Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual(ex.10%).Retorne(return) o valor do primeiro número somado
do aumento do percentual do mesmo.


def por(n1, n2):
    n2 = n2 / 100
    return n1 + (n1*n2)


print(por(10, 5))
"""


"""
4-Fizz Buzz-Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5,retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3,retorne FizzBuzz,caso contrário, retorneo
número enviado.
"""


def fizzbuzz(parametro):
    if parametro % 5 == 0 and parametro % 3 == 0:
        return print('fizzbuzz')
    if parametro % 3 == 0:
        return print('fizz')
    if parametro % 5 == 0:
        return print('buzz')
    return print(parametro)


fizzbuzz(15)
