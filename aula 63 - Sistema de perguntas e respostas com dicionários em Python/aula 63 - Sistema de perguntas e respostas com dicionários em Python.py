perguntas = {
    'Pergunta1': {
        'pergunta': 'Quanto e 2+2? ',
        'resposta': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b'
    },
    'Pergunta2': {
        'pergunta': 'Quanto e 5*5? ',
        'resposta': {
            'a': '5',
            'b': '10',
            'c': '25',
        },
        'resposta_certa': 'c'
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['resposta'].items():
        print(f'{rk}: {rv}')

    resposta_usuario = input('\nSua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Voce ACERTOU')
        respostas_certas += 1
    else:
        print('Voce ERROU!')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} respostas')
print(f'Sua  porcentagem de acerto foi {porcentagem_acerto}%')
