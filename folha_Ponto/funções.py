#nome , dia, horário ,  ano 
import sqlite3
import re

# Criação da tabela
def criar_tabela():
    con = sqlite3.connect("alunos.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            data_nasc TEXT NOT NULL,
            serie INTEGER NOT NULL,
            email TEXT
        )
    """)
    con.commit()
    con.close()
