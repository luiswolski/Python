""""
    VALIDAÇÃO DE CPF
"""
import re
import string


def valida_cpf(cpf):
    cpf = str(cpf)

    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    digitos = []
    cont1 = 0
    cont2 = 0
    new_cpf = ""


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

    # Criando o new cpf
    for i in range(len(cpf_pontuation)):
        if i != 9 and i != 10:
            new_cpf = new_cpf + cpf_pontuation[i]


    # Adicionando os digitos verificadores
    new_cpf = new_cpf + str(val_dg1) + str(val_dg2)
    if new_cpf == cpf:
        return True
    else:
        return False