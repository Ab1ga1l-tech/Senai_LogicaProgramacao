nomes=[]

for i in range (3):
    nome= input(f"Digite o nome na posição {i+1}: ")
    nomes.append(nome)
    
for nome in nomes: 
    print(f" - {nome}",end="")
    
nome_remover = input("\n Digite o nome para remover")

if nome_remover in nomes:
    nomes.remove(nome_remover)
    print("Nome removido com sucesso")
    for nome in nomes:
        print({nome})
else:
    print("Não foi encontrado")
    
pos = int(input("\n Digite ")) 
del nomes[pos]
for nome in nomes:
    print(f"{nome}", end="")

for indice , nome in enumerate (nomes):
    if nome == "A":
        print(f"O Silvio está na posição {indice}")
    else:
        print("")
    
    