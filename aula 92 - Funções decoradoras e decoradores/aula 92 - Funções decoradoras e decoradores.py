from time import time
from time import sleep

def velocidade(funcao):
    def slave(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        all_time = (end_time - start_time) * 1000
        print(f'A funcao {funcao.__name__} levou {all_time:.2f}ms para executar.')
        return resultado
    return slave

@velocidade
def loss_time():
    for i in range(5):
        print(i)
        sleep(1)

loss_time()