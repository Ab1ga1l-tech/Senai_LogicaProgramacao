num1= float(input("Digite o primeiro número"))
num2= float(input("Digite o segundo número"))

operacao = input("Digite a operação desejada: \n somar:+ \n subtrair:- \n dividir:/\n mutiplicar:x\n :")

if operacao == "+" :
    print("Soma", num1+num2)
elif operacao == "-":
    print("Subtração", num1-num2)
elif operacao ==  "*":
    print("multiplicação", num1*num2)
elif operacao == "/":
    print("divisão",num1/num2)
else:
    print("Termo inválido")