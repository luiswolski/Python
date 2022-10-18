
"""
 Toda vez que um arquivo é aberto ele deve ser fechado
 
 arquivo = open('abc.txt', 'test')
 arquivo.write('Alguma coisa')
 arquivo.close()
 
 Voce pode fazer isso desta maneira
"""


class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo')
        self.arquivo.close()


with Arquivo('abc.txt', 'test') as arquivo:
    arquivo.write('Alguma coisa')
