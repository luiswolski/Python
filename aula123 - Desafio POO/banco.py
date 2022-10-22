from conta import Conta
from cliente import Cliente


class Usuario:
    def __init__(self):
        self.agencias = [123, 132, 231]
        self.contas = []
        self.clientes = []

    def add_cliente(self, cliente):
        self.clientes.append(cliente)

    def add_conta(self, conta):
        self.contas.append(conta)

    def verifica(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False

        return True
