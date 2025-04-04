produtos={}

while True:
    print(" Menu ")
    print(" 1. Cadastrar ")
    print(" 2. Alterar Produto")
    print(" 3. Consultar ")
    print(" 4. Excluir Produtos ")
    print(" 5. Sair ")
    opção = (input("qual opção? \n "))

#Instanciar o dicionário

    if opção == '1': 
        nome = input("Digite um valor")
        preco = float(input(f"Digite o preco de {nome}: "))
        produtos[nome]= preco 
        
    elif opção == '2': 
        nome = input("Digite um valor")
        preco = float(input(f"Digite o preco de {nome}: "))
        produtos[nome]= preco        

    elif opção == '3': 
        consulta = input("Digite o nome do produto para consultar")
        if consulta in produtos:
         print(f"{consulta} custa R$ {produtos[consulta]:.2f}")
        else:
         print("produto não encontrado")
         print(produtos.items)

    elif opção =='4':
        excluir = input("Nome para excluir")
        if consulta in produtos:
         print(f"{consulta} custa R$ {produtos[consulta]:.2f}")
        else:
         print("produto não encontrado")
         print(produtos.items)
    elif opção == '5':
        break
    
         

