"""
d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1.copy()
print(type(d1))
print(type(v))

AO FAZER ISSO VS NAO ESTA COPIANDO, OS DOIS REFERENCIAM O MESMO ENDERECO DE MEMORIA
"""
clientes = {
    'cliente1': {
        'nome': 'Luis',
        'sobrenome': 'Wolski',
    },
    'cliente2': {
        'nome': 'Felipe',
        'sobrenome': 'Correa',
    },
    'cliente3': {
        'nome': 'Amanda',
        'sobrenome': 'Wolski',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
