import random
frutas =["banana","maça", "uva"]
fruta_aleatória = random.choice(frutas)

for i in range(1,4):
   eu = (input(f"{frutas} \n escolha entre as frutas acima e tente adivinhar qual eu pensei: ")) 
if eu == fruta_aleatória:
    print(f" acertou, a fruta era {eu}")
       
else:
       print("errou, acabaram as tentativas")
       

