import sqlite3

# Conecta (ou cria) o banco de dados
conn = sqlite3.connect("alunos.db")
cursor = conn.cursor()

# Cria a tabela se ainda não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    cpf TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    idade INTEGER NOT NULL,
    serie INTEGER NOT NULL,
    nota FLOAT NOT NULL
)
""")
conn.commit()

# Função para cadastrar aluno
def cadastrar_aluno():
    cpf = input("CPF (somente números): ").strip()
    cursor.execute("SELECT cpf FROM alunos WHERE cpf = ?", (cpf,))
    if cursor.fetchone():
        print("CPF já cadastrado.")
        return

    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    idade = int(input("Idade: "))
    serie = int(input("Série: "))
    nota = int(input("Digite sua nota: "))

    cursor.execute("INSERT INTO alunos (cpf, nome, email, idade, serie, nota) VALUES (?, ?, ?, ?, ?, ?)", (cpf, nome, email, idade, serie, nota))
    conn.commit()
    print("Aluno cadastrado com sucesso.")

# Função para listar todos os alunos
def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    print("\nLista de alunos:")
    for a in alunos:
        print(f"CPF: {a[0]}, Nome: {a[1]}, Email: {a[2]}, Idade: {a[3]}, Série: {a[4]}, Nota: {a[5]}")

def Adicionar_nota():
    cpf = input("Digite o seu cpf para adicionar uma nota").strip()
    cursor.execute("SELECT * FROM alunos WHERE cpf = ? ", (cpf,))
    aluno = cursor.fetchone()
    if not aluno:
     print("inválido")
     return
    nota_atual = aluno[5]
    nota = float(input(f"Qual nota deseja inserir em {aluno[1]} ? "))
    media = (nota + nota_atual)/2 
    cursor.execute("UPDATE alunos SET nota = ?  WHERE cpf= ?",(media,cpf))
    conn.commit()
    print(f"foi adicionada a nota {aluno[5]} em {aluno[1]} , nova media {media}")
   
def Consultar_boletim():
    cpf = input("Digite o seu cpf para adicionar uma nota").strip()
    cursor.execute("SELECT FROM alunos")
    aluno = cursor.fetchall()
    if not aluno:
        print(f"{cpf} inválido")
        return
    print(f"A nota do aluno{aluno[1]} é {aluno[5]}")
    conn.commit()
    

def fechar_conexao():
    conn.close()
