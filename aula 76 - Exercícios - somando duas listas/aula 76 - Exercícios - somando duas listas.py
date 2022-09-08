"""
Considerando duas listas de inteiros ou floats(lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados;
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor
Exemplo:
lista_a  =[1,2,3,4,5,6,7]
lista_b =[1,2,3,4]
   ===== resultado
lista_soma   =[2,4,6,8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [9, 10, 11, 12]

lista_soma = zip(lista_a, lista_b)

soma_total = []
for valor1, valor2 in lista_soma:
    soma = float(valor1) + float(valor2)
    soma_total.append(soma)
print(soma_total)
