# %%

#Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra
    
    
# %%

#Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.
print("Soma de Alturas")
soma=0
contador=4
while contador > 0:
    a=input("Adicione a altura")
    a= float(a)
    soma+= a
    contador-= 1

print("Soma das alturas igual a", soma)
# %%

# Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”, mas quando o usuário apertar “enter” sem digitar valor algum, o programa para de receber valores, e exibe a soma de todos os valores digitados anteriormente.

saldo_total =0
while True:
    saldo = input("Entre com o saldo: ")
    if saldo == "":
        break
    saldo_total += float(saldo)
    
print(saldo_total)
    
# %%
