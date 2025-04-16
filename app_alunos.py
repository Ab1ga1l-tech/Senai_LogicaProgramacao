import tkinter as tk 
from  datetime import datetime
from tkinter import messagebox
from  funções import*

def cadastrar():
    cpf = cpf_entry.get()
    email = email_entry.get()
    nome = nome_entry.get()
    nascimento = nasc_entry.get()
    
    
#fazendo a interface
janela = tk.Tk()

#campos
tk.Label(janela, text="CPF*").grid(row=0, column=0, sticky="e", padx=5, pady=5)
cpf_entry = tk.Entry(janela, width=30)
cpf_entry.grid(row=0, column=1)

tk.Label(janela, text="Nome*").grid(row=1, column=0, sticky="e", padx=5, pady=5)
nome_entry = tk.Entry(janela, width=30)
nome_entry.grid(row=1, column=1)

tk.Label(janela, text="Dt_Nasc.* (DD/MM/AAAA)").grid(row=2, column=0, sticky="e", padx=5, pady=5)
nasc_entry = tk.Entry(janela, width=30)
nasc_entry.grid(row=2, column=1)

tk.Label(janela, text="Série*").grid(row=3, column=0, sticky="e", padx=5, pady=5)
serie_entry = tk.Entry(janela, width=30)
serie_entry.grid(row=3, column=1)

tk.Label(janela, text="E-mail").grid(row=4, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(janela, width=30)
email_entry.grid(row=4, column=1)


#botões
tk.Button(janela,text="cadastrar",  width=15).grid(row=5, column=0, pady=10)
tk.Button(janela,text="consultar",width=15).grid(row=5, column=1, pady=10)
tk.Button(janela,text="Listar ",width=15).grid(row=5, column=2, pady=10)

criar_tabela()
janela.title("alunos")
janela.geometry("520x350")
janela.mainloop()
