# nove itens no cadastro 

from parte1 import*

def menu():
    
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
            listar_alunos()    
        elif opcao == "3":
            break
        

if __name__ == "__main__":
    menu()
