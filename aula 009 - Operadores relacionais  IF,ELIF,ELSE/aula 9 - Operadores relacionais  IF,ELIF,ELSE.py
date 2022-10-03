nome = input('Qual é o seu nome? ')
idade = int(input('Qual a sua idade? '))

#setando idades permitidas para pegar o emprestimo

if idade>=20 and idade<=30:
    print(f'{nome} seu emprestimo foi liberado')
else:
    print(f'{nome} seu emprestimo foi negado')
