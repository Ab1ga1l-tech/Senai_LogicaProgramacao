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
    nota INTEGER NOT NULL
)
""")
conn.commit()

# Função para cadastrar aluno
def cadastrar_aluno():
    cpf = input("CPF (somente números): ").strip()
    cursor.execute("SELECT cpf FROM alunos WHERE cpf = ?", (cpf,))
    if cursor.fetchone():
        print(" CPF já cadastrado.")
        return

    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    idade = int(input("Idade: "))
    serie = int(input("Série: "))
    nota = int(input("digite sua nota: "))

    cursor.execute("INSERT INTO alunos VALUES (?, ?, ?, ?, ?)", (cpf, nome, email, idade, serie))
    conn.commit()
    print(" Aluno cadastrado com sucesso.")

# Função para listar todos os alunos
def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    print("\n Lista de alunos:")
    for a in alunos:
        print(f"CPF: {a[0]}, Nome: {a[1]}, Email: {a[2]}, Idade: {a[3]}, Série: {a[4]}")

# Menu simples para testar
if __name__ == "_main_":
 def menu():
    while True:
        print("\n1. Cadastrar aluno\n2. Listar alunos\n3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            break
        else:
            print(" Opção inválida.")

# Fecha a conexão ao sair
conn.close()