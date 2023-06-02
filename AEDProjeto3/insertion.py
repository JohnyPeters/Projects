import timeit
import random

def insertion_sort(lista_info):
    #start = timeit.default_timer()
    troca=0
    lista_organizada=lista_info
    for i in range(1,len(lista_organizada)+1):
        for j in range(1,i):
            if(lista_organizada[i-j-1][0]>lista_organizada[i-j][0]):
                lista_organizada[i-j-1],lista_organizada[i-j]=lista_organizada[i-j],lista_organizada[i-j-1]
                troca+=1
            else:
                break
    #time = timeit.default_timer() - start
    #print(time)
    return lista_organizada,troca

def print_lista(lista):
    for i in range(len(lista)):
        tok=" "
        print(tok.join(lista[i]))
    print("FIM")

#file=open("cenas_aed.txt","w+")
for i in range(1):
    N=100000
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
    #registos_aleatorios.sort(key=lambda x: x[0],reverse=True)
    lista=insertion_sort(registos_aleatorios)
    time = timeit.default_timer() - start
    print("{} elementos: {} s".format(N,time))
    #file.write("Insertion ({} elementos): {}\n".format(N,time))
#file.close()
#print_lista(lista)