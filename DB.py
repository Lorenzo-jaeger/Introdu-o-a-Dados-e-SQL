import sqlite3


def cria_db():
    # Cria (ou conecta) o banco de dados
    conn = sqlite3.connect("control.db")
    cursor = conn.cursor()

    # Cria a tabela de despesas (ou vendas)
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS despesas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE,
        categoria TEXT,
        descricao TEXT,
        valor REAL
    )
    """
    )

    # Salva as alterações
    conn.commit()


if __name__ == "__main__":
    cria_db()
    print("Banco e tabela criados.")
