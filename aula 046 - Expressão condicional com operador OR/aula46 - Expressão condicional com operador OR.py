"""
nome = input('Qual o seu nome?')
if nome:
   print(nome)
else:
     print('Você não digitou nada')

     A FUNÇÃO OR TRABALHA DE FORMA BOLEANA, É POSSIVEL ADICIONAR QUANTOS ELEMENTOS
     VOCÊ NECESSITAR, POREM ELA PARA NO PRIMEIRO TRUE
"""

nome = input('Qual o seu nome?')
print(nome or 'Você não digitou o seu nome!')