import math
import heapq
import random
import timeit
from sys import stdin,stdout
def readln():
 return stdin.readline().rstrip()
def outln(n):
 stdout.write(n)
 stdout.write("\n")
class Heaptree:
    def __init__(self):
        self.heap = []
        self.rotacoes=0

    def insert(self, chatId, username, prompt):
        for i in range(len(self.heap)):
            if self.heap[i][0] == chatId:
                if self.heap[i][1] != username:
                    self.heap[i][1] = username
                    self.heap[i][2] = [prompt]
                else:
                    self.heap[i][2].append(prompt)
                self.build_min_heap()
                return 0
        self.heap.append([chatId, username, [prompt]])
        self.build_min_heap()
        return 1

    def update(self):
        for i in range(len(self.heap)-1, -1, -1):
            self._update(math.floor(i/2), i)

    def _update(self, parent, child):
        if self.heap[child][0] < self.heap[parent][0]:
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]

    def remove(self, chatId):
        for i in range(len(self.heap)):
            if self.heap[i][0] == chatId:
                self.heap.pop(i)
                self.build_min_heap()
                return 1
        return 0

    def find(self, chatId):
        for i in range(len(self.heap)):
            if self.heap[i][0] == chatId:
                return self.heap[i][1], self.heap[i][2]
        return None, None

    def min_heapify(self, heap_size, i):
        l = 2 * i
        r = 2 * i + 1
        smallest = i
        if l < heap_size and self.heap[l][0] < self.heap[i][0]:
            smallest = l
        if r < heap_size and self.heap[r][0] < self.heap[smallest][0]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(heap_size, smallest)
            self.rotacoes += 1

    def build_min_heap(self):
        heap_size = len(self.heap)
        for i in range(heap_size // 2, -1, -1):
            self.min_heapify(heap_size, i)



if __name__=="__main__":
    apoio = [0.1, 0.9]
    for k in range(2):
        percentagem = apoio[k]
        for j in range(1, 6):
            tree=Heaptree()
            N = 20000 * j
            consola = ["NEW_PROMPT", "GET_CHAT", "DELETE_CHAT"]
            user = "user"
            palavras = ["eu", "sou", "uma", "maquina"]
            lista = []
            contador_insercoes = 0
            sum_time = 0
            max_insercoes = percentagem * N
            for i in range(N):
                if (contador_insercoes < max_insercoes):
                    indice = random.randint(0, 2)
                else:
                    indice = random.randint(1, 2)
                if (indice == 0):
                    contador_insercoes += 1
                    name = user + str(random.randint(1, N))
                    lista += ["{} {} {} {}".format(consola[indice], random.randint(1, N), name,
                                                   palavras[random.randint(0, 3)] + " " + palavras[
                                                       random.randint(0, 3)] + " " + palavras[
                                                       random.randint(0, 3)] + " " + palavras[random.randint(0, 3)])]
                elif (indice == 1):
                    name = user + str(random.randint(1, N))
                    lista += ["{} {}".format(consola[indice], random.randint(1, N))]
                elif (indice == 2):
                    name = user + str(random.randint(1, N))
                    lista += ["{} {}".format(consola[indice], random.randint(1, N))]
            lista += ["FIM"]
            sum_rotacoes = 0
            sum_time = 0
            h = 0
            user,prompt=None,None
            comando=" "
            while(comando[0]!="FIM"):
                #comando = input()
                comando = lista[h]
                comando = comando.split(" ")
                if(comando[0]=="NEW_PROMPT"):
                    start = timeit.default_timer()
                    tree.insert(int(comando[1]), comando[2], " ".join(comando[3:]))
                    time = timeit.default_timer() - start
                    sum_time += time
                    '''if(tree.insert(int(comando[1]), comando[2], " ".join(comando[3:]))):
                          outln("CHAT {} CRIADO".format(comando[1]))
                    else:
                         outln("CHAT {} ATUALIZADO".format(comando[1]))
                    tree.insertflag=-1'''
                elif(comando[0]=="GET_CHAT"):
                    start = timeit.default_timer()
                    user, prompt = tree.find(int(comando[1]))
                    time = timeit.default_timer() - start
                    sum_time += time
                    '''if(user!=None):
                       outln(user)
                      for i in prompt:
                            outln(i)
                        outln("FIM")
                     else:
                        outln("CHAT {} NAO ENCONTRADO".format(comando[1]))
                     user, prompt = None, None'''
                elif (comando[0] == "DELETE_CHAT"):
                    start = timeit.default_timer()
                    tree.remove(int(comando[1]))
                    time = timeit.default_timer() - start
                    sum_time += time
                    '''if (tree.remove(int(comando[1]))):
                        outln("CHAT {} APAGADO".format(comando[1]))
                    else:
                        outln("CHAT {} NAO ENCONTRADO".format(comando[1]))'''
                h += 1

            print("------------\nNºentradas: {}\n% inserções: {}\nTempo: {} s\nRotações: {}\n------------\n".format(N,
                                                                                                                      percentagem,
                                                                                                              sum_time,
                                                                                                              tree.rotacoes))