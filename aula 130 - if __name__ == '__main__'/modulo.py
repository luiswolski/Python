"""
print(__name__) caso eu execute o arquivo modulo este comando
me retornara '__main__', porem caso eu execute o arquivo app
o comando me retornara 'modulo'. O python considera o main
como o arquivo que esta sendo executado
"""


def soma(x: float, y: float) -> float:
    return x + y


if __name__ == '__main__':
    print(soma(10, 5))
    print(soma(10, 20))
    print(soma(10, 10))
