"""
Operador ternário em Python
"""


logged_user1 = True

if logged_user1:
    msg = 'Usuario Logado!'
else:
    msg = 'Usuário precisa logar!'

print(msg)
print("\n************************\n")
print('I operador ternário I')
print('V                   V\n')

logged_user2 = False

msg2 = 'Usuario Logado!' if logged_user2 else 'Usuário precisa logar!'
print(msg2)