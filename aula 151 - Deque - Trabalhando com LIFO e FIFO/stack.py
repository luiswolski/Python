"""
Pilhas e filas
Pilha (stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre O outro
 Fila (queue) - FIFO - first in, first out. (Pior desempenho)
     Exemplo: Uma fila de banco (ou qualquer fila da vida real)
 Filas podem ter efeitos colaterais em desempenho, porque a cada item
 alterado, todos OS índices serão modificados.
"""

#   EXEMPLO DE STACK
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')
print(livros)
livro_removido = livros.pop()
print(f'O {livro_removido} foi removido!')

print('**********************************')

# AGORA COMO FUNCIONA FILAS
# COLLECTIONS É SOBRE ESTRUTURA DE DADOS DE ALTO DESEMPENHO
from collections import deque
fila = deque(maxlen=5)
fila.append('Pessoa 1')
fila.append('Pessoa 2')
fila.append('Pessoa 3')
fila.append('Pessoa 4')
fila.append('Pessoa 5')
fila.append('Pessoa 6')
print(fila)
fila.rotate(2)
print(fila)
