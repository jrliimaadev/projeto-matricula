import sqlite3

conn = sqlite3.connect('banco_dados.db')
cursor = conn.cursor()

# Criação da tabela de usuários (login)
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL
)
''')

# Criação da tabela de matrículas com 17 colunas
cursor.execute('''
CREATE TABLE IF NOT EXISTS matriculas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo TEXT,
    endereco TEXT,
    cep TEXT,
    cpf TEXT,
    rg TEXT,
    data_nascimento TEXT,
    cidade_nascimento TEXT,
    estado_nascimento TEXT,
    tipo_certificado TEXT,
    plano_eja TEXT,
    consultor TEXT,
    numero_matricula TEXT,
    documento_frente TEXT,
    documento_verso TEXT,
    data_matricula TEXT,
    status_pagamento TEXT
)
''')

# Inserção dos usuários padrão
cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", ('thalita', '123456'))
cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", ('maria', '123456'))
cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", ('danny', '123456'))

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
