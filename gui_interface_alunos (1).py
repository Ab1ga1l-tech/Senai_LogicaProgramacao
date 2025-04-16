import tkinter as tk
from tkinter import messagebox
from funcoes_alunos_1 import criar_tabela, inserir_aluno, consultar_aluno, listar_todos, validar_cpf, validar_email
from datetime import datetime

# Função principal para cadastrar aluno com validações
def cadastrar():
    cpf = cpf_entry.get()
    nome = nome_entry.get()
    data_nasc = nasc_entry.get()
    serie = serie_entry.get()
    email = email_entry.get()

    if not cpf or not nome or not data_nasc or not serie:
        messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")
        return

    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "CPF inválido! Deve conter 11 dígitos numéricos.")
        return

    if email and not validar_email(email):
        messagebox.showerror("Erro", "E-mail inválido!")
        return

    try:
        datetime.strptime(data_nasc, "%d/%m/%Y")
        serie_int = int(serie)
    except:
        messagebox.showerror("Erro", "Data deve estar no formato DD/MM/AAAA e Série deve ser número.")
        return

    sucesso = inserir_aluno(cpf, nome, data_nasc, serie_int, email)
    if sucesso:
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        limpar_campos()
    else:
        messagebox.showerror("Erro", "CPF já cadastrado!")

def consultar():
    cpf = cpf_entry.get()
    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "Digite um CPF válido para consultar.")
        return
    aluno = consultar_aluno(cpf)
    if aluno:
        nome_entry.delete(0, tk.END)
        nome_entry.insert(0, aluno[1])
        nasc_entry.delete(0, tk.END)
        nasc_entry.insert(0, aluno[2])
        serie_entry.delete(0, tk.END)
        serie_entry.insert(0, aluno[3])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, aluno[4])
    else:
        messagebox.showinfo("Consulta", "Aluno não encontrado.")

def listar():
    alunos = listar_todos()
    janela_lista = tk.Toplevel(janela)
    janela_lista.title("Lista de Alunos")
    texto = tk.Text(janela_lista, width=70, height=20)
    texto.pack()
    for a in alunos:
        texto.insert(tk.END, f"""CPF: {a[0]}, Nome: {a[1]}, Nasc: {a[2]}, Série: {a[3]}, Email: {a[4]}
""")

# Função para limpar os campos
def limpar_campos():
    cpf_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    nasc_entry.delete(0, tk.END)
    serie_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Interface
janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("520x350")

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

# Botões com espaçamento
tk.Button(janela, text="Cadastrar", command=cadastrar, width=15).grid(row=5, column=0, pady=10)
tk.Button(janela, text="Consultar", command=consultar, width=15).grid(row=5, column=1)
tk.Button(janela, text="Listar Todos", command=listar, width=15).grid(row=6, column=0, columnspan=2, pady=5)

criar_tabela()
janela.mainloop()
