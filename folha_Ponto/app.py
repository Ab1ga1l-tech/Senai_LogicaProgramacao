import tkinter as tk 
from  datetime import datetime
from tkinter import messagebox
from  funçoes import*

def cadastrar():
    cpf = cpf_entry.get()
    nome = nome_entry.get()
    nascimento = nasc_entry.get()
    serie = serie_entry.get()
    if not cpf or not nascimento or not nome:
        messagebox.showwarning("Você não preencheu todos os itens do cadastro")
        return
    if not validar_cpf(cpf):
        messagebox.showerror("O cpf está inválido ")
        return
    
    try:
        datetime.strptime(nascimento, "%d/%m/%Y")
        serie_int = int(serie)
    except:
        messagebox.showerror("Erro", "Data deve estar no formato DD/MM/AAAA e Série deve ser número.")
        return
    sucesso = inserir_aluno(cpf, nome, nascimento, serie_int)
    if sucesso:
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        limpar_campos()
    else:
        messagebox.showerror("Erro", "CPF já cadastrado!")
    
def consultar():
        cpf = cpf_entry.get()
        if not validar_cpf:
            messagebox.showerror("O cpf está inválido ")
            return
        aluno = consultar_aluno(cpf)
        if aluno:
            nome_entry.delete(0, tk.END)
            nome_entry.insert(0, aluno[2])
            nasc_entry.delete(0, tk.END)
            nasc_entry.insert(0, aluno[3])
            serie_entry.delete(0, tk.END)
            serie_entry.insert(0, aluno[4])
            
        else:
           messagebox.showinfo("Consulta", "Aluno não encontrado.")

def limpar_campos():
    cpf_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    nasc_entry.delete(0, tk.END)
    serie_entry.delete(0, tk.END)
#fazendo a interface
janela = tk.Tk()

def listar():
    alunos = listar_todos()
    texto = tk.Text(janela, width=70, height=20)
    texto.grid(row=7, column=0,columnspan=2, sticky="e", padx=5, pady=5)
    for a in alunos:
        texto.insert(tk.END, f"""CPF: {a[0]}, Nome: {a[1]}, Nasc: {a[2]}, Série: {a[3]}, Email: {a[4]}""")



#campos
tk.Label(janela, text="CPF*").grid(row=0, column=0, sticky="e", padx=5, pady=5)
cpf_entry = tk.Entry(janela, width=30)
cpf_entry.grid(row=0, column=1)

tk.Label(janela, text="Nome*").grid(row=1, column=0, sticky="e", padx=5, pady=5)
nome_entry = tk.Entry(janela, width=30)
nome_entry.grid(row=1, column=1)

tk.Label(janela, text="Data: (DD/MM/AAAA) *").grid(row=2, column=0, sticky="e", padx=5, pady=5)
nasc_entry = tk.Entry(janela, width=30)
nasc_entry.grid(row=2, column=1)

tk.Label(janela, text=" Área *").grid(row=3, column=0, sticky="e", padx=5, pady=5)
serie_entry = tk.Entry(janela, width=30)
serie_entry.grid(row=3, column=1)


#botões
tk.Button(janela,text="cadastrar",  width=15).grid(row=5, column=0, pady=10)
tk.Button(janela,text="consultar",width=15).grid(row=5, column=1, pady=10)
tk.Button(janela,text="Listar ",width=15).grid(row=5, column=2, pady=10)

criar_tabela()
janela.title("alunos")
janela.geometry("")
janela.mainloop()
