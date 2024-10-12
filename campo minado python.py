from random import randint

m=[]
n=[]
ma=[]
mb=[]
p=0
c=1

d=int(input("Qual a ordem do tamanho do campo? \n"))
b=int(input("Quantas bombas você quer? \n"))
for i in range(d):  #criando o campo normal
    l=[]
    for j in range(d):
        n="-O-"
        l.append(n)
    m.append(l)
print("\nEste é o campo:\n")
for i in range(d):  #imprimindo o campo normal
    for j in range(d):
        print(m[i][j], end=" ")
    print()

ma.append(randint(0, d-1))
mb.append(randint(0, d-1))

while c!=b: #criando as coordenadas das bombas
    ma.append(randint(0, d-1))
    mb.append(randint(0, d-1))
    c=c+1
    if ma[-1] in ma[:-1] and mb[-1] in mb[:-1]: #verificando se uma coordenada já apareceu. Se sim, vai ser excluída
        c-=1
        ma.pop()
        mb.pop()
print("\n##########################\n")
print("Para testes, se quiser logo acertar as bombas, as coordenadas das bombas são as seguintes:\n")

for i in range(len(ma)):    #imprimindo as coordenadas
    print(f"Bomba {i+1} | Linha: {ma[i]}, Coluna: {mb[i]}")

print("\n##########################\n")

while p<=b-1:
        c=int(input(f"Agora coloque a LINHA da coordenada que você acha que tem uma bomba (de 0 a {d-1}: )\n"))
        u=int(input(f"Agora coloque a COLUNA da coordenada que você acha que tem uma bomba (de 0 a {d-1}: )\n"))
        print("Se nada acontecer, significa que errou as coordenadas das bombas")
        for t in range(len(ma)):
            if c==ma[t] and u==mb[t]:   #verificando se existe uma bomba na coordenada que o usuário inseriu
                m[c][u]="-X-"
                p=p+1
                print("VOCÊ ACERTOU UMA BOMBA")
                for i in range(d):  #imprimindo o campo atualizado com a última bomba explodida
                    for j in range(d):
                        print(m[i][j], end=" ")
                    print()


print("VOCÊ VENCEU")