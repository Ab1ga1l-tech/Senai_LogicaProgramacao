from cadastro import *

def menu():
    
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar todos os alunos")
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
            listar_alunos()    
        elif opcao == "3":
            Adicionar_nota()
        elif opcao == "4":
            Consultar_boletim()
        elif  opcao =="5":
            Consultar_aluno_nome()
        elif opcao == "6":
            Editar_dados()
        elif opcao == "7":
            Exclui_aluno()   
        elif opcao == "8":
            Exclui_disciplina()
        elif opcao =="9":
            break   
        else:
            print("opção inválida")
    # Verifica se o aluno existe
if __name__=='__main__':
    menu()
