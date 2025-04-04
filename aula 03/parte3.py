Palavra = []
for i in range (3):
    nome = input("nome para adicionar ")
    Palavra.append(nome) 
print(Palavra)

nome_deletar = input("Nome para deletar e ter o indice: ")

for indice, nome in enumerate (Palavra):
    if nome == nome_deletar :
        print(f"O {nome} está na posição {indice} ")
        del Palavra[indice]
        break
    else:
        print(f"O termo {nome_deletar} não está na lista palavra")
print(Palavra)
    
    

