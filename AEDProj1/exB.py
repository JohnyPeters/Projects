def print_matriz(matriz):
    for i in range(len(matriz)):
        token=""
        for h in range(len(matriz[0])):
            if(h==len(matriz[0])-1):
                token += str(matriz[i][h])
            else:
                token+=str(matriz[i][h])+" "
        print(token)

def roda_matriz(matriz,linhas,colunas):
    novamatriz=[]
    for i in range(colunas):
        line=[]
        for h in range(linhas):
            line+=[0]
        novamatriz+=[line]
    #print_matriz(novamatriz)
    for i in range(colunas):
        for h in range(linhas):
            novamatriz[i][h]=matriz[linhas-h-1][i]
    return novamatriz,colunas,linhas




stringlida=input()
stringlida=stringlida.split()
linhas=int(stringlida[0])
colunas=int(stringlida[1])
matriz=[]
for i in range(linhas):
    line=input()
    line=[int(h) for h in line.split()]
    matriz+=[line]
#print_matriz(matriz)

for i in range(1,4):
    print(90*i)
    matriz,linhas,colunas= roda_matriz(matriz, linhas, colunas)
    print_matriz(matriz)



