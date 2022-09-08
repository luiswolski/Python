try:
    a = {}
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor')
except (IndexError, KeyError) as erro:
    print('Erro de indice')
except Exception as erro: # esse é o mais geral possivel
    print('Ocorreu um erro')
else: # roda caso não tenha nenhum erro
    print('Seu codigo foi executado com sucesso')
finally: #sempre vai rodar, pode ser usado para fechar algum diretorio
    print('Finalmente')