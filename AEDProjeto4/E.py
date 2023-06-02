from sys import stdin,stdout
import random
import timeit
def readln():
 return stdin.readline().rstrip()
def outln(n):
 stdout.write(n)
 stdout.write("\n")


class Node:
    def __init__(self,topico):
        self.topico=topico
        self.contagem=1
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.busca=False
        self.eliminado=False
        self.contagembusca=None
        self.insertflag=-1

    def insert(self,topico):
        if(self.root==None):
            self.root=Node(topico)
            self.insertflag=1
        elif(topico==self.root.topico):
            self.root.contagem+=1
            self.insertflag=0
        else:
            self._insert(self.root,topico)

    def _insert(self,node,topico):
        if (topico < node.topico):
            if(node.left==None):
                node.left=Node(topico)
                self.insertflag=1
            else:
                self._insert(node.left, topico)
        elif(topico > node.topico):
            if (node.right == None):
                node.right = Node(topico)
                self.insertflag= 1
            else:
                self._insert(node.right,topico)
        elif(topico == node.topico):
            node.contagem+=1
            self.insertflag=0



    def remove(self,topico):
        if(self.root!=None):
            if(self.root.topico==topico):
                if (self.root.right != None and self.root.left != None):
                    self.root.topico,self.root.plano = self.aux_remove(self.root,self.root.right)
                elif (self.root.left != None):
                    self.root = self.root.left
                elif (self.root.right != None):
                    self.root = self.root.right
                else:
                    self.root = None
                self.eliminado=True
            else:
                self._remove(self.root,topico)

    def _remove(self,node,topico):
        if(node.left!=None):
            if(node.left.topico==topico):
                if (node.left.right != None and node.left.left != None):
                    node.left.topico,node.left.plano = self.aux_remove(node.left,node.left.right)
                elif (node.left.left != None):
                    node.left = node.left.left
                elif (node.left.right != None):
                    node.left = node.left.right
                else:
                    node.left = None
                self.eliminado=True
            else:
                self._remove(node.left,topico)
        if (node.right != None):
            if (node.right.topico == topico):
                if(node.right.right!=None and node.right.left!=None):
                    node.right.topico,node.right.plano = self.aux_remove(node.right,node.right.right)
                elif(node.right.left!=None):
                    node.right=node.right.left
                elif(node.right.right!=None):
                    node.right=node.right.right
                else:
                    node.right=None
                self.eliminado=True
            else:
                self._remove(node.right, topico)

    def remove2(self,chatId):
        if(self.root!=None):
            if (self.root.chatId == chatId):
                if (self.root.right != None and self.root.left != None):
                    self.root.chatId, self.root.topico, self.root.prompt = self.aux_remove(self.root, self.root.right)
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
                    node.chatId,node.topico,node.prompt = self.aux_remove(node,node.right)
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
            return temp.chatId,temp.topico,temp.prompt
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
        return temp.topico, temp.contagem


    def print(self):
        if(self.root!=None):
            self._print(self.root)


    def _print(self,node):
        if(node!=None):
            outln("ChatID: {} topico: {} Prompt: {}".format(node.chatId,node.topico,node.prompt))
            self._print(node.left)
            self._print(node.right)


    def find(self,topico):
        if(self.root!=None):
            if(self.root.topico==topico):
                self.busca = True
                self.contagembusca=self.root.contagem
            else:
                self._find(self.root,topico)

    def _find(self,node,topico):
        if(node!=None):
            if(node.topico==topico):
                self.busca=True
                self.contagembusca=node.contagem
            elif(node.topico>topico):
                self._find(node.left, topico)
            elif (node.topico < topico):
                self._find(node.right, topico)

    def update(self,topico,plano):
        if(self.root!=None):
            if(self.root.topico==topico):
                self.updatado = True
                self.root.plano=plano
            else:
                self._update(self.root,topico,plano)

    def _update(self,node,topico,plano):
        if(node!=None):
            if(node.topico==topico):
                self.updatado=True
                node.plano=plano
            elif(node.topico>topico):
                self._update(node.left, topico,plano)
            elif (node.topico < topico):
                self._update(node.right, topico,plano)

    def search(self, chatId):
        current = self.root
        while current != None:
            if current.chatId == chatId:
                return current.topico,current.prompt
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
                    current.chatId,current.topico,current.prompt = self.aux_remove(current,current.right)
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

    def list(self):
        if(self.root!=None):
            return self._list(self.root.left)+["{} {}".format(self.root.topico,self.root.contagem)]+self._list(self.root.right)

    def _list(self,node):
        if(node!=None):
            return self._list(node.left)+["{} {}".format(node.topico,node.contagem)]+self._list(node.right)
        else:
            return []


if __name__=="__main__":

    '''
    tree.insert(2,"Johny","asdasdasd")
    tree.insert(3, "Manel", "bom dia")
    tree.insert(6, "Ana", "hghjgggggg")
    tree.insert(8,"Paulo","Oi amigo")
    #topico=tree.find(8)
    if(topico!=None):
        outln(topico)
    else:
        outln("Nao encontrado")


    tree.print()
    tree.remove(8)
    print('\n')
    tree.print()'''
    for j in range(1, 6):
        tree = BinarySearchTree()
        N = 20000 * j
        consola = ["ADD_SUBJECT", "GET_SUBJECT_COUNT", "LIST_ALL"]
        user = "user"
        # palavras = ["eu", "sou", "uma", "maquina"]
        lista = []
        contador_insercoes = 0
        sum_time = 0
        topicos = []
        percentagem_topicos = 0.5
        n_gets = 0
        contador_topicos = 0
        contador_acessos = 0
        for h in range(int(N * percentagem_topicos)):
            contador_topicos += 1
            name = user + str(random.randint(1, N))
            if (contador_topicos < int(N * percentagem_topicos * 0.05)):
                topicos += [name]
            lista += ["{} {}".format(consola[0], name)]

        for i in range(int(N * (1 - percentagem_topicos))):
            indice = random.randint(1, 2)
            if (indice == 1):
                contador_acessos += 1
                if (contador_acessos < 0.9 * len(topicos)):
                    name = topicos[random.randint(1, len(topicos) - 1)]
                else:
                    name = user + str(random.randint(1, N))
                lista += ["{} {}".format(consola[indice], name)]
            elif (indice == 2):
                # name = user + str(random.randint(1, N))
                lista += [consola[indice]]
        lista += ["FIM"]
        sum_rotacoes = 0
        sum_time = 0
        p = 0
        # print(lista[0])
        comando = " "
        while(comando[0]!="FIM"):
            #comando = input()
            comando=lista[p]
            comando = comando.split(" ")
            if(comando[0]=="ADD_SUBJECT"):
                start = timeit.default_timer()
                tree.insert((comando[1]))
                time = timeit.default_timer() - start
                sum_time += time
                '''if(tree.insertflag!=-1):
                    outln("REGISTADO")
                tree.insertflag=-1'''
            elif(comando[0]=="GET_SUBJECT_COUNT"):
                start = timeit.default_timer()
                tree.find((comando[1]))
                time = timeit.default_timer() - start
                sum_time += time
                '''if(tree.busca):
                    contagem=tree.contagembusca
                    outln("{} {}".format((comando[1]),contagem))
                    tree.busca = False
                else:
                    outln("SUBJECT NAO ENCONTRADO")'''
            elif(comando[0]=="LIST_ALL"):
                start = timeit.default_timer()
                listagem=tree.list()
                time = timeit.default_timer() - start
                sum_time += time
                '''for i in lista:
                    outln(i)
                outln("FIM")'''
            p += 1
        print("------------\nNºentradas: {}\n% inserções: {}\nTempo: {} s\n------------\nRotações: {}".format(N,
                                                                                                              "0.9 de 0.05",
                                                                                                              sum_time,
                                                                                                              sum_rotacoes))
