import json

alunos = {}

def cadastrar_aluno():
    cpf = input("CPF do aluno: ")
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    serie = input("Série: ")
    alunos[cpf] = {
        "nome": nome,
        "idade": idade,
        "serie": serie,
        "disciplinas": {}
    }

def adicionar_disciplina():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        disciplina = input("Nome da disciplina: ")
        alunos[cpf]["disciplinas"][disciplina] = []
    else:
        print("CPF não encontrado.")

def adicionar_nota():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        disciplina = input("Nome da disciplina: ")
        if disciplina in alunos[cpf]["disciplinas"]:
            nota = float(input("Nota: "))
            alunos[cpf]["disciplinas"][disciplina].append(nota)

def consultar_boletim():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        aluno = alunos[cpf]
        print(f"Boletim de {aluno['nome']} - {aluno['serie']}:")
        for d, notas in aluno["disciplinas"].items():
            media = sum(notas) / len(notas) if notas else 0
            print(f"{d}: notas = {notas}, média = {media:.2f}")
    else:
        print("Aluno não encontrado")
## 
'''def Consultar_aluno_nome():
    nome_consulta = input("Digite qual nome você quer ?")
    if nome_consulta in alunos[cpf]:
        alunos[cpf]=  {
        "nome": nome,
        "idade": idade,
        "serie": serie,
        "disciplinas": {}}'''


def salvar_dados():
    with open("alunos.json", "w", encoding="utf-8") as arq:
        json.dump(alunos, arq, indent=4)

def carregar_dados():
    global alunos
    try:
        with open("alunos.json", "r", encoding="utf-8") as arq:
            alunos = json.load(arq)
    except FileNotFoundError:
        print("Arquivo não encontrado. Iniciando com a base vazia")

            
if __name__ == "__main__":
    print()
    