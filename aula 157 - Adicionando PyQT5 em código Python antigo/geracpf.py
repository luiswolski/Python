""""
    VALIDAÇÃO DE CPF
"""
import string
from random import randint

def gera_cpf():
    digitos = []
    cont1 = 0
    cont2 = 0
    new_cpf = ""

    # gerando um cpf aleatorio
    cpf = str(randint(100000000, 999999999))

    # retirando pontuação do cpf
    cpf_pontuation = ''.join([i for i in cpf if i not in string.punctuation])

    # utilizando somente digitos
    for caractere in cpf_pontuation:
        if caractere.isdigit():
            digitos.append(caractere)

    # convertendo string em int
    int_list = list(map(int, digitos))

    # multiplicando e contando primeiro digito
    for p, r in enumerate(range(10, 1, -1)):
        mult1 = r * int_list[p]
        cont1 += mult1

    # validação primeiro digito
    val_dg1 = (11 - (cont1 % 11))
    if val_dg1 <= 9:
        pass
    else:
        val_dg1 = 0

    # multiplicando e contando segundo digito
    for x, y in enumerate(range(11, 1, -1)):
        int_list.append(val_dg1)
        mult2 = y * int_list[x]
        cont2 += mult2

    # validação segundo digito
    val_dg2 = (11 - (cont2 % 11))
    if val_dg2 <= 9:
        pass
    else:
        val_dg2 = 0

    novo_cpf = cpf + str(val_dg1) + str(val_dg2)
    return novo_cpf
