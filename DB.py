import sqlite3

# Cria (ou conecta) o banco de dados
conn = sqlite3.connect("controle_despesas.db")
cursor = conn.cursor()

# Cria a tabela de despesas (ou vendas)
cursor.execute("""
CREATE TABLE IF NOT EXISTS despesas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE,
    categoria TEXT,
    descricao TEXT,
    valor REAL
)
""")

# Salva as alterações
conn.commit()

# Fecha a conexão
conn.close()