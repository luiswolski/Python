import re


def remover_caracteres(cnpj1):
    return re.sub(r'\D', '', cnpj1)


def verifica1(cnpj_origina):
    l1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cpf_list = list(cnpj_origina)
    multiplicacao = [x * int(y) for x, y in zip(l1, cpf_list)]
    aux = 11 - (sum(multiplicacao) % 11)

    if aux > 9:
        dig_vers1 = 0
    else:
        dig_vers1 = aux

    return dig_vers1


def verifica2(cnpj_origin, dig_ver):
    l1 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cpf_list = list(cnpj_origin)
    cpf_list[12] = dig_ver
    multiplicacao = [x * int(y) for x, y in zip(l1, cpf_list)]
    aux = 11 - (sum(multiplicacao) % 11)

    if aux > 9:
        dig_vers2 = 0
    else:
        dig_vers2 = aux

    return dig_vers2


while True:
    cnpj = input('Digite seu CNPJ: ')
    cnpj_original = list(remover_caracteres(cnpj))
    aux = cnpj_original
    cpf = tuple(aux)

    dig_ver1 = verifica1(cnpj_original)
    dig_ver2 = verifica2(cnpj_original, dig_ver1)

    new_cnpj = cnpj_original
    new_cnpj[12] = str(dig_ver1)
    new_cnpj[13] = str(dig_ver2)

    cnpj_digitado = list(cpf)

    if cnpj_digitado == new_cnpj:
        print('Este CNPJ é VERDADEIRO!')
    else:
        print('Este CNPJ é FALSO!')
