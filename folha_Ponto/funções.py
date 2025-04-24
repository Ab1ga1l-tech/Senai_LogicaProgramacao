import sqlite3

def criar_tabela():
    con = sqlite3.connect("professores.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS professores (
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            area TEXT NOT NULL,
            tipo TEXT NOT NULL,
            justificativa TEXT 
        )
    """)
    con.commit()
    con.close()

def inserir_aluno(nome, data, hora, area, tipo, justificativa):
    try:
        con = sqlite3.connect("professores.db")
        cur = con.cursor()
        cur.execute("""
            INSERT INTO professores (nome, data, hora, area, tipo, justificativa)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, data, hora, area, tipo, justificativa))
        con.commit()
        con.close()
        return True
    except Exception as e:
        print("Erro ao inserir:", e)  # Vai exibir o erro no terminal
        return False

def consultar_por_filtro(nome, data):
    con = sqlite3.connect("professores.db")
    cur = con.cursor()

    query = "SELECT * FROM professores WHERE 1=1"
    parametros = []

    if nome:
        query += " AND nome LIKE ?"
        parametros.append(f"%{nome}%")
    if data:
        query += " AND data = ?"
        parametros.append(data)

    cur.execute(query, parametros)
    resultado = cur.fetchall()
    con.close()
    return resultado


def listar_todos():
    con = sqlite3.connect("professores.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM professores")
    lista = cur.fetchall()
    con.close()
    return lista
