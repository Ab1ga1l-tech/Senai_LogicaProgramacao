estoque ={}

while True:
    print(" Menu ")
    print(" 1. Cadastrar ") #ok
    print(" 2. Alterar Produto") #ok
    print(" 3. Consultar ") #ok
    print(" 4. Excluir Produtos ") #ok
    print(" 5. Adicionar")#
    print(" 6. Sair ")
    opção = (input("qual opção? \n "))
#Instanciar o dicionário

if opção == 1: 
    nome = input("Digite o nome do produto ")
    qtd = int(input(f"Digite a quantidade  de {nome}: "))
        
    if qtd > 0: 
    estoque[nome]= qtd
     print(f"Produto '{nome}' cadastrado com {qtd} unidades!")
        else: 
         del estoque[nome] 
         del qtd
        
    elif opção == '2': 
        nome = input("Digite o nome do produto ")
        qtd = int(input(f"Digite a quantidade  de  {nome}: "))
        if qtd > 0: 
          estoque[nome]= qtd
        else: 
         del estoque[nome] 
         del qtd
         
    elif opção == '3': 
        consulta = input("Digite o nome do produto para consultar")
        if consulta in estoque:
         print(f"{consulta} tem {estoque[consulta]}")
        else:
         print("produto não encontrado")
         print(estoque.items)

    elif opção =='4':
        consulta = input("Nome para excluir")
        if consulta in estoque:
         print(f"{consulta} custa R$ {estoque[consulta]:}")
         del estoque[consulta]
        else:
         print("produto não encontrado")
         
    elif opção == '5': 
        consulta = input("Digite o nome do produto para consultar")
        if consulta in estoque:
         print(f"{consulta} tem {estoque[consulta]}")
         
         adicionar = int(input("Qual quantidade você deseja adicionar ?"))
         estoque[consulta] = adicionar + qtd
        else:
         print("produto não encontrado")
         print(estoque.items)
  
    elif opção == '6':
        break
    else:
        print("Valor inválido")
print(estoque)

