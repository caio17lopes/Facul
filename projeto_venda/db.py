import sqlite3

def conectar():
    conn = sqlite3.connect('sistema.db')
    cursor = conn.cursor()

    # Corrigido nome da tabela e adicionado vírgulas corretamente
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    """)

    # Criando usuário admin padrão
    cursor.execute("SELECT * FROM usuarios WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (username, senha) VALUES ('admin', '12345')")

    conn.commit()  # corrigido: adicionado os parênteses
    return conn

    