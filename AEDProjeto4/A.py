from sys import stdin,stdout
import random
import timeit
def readln():
 return stdin.readline().rstrip()
def outln(n):
 stdout.write(n)
 stdout.write("\n")


class Node:
    def __init__(self,chatId,username,prompt):
        self.chatId=chatId
        self.username=username
        self.prompt = [prompt]
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.busca=False
        self.eliminado=False
        self.userbusca=None
        self.promptbusca=None
        self.insertflag=-1

    def insert(self,chatId,username,prompt):
        if(self.root==None):
            self.root=Node(chatId,username,prompt)
            self.insertflag= 1
        elif(chatId==self.root.chatId):
            if(username==self.root.username):
                self.root.prompt+=[prompt]
            else:
                self.root.prompt = [prompt]
            self.insertflag= 0
        else:
            self._insert(self.root, chatId, username, prompt)

    def _insert(self,node,chatId,username,prompt):
        if (chatId < node.chatId):
            if(node.left==None):
                node.left=Node(chatId,username,prompt)
                self.insertflag=1
            else:
                self._insert(node.left, chatId, username, prompt)
        elif(chatId > node.chatId):
            if (node.right == None):
                node.right = Node(chatId, username, prompt)
                self.insertflag= 1
            else:
                self._insert(node.right, chatId, username, prompt)
        elif(chatId == node.chatId):
            if (username == node.username):
                node.prompt += [prompt]
            else:
                node.username=username
                node.prompt = [prompt]
            self.insertflag= 0



    def remove(self,chatId):
        if(self.root!=None):
            if(self.root.chatId==chatId):
                if (self.root.right != None and self.root.left != None):
                    self.root.chatId,self.root.username,self.root.prompt = self.aux_remove(self.root,self.root.right)
                elif (self.root.left != None):
                    self.root = self.root.left
                elif (self.root.right != None):
                    self.root = self.root.right
                else:
                    self.root = None
                self.eliminado=True
            else:
                self._remove(self.root,chatId)

    def _remove(self,node,chatId):
        if(node.left!=None):
            if(node.left.chatId==chatId):
                if (node.left.right != None and node.left.left != None):
                    node.left.chatId,node.left.username,node.left.prompt = self.aux_remove(node.left,node.left.right)
                elif (node.left.left != None):
                    node.left = node.left.left
                elif (node.left.right != None):
                    node.left = node.left.right
                else:
                    node.left = None
                self.eliminado=True
            else:
                self._remove(node.left,chatId)
        if (node.right != None):
            if (node.right.chatId == chatId):
                if(node.right.right!=None and node.right.left!=None):
                    node.right.chatId,node.right.username,node.right.prompt = self.aux_remove(node.right,node.right.right)
                elif(node.right.left!=None):
                    node.right=node.right.left
                elif(node.right.right!=None):
                    node.right=node.right.right
                else:
                    node.right=None
                self.eliminado=True
            else:
                self._remove(node.right, chatId)

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
        return temp.chatId, temp.username, temp.prompt


    def print(self):
        if(self.root!=None):
            self._print(self.root)


    def _print(self,node):
        if(node!=None):
            outln("ChatID: {} Username: {} Prompt: {}".format(node.chatId,node.username,node.prompt))
            self._print(node.left)
            self._print(node.right)


    def find(self,chatId):
        if(self.root!=None):
            if(self.root.chatId==chatId):
                self.busca = True
                self.userbusca,self.promptbusca=self.root.username,self.root.prompt
            else:
                self._find(self.root,chatId)

    def _find(self,node,chatId):
        if(node!=None):
            if(node.chatId==chatId):
                self.busca=True
                self.userbusca,self.promptbusca=node.username,node.prompt
            elif(node.chatId>chatId):
                self._find(node.left, chatId)
            elif (node.chatId < chatId):
                self._find(node.right, chatId)

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

    apoio = [0.1, 0.9]
    for k in range(2):
        percentagem = apoio[k]
        for j in range(1, 6):
            tree = BinarySearchTree()
            N = 20000 * j
            consola = ["NEW_PROMPT", "GET_CHAT", "DELETE_CHAT"]
            user = "user"
            palavras=["eu","sou","uma", "maquina"]
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
                    lista += ["{} {} {} {}".format(consola[indice],random.randint(1, N), name, palavras[random.randint(0, 3)]+" "+palavras[random.randint(0, 3)]+" "+palavras[random.randint(0, 3)]+" "+palavras[random.randint(0, 3)])]
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
            comando = " "
            while(comando[0]!="FIM"):
                #comando = input()
                comando = lista[h]
                comando = comando.split(" ")
                if(comando[0]=="NEW_PROMPT"):
                    start = timeit.default_timer()
                    tree.insert(int(comando[1]), comando[2], " ".join(comando[3:]))
                    time = timeit.default_timer() - start
                    sum_time += time
                    '''if(tree.insertflag==1):
                        outln("CHAT {} CRIADO".format(comando[1]))
                    elif(tree.insertflag==0):
                        outln("CHAT {} ATUALIZADO".format(comando[1]))
                    tree.insertflag=-1'''
                elif(comando[0]=="GET_CHAT"):
                    start = timeit.default_timer()
                    tree.find(int(comando[1]))
                    time = timeit.default_timer() - start
                    sum_time += time
                    '''if(tree.busca):
                        username,prompt=tree.userbusca,tree.promptbusca
                        outln(username)
                        for i in prompt:
                            outln(i)
                        outln("FIM")
                        tree.busca = False
                    else:
                        outln("CHAT {} NAO ENCONTRADO".format(comando[1]))'''
                elif(comando[0]=="DELETE_CHAT"):
                    start = timeit.default_timer()
                    tree.remove(int(comando[1]))
                    time = timeit.default_timer() - start
                    sum_time += time
                    '''if(tree.eliminado):
                        outln("CHAT {} APAGADO".format(comando[1]))
                        tree.eliminado=False
                    else:
                        outln("CHAT {} NAO ENCONTRADO".format(comando[1]))'''
                h += 1
            print("------------\nNºentradas: {}\n% inserções: {}\nTempo: {} s\n------------\nRotações: {}".format(N,
                                                                                                                  percentagem,
                                                                                                                  sum_time,
                                                                                                                  sum_rotacoes))