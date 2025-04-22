#nome , dia, horário ,  ano 
import sqlite3
import re

# Criação da tabela
def criar_tabela():
    con = sqlite3.connect("professores.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS professores (
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            area text NOT NULL,
                
        )
    """)
    con.commit()
    con.close()

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Validação simples de e-mail

# Inserção de aluno
def inserir_aluno(cpf, nome, data, area):
    try:
        con = sqlite3.connect("professores.db")
        cur = con.cursor()
        cur.execute("INSERT INTO professores (cpf, nome, data_nasc, serie, email) VALUES (?, ?, ?, ?, ?)",
                    (cpf, nome, data_nasc, serie, email))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        return False

# Consulta aluno por CPF
def consultar_aluno(cpf):
    con = sqlite3.connect("professores.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos WHERE cpf = ?", (cpf,))
    aluno = cur.fetchone()
    con.close()
    return aluno

# Listar todos os alunos
def listar_todos():
    con = sqlite3.connect("professores.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos")
    lista = cur.fetchall()
    con.close()
    return lista
