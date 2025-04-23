import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
from  datetime import datetime
import pytz 
from cadastro import*

def cadastrar():
    nome = nome_entry.get()
    data = data_entry.get()
    hour = hour_entry.get()
    area = area_entry.get()
    jus = jus_entry.get()


    if not  data or not nome or not area or not hour:
        messagebox.showwarning("Você não preencheu todos os itens do cadastro")
        return
    
    try:
        datetime.strptime(data, "%d/%m/%Y")
        
    except:
        messagebox.showerror("Erro", "Data deve estar no formato DD/MM/AAAA e Série deve ser número.")
        return
    sucesso = inserir_aluno( nome, data)
    if sucesso:
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        limpar_campos()
    else:
        messagebox.showerror("Erro", "CPF já cadastrado!")
    
#def consultar():
        

def limpar_campos():
    nome_entry.delete(0, tk.END)
    area_entry.set('')
    tipo_entry.set('')
    jus_entry.delete(0, tk.END)

    fuso_fortaleza = pytz.timezone('America/Fortaleza')
    agora = datetime.now(fuso_fortaleza)

    data_entry.delete(0, tk.END)
    data_entry.insert(0, agora.strftime('%d/%m/%Y'))

    hour_entry.delete(0, tk.END)
    hour_entry.insert(0, agora.strftime('%H:%M'))

    
#fazendo a interface
janela = tk.Tk()

def listar():
    alunos = listar_todos()
    texto = tk.Text(janela, width=70, height=20)
    texto.grid(row=7, column=0, columnspan=2, sticky="e", padx=5, pady=5)
    for a in alunos:
        texto.insert(tk.END, f"""CPF: {a[0]}, Nome: {a[1]}, Nasc: {a[2]}, Série: {a[3]}, Email: {a[4]}""")


#formulário
tk.Label(janela, text="Nome*").grid(row=1, column=0, sticky="e", padx=5, pady=5)
nome_entry = ttk.Combobox(janela, width=30)
nome_entry.grid(row=1, column=1)

tk.Label(janela, text="Data: (DD/MM/AAAA) *").grid(row=2, column=0, sticky="e", padx=5, pady=5)
data_entry = tk.Entry(janela, width=30)
data_entry.grid(row=2, column=1)

tk.Label(janela, text="Horário:  00:00  *").grid(row=3, column=0, sticky="e", padx=5, pady=5)
hour_entry = tk.Entry(janela, width=30)
hour_entry.grid(row=3, column=1) 

tk.Label(janela, text="Área *").grid(row=4, column=0, sticky="e", padx=5, pady=5)
area_entry = ttk.Combobox(janela, width=28)
area_entry['values'] = ["Matemática", "Português", "História", "Inglês", "Educação Física"]  # você pode alterar essa lista
area_entry.grid(row=4, column=1)

tk.Label(janela, text=" Tipo*").grid(row=5, column=0, sticky="e", padx=5, pady=5)
tipo_entry = ttk.Combobox(janela, width=28)
tipo_entry['values'] = ["entrada", "Saída"]  
tipo_entry.grid(row=5, column=1)

tk.Label(janela, text=" Justificativa ").grid(row=6, column=0, sticky="e", padx=5, pady=5)
jus_entry = tk.Entry(janela, width=30)
jus_entry.grid(row=6, column=1)

#botões
tk.Button(janela,text="cadastrar ", command=cadastrar,width=15).grid(row=7, column=0, pady=10)
tk.Button(janela,text=" consultar ",width=15).grid(row=7, column=2, pady=10)

criar_tabela()
limpar_campos()
janela.title(" professores - Folha de Pontos ")
janela.geometry("")
janela.mainloop()
