import random
import timeit
from sys import stdin,stdout
def readln():
 return stdin.readline().rstrip()
def outln(n):
 stdout.write(n)
 stdout.write("\n")


class Node:
    def __init__(self,username,plano):
        self.username=username
        self.plano=plano
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.busca=False
        self.updatado = False
        self.eliminado=False
        self.planobusca=None
        self.insertflag=-1

    def insert(self,username,plano):
        if(self.root==None):
            self.root=Node(username,plano)
            self.insertflag=1
        elif(username==self.root.username):
            self.insertflag=0
        else:
            self._insert(self.root,username,plano)

    def _insert(self,node,username,plano):
        if (username < node.username):
            if(node.left==None):
                node.left=Node(username,plano)
                self.insertflag=1
            else:
                self._insert(node.left, username,plano)
        elif(username > node.username):
            if (node.right == None):
                node.right = Node(username,plano)
                self.insertflag= 1
            else:
                self._insert(node.right,username,plano)
        elif(username == node.username):
            self.insertflag=0



    def remove(self,username):
        if(self.root!=None):
            if(self.root.username==username):
                if (self.root.right != None and self.root.left != None):
                    self.root.username,self.root.plano = self.aux_remove(self.root,self.root.right)
                elif (self.root.left != None):
                    self.root = self.root.left
                elif (self.root.right != None):
                    self.root = self.root.right
                else:
                    self.root = None
                self.eliminado=True
            else:
                self._remove(self.root,username)

    def _remove(self,node,username):
        if(node.left!=None):
            if(node.left.username==username):
                if (node.left.right != None and node.left.left != None):
                    node.left.username,node.left.plano = self.aux_remove(node.left,node.left.right)
                elif (node.left.left != None):
                    node.left = node.left.left
                elif (node.left.right != None):
                    node.left = node.left.right
                else:
                    node.left = None
                self.eliminado=True
            else:
                self._remove(node.left,username)
        if (node.right != None):
            if (node.right.username == username):
                if(node.right.right!=None and node.right.left!=None):
                    node.right.username,node.right.plano = self.aux_remove(node.right,node.right.right)
                elif(node.right.left!=None):
                    node.right=node.right.left
                elif(node.right.right!=None):
                    node.right=node.right.right
                else:
                    node.right=None
                self.eliminado=True
            else:
                self._remove(node.right, username)

    def remove2(self,chatId):
        if(self.root!=None):
            if (self.root.chatId == chatId):
                if (self.root.right != None and self.root.left != None):
                    self.root.chatId, self.root.username, self.root.prompt = self.aux_remove(self.root, self.root.right)
                elif (self.root.left != None):
                    self.root = self.root.left
                elif (self.root.right != None):
                    self.root = self.root.right
                else:
                    self.root = None
                self.eliminado = True
            elif (self.root.chatId > chatId):
                self._remove(self.root.left, chatId)
            else:
                self._remove(self.root.right, chatId)


    def _remove2(self,node,chatId):
        if(node!=None):
            if(node.chatId==chatId):
                if (node.right != None and node.left != None):
                    node.chatId,node.username,node.prompt = self.aux_remove(node,node.right)
                elif (node.left != None):
                    node = node.left
                elif (node.right != None):
                    node = node.right
                else:
                    node = None
                self.eliminado=True
            elif (node.chatId > chatId):
                self._remove(node.left, chatId)
            else:
                self._remove(node.right, chatId)


    def aux_remove2(self,node):
        if(node.left==None):
            temp=node
            if(node.right==None):
                node=None
            else:
                node=node.right
            return temp.chatId,temp.username,temp.prompt
        else:
            self.aux_remove(node.left)

    def aux_remove(self,parent, node):
        flag=True
        while(node.left!=None):
            parent=node
            node=node.left
            flag=False
        if(flag):
            temp = node
            parent.right = node.right
        else:
            temp=node
            parent.left=node.right
        node=None
        return temp.username, temp.plano


    def print(self):
        if(self.root!=None):
            self._print(self.root)


    def _print(self,node):
        if(node!=None):
            outln("ChatID: {} Username: {} Prompt: {}".format(node.chatId,node.username,node.prompt))
            self._print(node.left)
            self._print(node.right)


    def find(self,username):
        if(self.root!=None):
            if(self.root.username==username):
                self.busca = True
                self.planobusca=self.root.plano
            else:
                self._find(self.root,username)

    def _find(self,node,username):
        if(node!=None):
            if(node.username==username):
                self.busca=True
                self.planobusca=node.plano
            elif(node.username>username):
                self._find(node.left, username)
            elif (node.username < username):
                self._find(node.right, username)

    def update(self,username,plano):
        if(self.root!=None):
            if(self.root.username==username):
                self.updatado = True
                self.root.plano=plano
            else:
                self._update(self.root,username,plano)

    def _update(self,node,username,plano):
        if(node!=None):
            if(node.username==username):
                self.updatado=True
                node.plano=plano
            elif(node.username>username):
                self._update(node.left, username,plano)
            elif (node.username < username):
                self._update(node.right, username,plano)

    def search(self, chatId):
        current = self.root
        while current != None:
            if current.chatId == chatId:
                return current.username,current.prompt
            elif chatId < current.chatId:
                current = current.left
            else:
                current = current.right
        return False,False

    def remove_novo(self, chatId):
        current = self.root
        while current != None:
            if current.chatId == chatId:
                if (current.right != None and current.left != None):
                    current.chatId,current.username,current.prompt = self.aux_remove(current,current.right)
                elif (current.left != None):
                    current = current.left
                elif (current.right != None):
                    current = current.right
                else:
                    current = None
                return True
            elif chatId < current.chatId:
                current = current.left
            else:
                current = current.right
        return False

if __name__=="__main__":

    '''
    tree.insert(2,"Johny","asdasdasd")
    tree.insert(3, "Manel", "bom dia")
    tree.insert(6, "Ana", "hghjgggggg")
    tree.insert(8,"Paulo","Oi amigo")
    #username=tree.find(8)
    if(username!=None):
        outln(username)
    else:
        outln("Nao encontrado")


    tree.print()
    tree.remove(8)
    print('\n')
    tree.print()'''
    apoio=[0.1,0.9]
    for k in range(2):
        percentagem = apoio[k]
        for j in range(1,6):
            tree = BinarySearchTree()
            N=20000*j
            consola = ["NEW_USER", "UPDATE_USER", "GET_TYPE", "DELETE_USER"]
            planos=["FREE","BASIC","PREMIUM"]
            user = "user"
            lista = []
            contador_insercoes=0
            sum_time=0
            max_insercoes=percentagem*N
            for i in range(N):
                if(contador_insercoes<max_insercoes):
                    indice=random.randint(0,3)
                else:
                    indice = random.randint(1, 3)
                if(indice==0):
                    contador_insercoes+=1
                    name=user+str(random.randint(1,N))
                    lista+=["{} {} {}".format(consola[indice],name,planos[random.randint(0,2)])]
                elif(indice==1):
                    name = user + str(random.randint(1, N))
                    lista += ["{} {} {}".format(consola[indice], name, planos[random.randint(0, 2)])]
                elif(indice==2):
                    name = user + str(random.randint(1, N))
                    lista += ["{} {}".format(consola[indice], name)]
                elif (indice == 3):
                    name = user + str(random.randint(1, N))
                    lista += ["{} {}".format(consola[indice], name)]
            lista+=["FIM"]
            sum_rotacoes=0
            sum_time=0
            h=0
            comando=" "
            while(comando[0]!="FIM"):
                #comando = input()
                comando=lista[h]
                #print(comando)
                comando = comando.split(" ")
                if(comando[0]=="NEW_USER"):
                    start = timeit.default_timer()
                    tree.insert((comando[1]), comando[2])
                    time = timeit.default_timer() - start
                    sum_time+=time
                    '''if(tree.insertflag==1):
                        outln("USER {} CRIADO".format(comando[1]))
                    elif(tree.insertflag==0):
                        outln("USER {} JA EXISTE".format(comando[1]))
                    tree.insertflag=-1'''
                elif(comando[0]=="GET_TYPE"):
                    start = timeit.default_timer()
                    tree.find((comando[1]))
                    time = timeit.default_timer() - start
                    sum_time += time
                    '''
                    if(tree.busca):
                        plano=tree.planobusca
                        outln(plano)
                        tree.busca = False
                    else:
                        outln("USER NAO ENCONTRADO")'''
                elif(comando[0]=="DELETE_USER"):
                    start = timeit.default_timer()
                    tree.remove((comando[1]))
                    time = timeit.default_timer() - start
                    sum_time += time
                    '''
                    if(tree.eliminado):
                        outln("USER {} APAGADO".format(comando[1]))
                        tree.eliminado=False
                    else:
                        outln("USER NAO ENCONTRADO")'''
                elif(comando[0]=="UPDATE_USER"):
                    start = timeit.default_timer()
                    tree.update((comando[1]),comando[2])
                    time = timeit.default_timer() - start
                    sum_time += time
                    '''
                    if (tree.updatado):
                        outln("USER {} ATUALIZADO".format(comando[1]))
                        tree.updatado = False
                    else:
                        outln("USER NAO ENCONTRADO")'''
                h+=1

            print("------------\nNºentradas: {}\n% inserções: {}\nTempo: {} s\n------------\nRotações: {}".format(N,percentagem,sum_time,sum_rotacoes))