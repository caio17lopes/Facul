import sqlite3

con = sqlite3.connect('oficina.db')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS cadastro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    proprietario TEXT,
    veiculo TEXT,
    fabricante TEXT,
    ano_veiculo TEXT,
    placa TEXT,
    servico TEXT,
    valor_pecas REAL,
    valor_servico REAL,
    valor_total REAL,
    data_servico TEXT,
    observacao TEXT
);


''')
con.commit()
con.close()