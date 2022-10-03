from cp import ContaPoupanca
from cc import ContaCorrente


cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(5)

print('-----------------------------------')
cc = ContaCorrente(agencia=111, conta=333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(500)
cc.sacar(500)
cc.depositar(100)
cc.depositar(1000)
