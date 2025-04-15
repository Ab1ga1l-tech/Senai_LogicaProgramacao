frutas = ['banana', 'maçã', 'melancia', 'abacaxi']
cereais = ['aveia', 'granola', 'milho', 'trigo', 'linhaça']
precos = {
    "banana": 2.00, "maçã": 2.50, "melancia": 7.00, "abacaxi": 5.50,
    "aveia": 4.00, "granola": 5.50, "milho": 3.80, "trigo": 4.50, "linhaça": 6.00
}
vendas = [
    ["banana", 5, 2.00],      # R$ 10.00
    ["maçã", 8, 2.50],        # R$ 20.00
    ["melancia", 4, 7.00],    # R$ 28.00
    ["abacaxi", 4, 5.50],     # R$ 22.00
    ["aveia", 6, 4.00],       # R$ 24.00
    ["granola", 8, 5.50],     # R$ 44.00
    ["milho", 4, 3.80],       # R$ 15.20
    ["trigo", 7, 4.50],       # R$ 31.50
    ["linhaça", 5, 6.00],     # R$ 30.00
    ["maçã", 1, 2.00],        # ⚠️ abaixo do preço
    ["milho", 1, 4.50]        # ⚠️ acima do preço
]
# Objetivo buscado 
# - Mostrar um relatório de vendas com:
#   → Produto -, quantidade- , preço real- , preço vendido- , total vendido-

#- Calcular e exibir:
#   → Total geral de vendas 
#   → Total vendido em frutas 
#   → Total vendido em cereais 
#- Identificar o item mais e o menos vendido.
vendas_frutas = 0
vendas_totais = 0
vendas_cereais = 0 
valor_max = 0
valor_min = 100
lista = []
#produto, quantidade , preço e total de totodos 

relatório = {}

for produtos , quantidade , preco in vendas:
        valores = quantidade*preco
        relatório[produtos]= quantidade , preco, valores
print(relatório)
#vendas totais

for produtos, quantidade , preco in vendas:
        vendas_totais += quantidade*preco
print(vendas_totais)

#vendas frutas

for produtos , quantidade , preco in vendas:
        
        if produtos in frutas:
            vendas_frutas += quantidade*preco
print(vendas_frutas)

# vendas cereais 

for produtos , quantidade , preco in vendas:
        
        if produtos in cereais:
            vendas_cereais += quantidade*preco
print(vendas_cereais)
lista_valores = []
# mais vendido

for produtos , quantidade , preco in vendas:
         
         valores = quantidade*preco
         lista.append(valores)
print(lista)

#mais vendidos

for i in lista:
     if i > valor_max  :
        valor_max = i
        
print(valor_max)

# menos vendido 

for i in lista:
        if i < valor_min  :
            valor_min = i
print(valor_min)

#min
for produtos, quantidade , preco in vendas:
        valores = quantidade*preco
        if valores == valor_min:
            print(produtos,quantidade,preco,valores)

for produtos, quantidade , preco in vendas:
        valores = quantidade*preco
        if valores == valor_max:
            print(produtos,quantidade,preco,valores)


