import sqlite3


conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

"""
cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# TRÊS FORMAS DIFERENTES DE INCREMENTAR NA BASE DE DADOS
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 60))
cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': 'Joao','peso': 58}
)
cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Daniel','peso': 92}
)
conexao.commit()
"""

cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id ',
               {'nome':'Joana', 'id':2}
)
conexao.commit()

# ASSIM POSSO EXCLUIR PERMANENTEMENTE DA BASE DE DADOS
# cursor.execute('DELETE FROM clientes WHERE id=:id ',
#                {'id':2}
# )


cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)


cursor.close()
conexao.close()