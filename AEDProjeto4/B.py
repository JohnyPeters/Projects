import math
import heapq
from sys import stdin,stdout
def readln():
 return stdin.readline().rstrip()
def outln(n):
 stdout.write(n)
 stdout.write("\n")
class Node:
    def __init__(self,chatId,username,prompt):
        self.chatId=chatId
        self.username=username
        self.prompt=[prompt]

class Heaptree:
    def __init__(self):
        self.tree=[]

    def insert1(self,chatId,username,prompt):
        for i in range(len(self.tree)):
            if(self.tree[i][0]==chatId):
                if(self.tree[i][1]!=username):
                    self.tree[i][1]=username
                    self.tree[i][2]=[prompt]
                else:
                    self.tree[i][2]+=[prompt]
                self.build_max_heap()
                return 0
        self.tree+=[[chatId,username,[prompt]]]
        self.build_max_heap()
        #self.update()
        return 1

    def update1(self):
        for i in range(len(self.tree)-1,-1,-1):
            self._update(math.floor(i/2),i)

    def _update1(self,pai,filho):
        if(self.tree[filho][0]>self.tree[pai][0]):
            self.tree[filho],self.tree[pai]=self.tree[pai],self.tree[filho]

    def remove1(self,chatId):
        for i in range(len(self.tree)):
            if(self.tree[i][0]==chatId):
                self.tree.pop(i)
                self.build_max_heap()
                #self.update()
                return 1
        return 0

    def find(self,chatId):
        for i in range(len(self.tree)):
            if(self.tree[i][0]==chatId):
                return self.tree[i][1],self.tree[i][2]
        return None,None



    def max_heapify(self, heap_size, i):
        l = 2 * i
        r = 2 * i + 1
        largest = i
        if l < heap_size and self.tree[l][0] > self.tree[i][0]:
            largest = l
        if r < heap_size and self.tree[r][0] > self.tree[largest][0]:
            largest = r
        if largest != i:
            # swap elements
            self.tree[i], self.tree[largest] = self.tree[largest], self.tree[i]
            self.max_heapify(heap_size, largest)

    def build_max_heap(self):
        heap_size = len(self.tree)
        for i in range(heap_size // 2, 0, -1):
            self.max_heapify(heap_size, i)

    def insert(self, chatId, username, prompt):
        for i in range(len(self.tree)):
            if self.tree[i][0] == chatId:
                if self.tree[i][1] != username:
                    self.tree[i][1] = username
                    self.tree[i][2] = [prompt]
                else:
                    self.tree[i][2].append(prompt)
                return 0
        self.tree.append([[chatId,username,[prompt]]])
        heapq.heapify(self.tree)
        return 1

    def remove(self, chatId):
        for i in range(len(self.tree)):
            if self.tree[i][0] == chatId:
                self.tree.pop(i)
                heapq.heapify(self.tree)
                return 1
        return 0

    def find(self, chatId):
        for i in range(len(self.tree)):
            if self.tree[i][0] == chatId:
                return self.tree[i][1], self.tree[i][2]
        return None, None



import random

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
        comando = input()
        comando = comando.split(" ")
        if(comando[0]=="NEW_PROMPT"):
            tree.insert(int(comando[1]), comando[2], " ".join(comando[3:]))
            '''if(tree.insert(int(comando[1]), comando[2], " ".join(comando[3:]))):
                  outln("CHAT {} CRIADO".format(comando[1]))
            else:
                 outln("CHAT {} ATUALIZADO".format(comando[1]))
            tree.insertflag=-1'''
        elif(comando[0]=="GET_CHAT"):
             user, prompt = tree.find(int(comando[1]))
             '''if(user!=None):
                outln(user)
                for i in prompt:
                    outln(i)
                outln("FIM")
             else:
                outln("CHAT {} NAO ENCONTRADO".format(comando[1]))
             user, prompt = None, None'''
        elif (comando[0] == "DELETE_CHAT"):
            tree.remove(int(comando[1]))
            '''if (tree.remove(int(comando[1]))):
                outln("CHAT {} APAGADO".format(comando[1]))
            else:
                outln("CHAT {} NAO ENCONTRADO".format(comando[1]))'''