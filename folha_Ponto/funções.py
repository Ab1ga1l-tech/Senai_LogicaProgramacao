#nome , dia, horário ,  ano 
import sqlite3
import re

# Criação da tabela
def criar_tabela():
    con = sqlite3.connect("professores.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS professores (
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            area text NOT NULL,
            justificativa text 
                
        )
    """)
    con.commit()
    con.close()


# Validação simples de e-mail

# Inserção de aluno
def inserir_aluno( nome, data, area , justificativa):
    try:
        con = sqlite3.connect("professores.db")
        cur = con.cursor()
        cur.execute("INSERT INTO professores (nome, data,area, justificativa) VALUES (?, ?, ?, ?, ?)",
                    (nome, data , area ,justificativa))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        return False

# Consulta aluno por CPF
def consultar_aluno(nome):
    con = sqlite3.connect("professores.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM professores WHERE cpf = ?", (nome,))
    aluno = cur.fetchone()
    con.close()
    return aluno

# Listar todos os alunos
def listar_todos():
    con = sqlite3.connect("professores.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM professores")
    lista = cur.fetchall()
    con.close()
    return lista
