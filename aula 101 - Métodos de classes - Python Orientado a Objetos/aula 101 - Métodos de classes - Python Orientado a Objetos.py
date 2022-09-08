from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# metodos de instancia (uso para cada objeto)
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

# metodos de classe (especifico geral, altera em nivel de classe)
# ele precisa da classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

# não precisa da classe
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa('Luis', 22)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(p1.gera_id())