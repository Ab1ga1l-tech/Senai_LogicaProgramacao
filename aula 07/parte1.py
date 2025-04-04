def aluno(nome,idade,nota1,nota2):
    media = (nota1+nota2)/2
    return({"nome":nome,"idade":idade,"media":media})

resposta = aluno("Ana",14,8,6)
print(resposta)