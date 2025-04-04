nomes = []
for i in range (3):
    nome= input(f"Digite o nome na posição {i+1}: ")
    nomes.append(nome)
for nome in nomes: 
    print(f" - {nome}",end="")