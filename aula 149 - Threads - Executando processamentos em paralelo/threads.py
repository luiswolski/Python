from time import sleep
from threading import Thread


"""
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
    
"""


# OUTRA FORMA DE FAZER THREADS
"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo! 2', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 3))
t3.start()

for i in range(20):
    print(i)
    sleep(1)
"""


# DESENCADEAMENTO DE AÇÕES EM FUNÇÃO DA THREAD EXECUTADA
"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t1.start()
# se eu utilizar  t1.join() ela ira se juntar a thread principal, sendo assim um blocking

# espera a thread finalizar para executar a ação
while t1.is_alive():
    print('Esperando a thread.')
    sleep(1)

# apos executar a ação volta para o main
print('Thread acabou!')
"""
