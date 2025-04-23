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
    except sqlite3.IntegrityError:
        return False
    except Exception as e:
        print("Erro ao inserir:", e)  # Ajuda no debug
        return False

def consultar_aluno(nome):
    con = sqlite3.connect("professores.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM professores WHERE nome = ?", (nome,))
    aluno = cur.fetchone()
    con.close()
    return aluno

def listar_todos():
    con = sqlite3.connect("professores.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM professores")
    lista = cur.fetchall()
    con.close()
    return lista
