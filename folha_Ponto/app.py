import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import pytz
from cadastro import *

def cadastrar():
    nome = nome_entry.get()
    data = data_entry.get()
    hora = hour_entry.get()
    area = area_entry.get()
    tipo = tipo_entry.get()
    jus = jus_entry.get()

    if not nome or not data or not hora or not area or not tipo:
        messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios (*)")
        return

    try:
        datetime.strptime(data, "%d/%m/%Y")
    except:
        messagebox.showerror("Erro", "Data deve estar no formato DD/MM/AAAA.")
        return

    sucesso = inserir_aluno(nome, data, hora, area, tipo, jus)
    if sucesso:
        messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso!")
        limpar_campos()
        listar()
    else:
        messagebox.showerror("Erro", "Erro ao cadastrar professor.")

def consultar():
    nome = nome_entry.get()
    data = data_entry.get()
    resultados = consultar_por_filtro(nome, data)
    atualizar_texto(resultados)

def atualizar_texto(resultados):
    texto.delete("1.0", tk.END)
    if resultados:
        for p in resultados:
            texto.insert(tk.END, f"Nome: {p[0]}\nData: {p[1]} | Hora: {p[2]}\nÁrea: {p[3]} | Tipo: {p[4]}\nJustificativa: {p[5]}\n{'-'*60}\n")
    else:
        texto.insert(tk.END, "Nenhum resultado encontrado.")

def limpar_campos():
    nome_entry.set('')
    area_entry.set('')
    tipo_entry.set('')
    jus_entry.delete(0, tk.END)

    fuso_fortaleza = pytz.timezone('America/Fortaleza')
    agora = datetime.now(fuso_fortaleza)

    data_entry.delete(0, tk.END)
    data_entry.insert(0, agora.strftime('%d/%m/%Y'))

    hour_entry.delete(0, tk.END)
    hour_entry.insert(0, agora.strftime('%H:%M'))

def listar():
    professores = listar_todos()
    atualizar_texto(professores)

# Interface
janela = tk.Tk()
janela.title("Folha de Ponto - Escola")
janela.configure(bg="#f0f4f7")

frame = tk.Frame(janela, bg="#f0f4f7", padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Nome*", bg="#f0f4f7").grid(row=0, column=0, sticky="w")
nome_entry = ttk.Combobox(frame, width=30)
nome_entry['values'] = ["Lucia Helena Souza Santos", "Verônica Lopes do Santos","Sandra Maria Coelho de Oliveira","José Sérgio Pereira da Costa"]
nome_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Data* (DD/MM/AAAA)", bg="#f0f4f7").grid(row=1, column=0, sticky="w")
data_entry = tk.Entry(frame, width=32)
data_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Horário* (00:00)", bg="#f0f4f7").grid(row=2, column=0, sticky="w")
hour_entry = tk.Entry(frame, width=32)
hour_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Área*", bg="#f0f4f7").grid(row=3, column=0, sticky="w")
area_entry = ttk.Combobox(frame, width=30)
area_entry['values'] = ["Matemática", "Português", "História", "Inglês", "Educação Física", "Artes", "Física", "Química", "Biologia", "Sociologia", "Filosofia", "Geografia", "Funcionários", "SASP", "Multimeios", "Laboratório de Informática"]
area_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="Tipo* (Entrada/Saída)", bg="#f0f4f7").grid(row=4, column=0, sticky="w")
tipo_entry = ttk.Combobox(frame, width=30)
tipo_entry['values'] = ["Entrada", "Saída"]
tipo_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame, text="Justificativa", bg="#f0f4f7").grid(row=5, column=0, sticky="w")
jus_entry = tk.Entry(frame, width=32)
jus_entry.grid(row=5, column=1, padx=5, pady=5)

# Botões
botoes = tk.Frame(janela, bg="#f0f4f7")
botoes.pack(pady=10)

tk.Button(botoes, text="Cadastrar", command=cadastrar, bg="#007acc", fg="white", width=15).grid(row=0, column=0, padx=5)
tk.Button(botoes, text="Consultar", command=consultar, bg="#28a745", fg="white", width=15).grid(row=0, column=1, padx=5)
tk.Button(botoes, text="Limpar", command=limpar_campos, bg="#ffc107", width=15).grid(row=0, column=2, padx=5)

# Área de resultados
texto = tk.Text(janela, width=100, height=15, wrap="word")
texto.pack(padx=20, pady=10)
scroll = tk.Scrollbar(janela, command=texto.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
texto.config(yscrollcommand=scroll.set)

criar_tabela()
limpar_campos()
janela.mainloop()
