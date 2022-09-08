# FAZENDO ITERAÇÃO DE STRING

fazendo = 'testando para ver se essa merda funciona'
tamanho_string = len(fazendo)
contador = 0
new_string = ''

while contador < tamanho_string:
    print(fazendo[contador], contador)
    new_string += fazendo[contador]
    contador += 1