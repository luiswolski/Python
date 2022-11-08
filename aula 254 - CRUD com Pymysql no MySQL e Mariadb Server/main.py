import pymysql.cursors
from contextlib import contextmanager

# CRUD - CREATE, READ, UPDATE, DELETE

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()

# ADICIONA UM DADO NO DB
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
              '(%s, %s, %s, %s)'
        cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
        conexao.commit()
"""

# ADICIONAR MÚLTIPLUS DADOS NO DB
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
              '(%s, %s, %s, %s)'

        dados = [
            ('MURIEL', 'FIGUEIREDO', 18, 55),
            ('ROSE', 'FIGUEIREDO', 18, 55),
            ('JOSE', 'FIGUEIREDO', 18, 55),
        ]

        cursor.executemany(sql, dados)
        conexao.commit()
"""

# APAGAR UM DADO NO DB
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id = %s'
        cursor.execute(sql, (6,))
        conexao.commit()
"""

# APAGAR MULTIPLOS DADOS NO DB
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
        cursor.execute(sql, (7, 8, 9))
        conexao.commit()
"""

# APAGAR UMA SEQUENCIA DE DADOS NO DB
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
        cursor.execute(sql, (10, 12))
        conexao.commit()
"""

# SELECIONA OS DADOS NA DB
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
