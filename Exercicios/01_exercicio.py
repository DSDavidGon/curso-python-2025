#%%
#1. Faça um programa que dê bom dia.
print("Bom dia!")

#%%
#2. Faça um programa que de bom dia, pergunta o nome da pessoa e responde que é um prazer conhecer ela, citando o nome da pessoa.
print("Bom dia!")
nome = input("Qual o seu nome?")

print("Bom dia "+nome+ ", é um prazer conhecer você!")
#%%
#3. Crie uma história simples. Adicione essa história em um programa. A cada parágrafo, a história deve aguardar o usuário apertar “enter” para dar continuidade.
print("Um dia, um cão ia atravessando uma ponte, carregando um osso na boca.")
input()
print("Olhando para baixo, viu sua própria imagem refletida na água...")
input()
print("Pensando ver outro cão, cobiçou-lhe logo o osso e pôs-se a latir. ")
input()
print("Mal, porém, abriu a boca, seu próprio osso caiu na água e se perdeu para sempre.")
input()
print("Fim")
#%%
#4. Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.
numero = input("Fale um numero inteiro e trarei a sua raiz quadrada")
numero = int(numero)
raiz = numero ** 0.5
print("A raiz quadrada de "+ str(numero) +" é "+str(raiz))
#%%
#5. Faça um programa que exiba o dobro de um número inserido pelo usuário.
numero = input("Me fale um numero e dobrarei ele para você")
numero = int(numero)
dobro = numero*2
print("O dobro de "+str(numero)+ " é "+str(dobro))

#%%
#6. Faça um programa que exiba a seguinte receita de bolo de chocolate. Exiba um item por vez, conforme a pessoa aperte “enter”.

i1="2 xícaras de farinha de trigo"
i2 = "1 xícara de açúcar"
i3 = "1/2 xícara de cacau em pó"
i4 = "1 colher de chá de fermento em pó"
i5 = "1 colher de chá de bicarbonato de sódio"
i6 = "1/2 colher de chá de sal"
i7 = "2 ovos"
i8 = "1 xícara de leite"
i9 = "1/2 xícara de óleo vegetal"
i10 = "2 colheres de chá de extrato de baunilha"
i11 = "1 xícara de água fervente"
mp1 ="1. Pré-aqueça o forno a 180°C. Unte uma forma de bolo com manteiga e farinha, ou forre-a com papel manteiga."
mp2 ="2. Em uma tigela grande, peneire a farinha de trigo, o açúcar, o cacau em pó, o fermento em pó, o bicarbonato de sódio e o sal. Misture bem."
mp3 ="3. Em outra tigela, bata os ovos levemente. Adicione o leite, o óleo vegetal e o extrato de baunilha. Misture bem."
mp4 ="4. Despeje os ingredientes líquidos na mistura de ingredientes secos e mexa até que tudo esteja bem combinado."
mp5 ="5. Adicione a água fervente à massa e misture até que a massa fique homogênea. A massa ficará líquida, mas é normal."
mp6 ="6. Despeje a massa na forma preparada e leve ao forno pré-aquecido."
mp7 ="7. Asse por cerca de 30-35 minutos, ou até que um palito inserido no centro do bolo saia limpo."
mp8 ="8. Retire o bolo do forno e deixe esfriar na forma por alguns minutos. Em seguida, transfira para uma grade de resfriamento para esfriar completamente."
mp9 ="9. Depois de esfriar, você pode servir o bolo simples ou decorá-lo com cobertura de sua preferência, como ganache de chocolate ou glacê de chocolate."

print("Receita de Bolo de Chocolate")
print("Ingredientes")
print(i1)
input()
print(i2)
input()
print(i3)
input()
print(i4)
input()
print(i5)
input()
print(i6)
input()
print(i7)
input()
print(i8)
input()
print(i9)
input()
print(i10)
input()
print(i11)
input()
print("Modo de Preparo")
input()
print(mp1)
input()
print(mp2)
input()
print(mp3)
input()
print(mp4)
input()
print(mp5)
input()
print(mp6)
input()
print(mp7)
input()
print(mp8)
input()
print(mp9)
input()
