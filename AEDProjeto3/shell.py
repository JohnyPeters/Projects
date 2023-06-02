import timeit
import random

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
    print(time)
    return lista_organizada

def shellsort(lista_info):
    trocas=0
    start = timeit.default_timer()
    gap=round(len(lista_info)/2.2)

    lista_indices=[]
    for i in range(len(lista_info)):
        lista_indices.append([lista_info[i],i])

    #print(gap)
    while(gap>0):
        for h in range(gap):
            for i in range(h,len(lista_indices)+gap,gap):
                for j in range(gap,i,gap):
                    if (i - j - gap>-1) and (lista_indices[i - j - gap][0][0] > lista_indices[i - j][0][0]) or (lista_indices[i - j - gap][0][0] == lista_indices[i - j][0][0] and lista_indices[i - j - gap][1] > lista_indices[i - j][1]):
                        #print("{}>{} indices:{} e {}".format(lista_indices[i - j - gap][0][0], lista_indices[i - j][0][0],i-j-gap,i-j))
                        lista_indices[i-j - gap], lista_indices[i-j] = lista_indices[i-j],lista_indices[i-j - gap]
                        #trocas+=1
                    else:
                        break
        gap = round(gap / 2.2)
        #print(gap)

    time = timeit.default_timer() - start
    lista_organizada=[]
    for i in range(len(lista_indices)):
        lista_organizada.append(lista_indices[i][0])

    #print(time)
    return lista_organizada

def print_lista(lista):
    for i in range(len(lista)):
        tok=" "
        print(tok.join(lista[i]))
    print("FIM")

N = 900000

for i in range(1,11):
    N=100000*i

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

        registos_aleatorios.append([f'{numeros1}{letras}{numeros2}',tipo_linha,comprimento,nome])

    start = timeit.default_timer()

    #registos_aleatorios.sort(key=lambda x: x[0])
    #print(registos_aleatorios)
    lista=shellsort(registos_aleatorios)
    time = timeit.default_timer()-start
    print("{} elementos: {} s".format(N,time))
    #print_lista(lista)