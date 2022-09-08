variavel = 'valor'


def func():
    print(variavel)


def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
outra_variavel = func2(arg=variavel)

print(outra_variavel)
