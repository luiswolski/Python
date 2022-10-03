nome = 'Luis'
idade = 22
altura = 1.76
peso = 86
imc = peso / (altura**2)

print(nome, 'tem', idade, 'anos de idade e seu IMC é:', imc)

#Pode ser utilizado o f strings, para facilitar a leitura do codigo

print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')

#Pode ser formatado desta outra forma tambem

print('{} tem {} anos de idade e seu IMC é:{:.2f}'.format(nome, idade, imc))

print('"aaaa"')