nota1 = float(input("Digite a sua nota"))
nota2 = float(input("Digite a sua nota"))
nota3 = float(input("Digite a sua nota"))
media = (nota1+nota2+nota3)/3
print(media)
if media >= 7:
    print("aprovado")
elif (media <7) & (media>=5):
    print("recuperação")
else: 
    print("Reprovado")
    