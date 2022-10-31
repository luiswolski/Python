from threading import Thread
from time import sleep
from threading import Lock

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        #   caso não tenha esse lock todos os valores seriam aceitos, por não chegariam no decréscimo

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)    # simulando um atraso

        """
            AO SIMULAR UM ATRASO O PYTHON PASSA TODOS OS VALORES PELO if, SE FAZER O DECRÉSCIMO NA FUNÇÃO ABAIXO,
            ASSIM COMPROMETENDO A VARIÁVEL QUANTIDADE DO if. OU SEJA, A QUANTIDADE SERÁ SEMPRE A MESMA DURANTE ESSE
            UM SEGUNDO DE PAUSA.
        """

        self.estoque -= quantidade      # função de decréscimo
        print(f'Você comprou {quantidade} ingresso(s).'
              f'Ainda temos {self.estoque} em estoque.')

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    threads = []
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))     # faz com que um cliente comprando não bloqueie o outro
        threads.append(t)

# fazendo uma interrupção, o código só continua caso todas as threads tenham sido executadas

    for t in threads:
        t.start()

    executando = False
    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingressos.estoque)
