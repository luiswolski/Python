from time import sleep
from threading import Thread


class MeuThread(Thread):
    def __init__(self, tempo, texto):
        self.texto = texto
        self.tempo = tempo
        super(MeuThread, self).__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread(5, 'Thread 1')
t1.start()

t2 = MeuThread(2, 'Thread 2')
t2.start()

t3 = MeuThread(3, 'Thread 3')
t3.start()

for i in range(20):
    print(i)
    sleep(1)
