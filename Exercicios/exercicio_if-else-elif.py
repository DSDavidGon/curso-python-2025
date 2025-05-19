# %%
#1. Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50
texto = """Tá com sede? Escolha uma água para beber! 
1. Água mineral natural 
2. para água com gás."""
numero = input(texto)

if numero=="1":
    print("Está aqui sua garrafa, ela custa R$1,50")
elif numero=="2":
    print("Está aqui sua garrafa, ela custa R$2,50")
else:
    print("Entre com uma opção válida")

# %%
#2. Altere o programa anterior para considerar a quantidade de garrafas de água

numero = input(texto)
numero = int(numero)
quant = input("Quantas garrafas")
quant = int(quant)
conta = 0

if numero==1:
    conta = 1.5*quant
elif numero==2:
    conta = 2.5*quant

if conta==0:
    print("Entre com uma opção válida.")
else:
    print("Sua conta total é de R$",conta)
    
# %%
#3. Faça o programa de uma sorveteria, onde o usuário pode escolher:
#Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
#Sabor do sorvete: morango, creme, chocolate
#Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago
texto1 = """Bem vindo a Pingo. Por favor escolha o tipo de sorvete pelo número: 1. Casquinha R$ 1,00
2. Cascão R$ 2,50
3. Cestinha R$ 4,00"""
tipo = input(texto1)
tipo = int(tipo)

texto2 =""" Escolha um sabor:
1. Morango
2. Creme 
3. Chocolate"""
sabor = input(texto2)

texto3 = """Escolha uma cobertura, será cobrado um valor de R$ 1,50 para a cobertura:
1. Caramelo
2. Morango
3.Chocolate
4. Sem cobertura"""
cobertura = input(texto3)
cobertura= int(cobertura)

valor = 0

if tipo==1:
    valor = valor + 1
elif tipo==2:
    valor = valor + 2.5
elif tipo==3:
    valor = valor + 4
else:
    print("Escolha uma opção válida.")

if cobertura in [1,2,3]:
    valor = valor + 1.5
elif cobertura==4:
    valor=valor
else:
    print("Escolha uma opção válida")

print("Seu pedido foi computado, o valor total é de R$ "+str(valor))
# %%
#4. Faça um programa que verifique se a pessoa pertence à família “Calvo”.

sobrenome = input("Por favor digite seu sobrenome:")

if sobrenome == "Calvo":
    print("Bem vindo a família Calvo!")
else:
    print("Você não pertence a família Calvo")

# %%
#5. Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.
sobrenome = input("Por favor digite seu sobrenome:")

if sobrenome == "Calvo":
    print("Bem vindo a família Calvo!")
elif sobrenome == "Silva":
    print("Bem vindo a família Silva!")
else:
    print("Você não pertence a família Calvo nem a Silva")
    
# %%
#6. Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

item = input("Escolha um item e verificaremos se ele está disponivel.")

if item in ["laranja","cerveja","miojo","carvão","picanha"]:
    print("O item escolhido está disponível")
else:
    print("Infelizmente não temos esse item.")