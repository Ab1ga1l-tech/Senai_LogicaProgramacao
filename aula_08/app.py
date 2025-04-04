# nove itens no cadastro 

from aula_08.meu_cadastro import*

def menu():
    carregar_dados()
    while True:
        print("1 - Cadastrar aluno")
        print("2 - Adicionar disciplina")
        print("3 - Adicionar nota")
        print("4 - Consultar boletim")
        print("5 - Consultar aluno pelo nome")
        print("6 - Editar dados do aluno")
        print("7 - Excluir aluno")
        print("8 - Excluir disciplina")
        print("9 - Sair")

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
            Consultar_aluno_nome()
        elif opcao == "6":
            Editar_dados_aluno()
        elif opcao == "7":
            Excluir_aluno()
        elif opcao == "8":
            Excluir_disciplina()
        elif opcao == "9":
            break
        

if __name__ == "__main__":
    menu()

