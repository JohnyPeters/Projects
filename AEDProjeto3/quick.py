import timeit
import random

trocas=0
def insertion_sort(lista_info):
    start = timeit.default_timer()
    lista_organizada=lista_info
    for i in range(1,len(lista_organizada)+1):
        for j in range(1,i):
            if(lista_organizada[i-j-1][0]>lista_organizada[i-j][0]):
                lista_organizada[i-j-1],lista_organizada[i-j]=lista_organizada[i-j],lista_organizada[i-j-1]
            else:
                break
    time = timeit.default_timer() - start
    #print(time)
    return lista_organizada

def quicksort(lista):
    global trocas
    #print(lista)
    if(len(lista)>1):
        aux=[[lista[0],0],[lista[len(lista)//2],len(lista)//2],[lista[-1],len(lista)-1]]
        aux.sort(key=lambda x: x[0])
        pivot=aux[1][1]
        print(pivot)
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
                if(i>pivot):
                    trocas+=1
            elif(lista[i][0]>lista[pivot][0]):
                direita.append(lista[i])
                if (i < pivot):
                    trocas += 1
            else:
                if(i<pivot):
                    esquerda.append(lista[i])
                else:
                    direita.append(lista[i])
    return quicksort(esquerda)+[lista[pivot]]+quicksort(direita)


def print_lista(lista):
    for i in range(len(lista)):
        tok=" "
        print(tok.join(lista[i]))
    print("FIM")

for i in range(1,11):
    N=1000000000*i

    registos_aleatorios = []

    for i in range(N):
        letras = "".join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        numeros1 = "".join(random.choices('0123456789', k=2))
        numeros2 = "".join(random.choices('0123456789', k=2))
        tipo_linha = random.choice(
            ['traco continuo', 'pneus nao homologados', 'excesso velocidade', 'busina avariada', 'pneus carecas', 'alcool',
             'luzes fundidas'])
        comprimento = random.randint(1, 10)
        nome = ' '.join(random.choices(
            ['Gabriela', 'Anabela', 'Carlos', 'Catarina', 'David', 'Alice', 'Liliana', 'Cilio', 'Fernanda', 'Belmira'],
            k=2))

        registos_aleatorios.append(f'{numeros1}{letras}{numeros2}{" "}{tipo_linha} {comprimento} {nome}')
    start = timeit.default_timer()
    #trocas=0
    #registos_aleatorios.sort(key=lambda x: x[0],reverse=True)
    lista=quicksort(registos_aleatorios)
    time = timeit.default_timer() - start
    print("{} elementos: {} s".format(N,time))
    #print(time)
    #print_lista(lista)