num = input('Digite um numero inteiro: ')

if num.isdigit():
    num = int(num)
    resto = num%2
    if num==0 or resto==0:
        print('O numero é par')
    else:
        print('O numero é impar')
else:
    print("O valor digitado não é um numero inteiro")