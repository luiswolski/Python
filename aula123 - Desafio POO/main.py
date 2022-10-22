from banco import Usuario
from cliente import Cliente
from conta import ContaPoupanca, ContaCorrente

banco = Usuario()

cliente1 = Cliente('Luis', 22)
cliente2 = Cliente('Maria', 21)
cliente3 = Cliente('Carlos', 32)

conta1 = ContaPoupanca(123, 111110, 0)
conta2 = ContaCorrente(231, 111112, 0)
conta3 = ContaPoupanca(111, 111114, 0)

cliente1.add_conta(conta1)
cliente2.add_conta(conta2)
cliente3.add_conta(conta3)

cliente1.conta.depositar(20)

banco.add_cliente(cliente1)
banco.add_cliente(cliente2)
banco.add_cliente(cliente3)

banco.add_conta(conta1)
banco.add_conta(conta2)
banco.add_conta(conta3)


if banco.verifica(cliente1):
    cliente1.conta.depositar(20)
    cliente1.conta.sacar(40)
else:
    print('Cliente invalido')

print('------------------------------------------')

if banco.verifica(cliente2):
    cliente2.conta.depositar(20)
    cliente2.conta.sacar(40)
else:
    print('Cliente invalido')

print('------------------------------------------')

if banco.verifica(cliente3):
    cliente3.conta.depositar(20)
    cliente3.conta.sacar(40)
else:
    print('Cliente invalido')

print('------------------------------------------')