import random

# Gera um número inteiro entre A e B
inteiro = random.randint(10, 20)
print(f'Numero inteiro: {inteiro}')

# Gera um número aleatório usando a função range()
aleatorio = random.randrange(900, 1000, 10)
print(f'Numero aleatório com range: {aleatorio}')

# Gera um número de ponto flutuante entre A e B
flutuante = random.uniform(10, 20)
print(f'Numero float: {flutuante}')

# Gera um número de ponto flutuante entre 0 e 1
flutuante2 = random.random()
print(f'Numero float entre 0 e 1: {flutuante2}')

# Pode ser usado um random em uma lista
lista = ['Luis', 'Felipe', 'Maria', 'Joao', 'Carlos', 'Andre', 'Guilherme', 'Eduardo']
sorteio = random.choice(lista)
# random.choices(lista, k=2) - Pega mais de um nome aleatoriamente, porem ele pode repetir o mesmo
# random.sample(lista, 2) - Pega mais de um nome aleatoriamente, porem ele não repete o mesmo
print(f'Sorteio de uma lista: {sorteio }')

# Embaaralha a lista
print(f'Lista original: {lista}')
random.shuffle(lista)
print(f'Embaralha a lista: {lista}')