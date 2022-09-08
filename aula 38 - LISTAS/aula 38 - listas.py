"""
FUNÇOES DESTRO DE LISTAS

append - insere elementos ou até outras listas ao final da lista desejada (l2.append('b')
insert - você insere porem pode escolher a posição (l2.insert(0, 'qulaquer coisa'))
pop - deleta o último elemento da lista (l2.pop())
del - deleta elementos desejados (del(l2[0]))
clear -
estend - adiciona uma lista a outra, tal qual o +
+ - junta duas lista
min - menor valor da lista (print (min(l2))
max - maior valor da lista (print (max(l2))
range - pode se usar ela para fazer uma lista automaticamente desse odo: (l2 = list(range(0,100)) <- assim [e criada uma lista l2 de 0 ate 100

"""

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não é valido! Digite apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'EEBBBAAAA, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'QUE PENA, a letra "{letra}" não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'PARABENS VOCE GANHOU, A PALAVRA ERA {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1