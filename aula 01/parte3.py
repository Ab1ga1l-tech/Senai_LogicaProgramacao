#idade

idade = int(input(" Digite a sua idade: "))

if (idade >= 60):
    print("idoso")
elif (idade >= 18) & (idade < 60):
    print("adulto")
elif (idade < 18) & (idade >= 12):
    print("adolescente")
else:
    print("criança")

