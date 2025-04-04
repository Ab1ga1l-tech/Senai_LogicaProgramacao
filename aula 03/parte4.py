produtos=[]
preços= []
for i in range(1,4):
    produto=str(input("nome"))
    produtos.append(produto)
    
    preço = float(input("valor"))
    preços.append(preço)
    
produto_desejado = input("qual produto você quer? ")
for indice, produto in enumerate (produtos):
    if produto == produto_desejado:
        print(f"O {produto} tem o valor {preço[indice]} iremos deletar esses dados")
        del produtos[indice]
        del preços[indice]
        
        break
    else:
        print("")

print(produtos,preços)



     
     
