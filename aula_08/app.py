from aula_08.meu_cadastro import*

def menu():
    carregar_dados()
    while True:
        print("1 - Cadastrar aluno")
        print("2 - Adicionar disciplina")
        print("3 - Adicionar nota")
        print("4 - Consultar boletim")
        print("5 - Salvar e sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            adicionar_disciplina()
        elif opcao == "3":
            adicionar_nota()
        elif opcao == "4":
            consultar_boletim()
        elif opcao == "5":
            salvar_dados()
            break

if __name__ == "__main__":
    menu()

