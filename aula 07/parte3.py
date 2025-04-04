def aluno(nome,idade,nota1,nota2):
    media = (nota1 + nota2)/2 
    return ({"nome":nome,"idade":idade,"media":media})
resultado1 = aluno("Ana",14,8,10)
print(resultado1)
    