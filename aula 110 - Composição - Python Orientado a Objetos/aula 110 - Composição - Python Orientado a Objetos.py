from classes import Cliente, Endereco

cliente1 = Cliente('Luis', 22)
cliente1.insere_endereco('Curitiba', 'PR')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Joao', 42)
cliente3.insere_endereco('Sao Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('**************************************************')