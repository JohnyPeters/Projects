import timeit
def dim_bd(n,lista_info):
    for i in range(n):
        string=auxiliar(input())
        lista_info+=[string]
    print("BD_ATUALIZADA")

def auxiliar(string):
    lista=[string[0:6]]
    string=string[7:]
    for i in range(len(string)):
        if(string[i].isdigit()):
            lista+=[string[:i-1]]
            lista+=[string[i]]
            lista+=[string[i+2:]]
            break;
    return lista


def consulta_matricula(matricula,lista_info):
    flag=False
    for i in range(len(lista_info)):
        if(lista_info[i][0]==matricula):
            tok=" "
            print(tok.join(lista_info[i][1:]))
            flag=True
    if(not flag):
        print("REGISTOS NAO ENCONTRADOS")

    print("FIM")

def consulta_condutor(nome,lista_info):
    flag = False
    for i in range(len(lista_info)):
        if(lista_info[i][-1]==nome):
            tok=" "
            print(tok.join(lista_info[i][:-1]))
            flag = True

    if (not flag):
        print("REGISTOS NAO ENCONTRADOS")

    print("FIM")

def maximo(lista):
    maxi=lista[0][0]
    indice=0
    for i in range(len(lista)):
        if(lista[i][0]>maxi):
            maxi=lista[i][0]
            indice=i
    return indice

def minimo(lista):
    min=lista[0][0]
    indice=0
    for i in range(len(lista)):
        if(lista[i][0]<min):
            min=lista[i][0]
            indice=i
    return indice

def consulta_BD_insertion_sort(lista_info):
    start = timeit.default_timer()
    lista_organizada=lista_info
    for i in range(1,len(lista_organizada)+1):
        for j in range(1,i):
            if(lista_organizada[i-j-1][0]>lista_organizada[i-j][0]):
                temp=lista_organizada[i-j-1]
                lista_organizada[i-j-1]=lista_organizada[i-j]
                lista_organizada[i-j]=temp
            else:
                break
    time = timeit.default_timer() - start
    print(time)
    return lista_organizada

def consulta_BD_insertion_sort_beta(lista_info,gap=1):
    lista_organizada=lista_info
    for i in range(0,len(lista_organizada),gap):
        for j in range(i,len(lista_organizada)-gap,gap):
            if(j+gap<len(lista_organizada)):
                if(lista_organizada[j][0]>lista_organizada[j+gap][0]):
                    lista_organizada[j],lista_organizada[j+gap]=lista_organizada[j+gap],lista_organizada[j]
                else:
                    #print("break")
                    break
    return lista_organizada

def consulta_BD_quicksort(lista):
    #print(lista)
    if(len(lista)>1):
        aux=[[lista[0],0],[lista[len(lista)//2],len(lista)//2],[lista[-1],len(lista)-1]]
        aux.sort(key=lambda x: x[0])
        pivot=aux[1][1]
        #pivot=[[lista[0],0],[lista[len(lista)//2],len(lista)//2],[lista[-1],len(lista)-1]].sort(key=lambda x: x[0])[1][1]
    else:
        return lista

    # pivo=maximo([lista[0],lista[int(len(lista)/2)],lista[-1]])
    esquerda=[]
    direita=[]
    for i in range(len(lista)):
        if(i!=pivot):
            if(lista[i][0]<lista[pivot][0]):
                esquerda.append(lista[i])
            elif(lista[i][0]>lista[pivot][0]):
                direita.append(lista[i])
            else:
                if(i<pivot):
                    esquerda.append(lista[i])
                else:
                    direita.append(lista[i])
    return consulta_BD_quicksort(esquerda)+[lista[pivot]]+consulta_BD_quicksort(direita)


def consulta_BD_tinoquicksort(lista):
    if(len(lista)==1):
        return lista
    elif(len(lista)==2):
        if(lista[0][0]>lista[1][0]):
            lista[0],lista[1]=lista[1],lista[0]
            return lista

    pivo=int(len(lista)/2)
    # pivo=maximo([lista[0],lista[int(len(lista)/2)],lista[-1]]
    esquerda=[]
    direita=[]
    for i in range(len(lista)):
        if(i!=pivo):
            if(lista[i][0]<lista[pivo][0]):
                esquerda+=lista[i]
            else:
                direita+=lista[i]
    if (len(lista) > 3):
        return consulta_BD_tinoquicksort(esquerda)+[lista[pivo]]+consulta_BD_tinoquicksort(direita)
    elif(len(lista) == 3):
        return esquerda+[lista[pivo]]+direita



def consulta_BD_pseudo_shell_sort(lista_info):
    start = timeit.default_timer()
    lista_organizada=lista_info
    gap=int(len(lista_organizada)//2.2)
    while(gap>=2):
        for i in range(len(lista_organizada)-gap):
            if(lista_organizada[i][0]>lista_organizada[i+gap][0]):
                lista_organizada[i][0],lista_organizada[i+gap][0]=lista_organizada[i+gap][0],lista_organizada[i][0]
        gap=int(gap//2.2)
    time = timeit.default_timer() - start
    print(time)
    return lista_organizada

def consulta_BD_shell_sort_second(lista_info):
    start = timeit.default_timer()
    lista_organizada=lista_info
    gap=int(len(lista_organizada)/2.2)
    indice=0
    while(gap>0):
        for i in range(gap):
            for j in range(i+gap,len(lista_organizada),gap):
                if (lista_organizada[j-gap][0] > lista_organizada[j][0]):
                    lista_organizada[j-gap][0], lista_organizada[j][0] = lista_organizada[j][0],lista_organizada[j-gap][0]
        gap=int(gap/2.2)
    time = timeit.default_timer() - start
    print(time)
    return lista_organizada

def consulta_BD_shellsort(lista_info):
    start = timeit.default_timer()
    lista_organizada=lista_info
    gap=int(len(lista_organizada)/2.2)
    gap_real=len(lista_organizada)/2.2
    indice=0
    #print(gap)
    while(gap>0):
        for h in range(gap):
            for i in range(h,len(lista_organizada)+gap,gap):
                for j in range(gap,i,gap):
                    if (lista_organizada[i-j - gap][0] > lista_organizada[i-j][0]):
                        lista_organizada[i-j - gap], lista_organizada[i-j] = lista_organizada[i-j],lista_organizada[i-j - gap]
                    else:
                        break;
        gap=int(gap_real/2.2)
        gap_real = gap_real/ 2.2
        #print(gap)


    time = timeit.default_timer() - start
    print(time)
    return lista_organizada

def consulta_BD_tinosort(lista_info):
    start = timeit.default_timer()
    lista_organizada=lista_info
    for i in range(len(lista_organizada)):
        indice=maximo(lista_organizada[i:])
        elem=lista_organizada.pop(indice+i)
        lista_organizada=[elem]+lista_organizada
    time = timeit.default_timer() - start
    print(time)
    return lista_organizada

def print_lista(lista):
    for i in range(len(lista)):
        tok=" "
        print(tok.join(lista[i]))
    print("FIM")



lista_informacoes=[]
while(1):
    cmd=input().split(" ")
    if(cmd[0]=="DIM_BD"):
        dim_bd(int(cmd[1]),lista_informacoes)
    elif(cmd[0]=="CONSULTA_MATRICULA"):
        consulta_matricula(cmd[1],lista_informacoes)
    elif(cmd[0]=="CONSULTA_CONDUTOR"):
        #print(cmd)
        consulta_condutor(" ".join(cmd[1:]),lista_informacoes)
    elif(cmd[0]=="CONSULTA_BD"):
        #lista_organizada=consulta_BD_pseudo_shell_sort(lista_informacoes)
        #lista_organizada2=consulta_BD_insertion_sort(lista_organizada)
        lista_organizada=consulta_BD_insertion_sort(lista_informacoes)
        print_lista(lista_organizada)
    elif(cmd[0]=="TCHAU"):
        break;
    else:
        print("Introduza um comando válido")



