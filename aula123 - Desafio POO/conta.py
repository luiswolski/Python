from abc import abstractmethod


class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def depositar(self, valor):
        self.saldo += valor
        self.detalhe()

    @abstractmethod
    def sacar(self, valor):
        pass

    def detalhe(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente!')
            return

        self.saldo -= valor
        self.detalhe()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=500):
        super(ContaCorrente, self).__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente!')
            return

        self.saldo -= valor
        self.detalhe()
