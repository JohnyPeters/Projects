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
        self.color=1
        self.topico = topico
        self.contagem = 1
        self.left = None
        self.right = None
        self.parent=None

class Redtree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.rotacoes=0

    def insert(self, topico):
        node = Node(topico)
        node.parent = None
        node.topico = topico
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        node_aux2 = None
        node_aux1 = self.root

        while node_aux1 != self.TNULL:
            node_aux2 = node_aux1
            if node.topico < node_aux1.topico:
                node_aux1 = node_aux1.left
            elif (node.topico > node_aux1.topico):
                node_aux1 = node_aux1.right
            else:
                node_aux1.contagem += 1
                return

        node.parent = node_aux2
        if node_aux2 == None:
            self.root = node
        elif node.topico < node_aux2.topico:
            node_aux2.left = node
        else:
            node_aux2.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0

    def left_rotate(self, node_aux1):
        self.rotacoes += 1
        node_aux2 = node_aux1.right
        node_aux1.right = node_aux2.left
        if node_aux2.left != self.TNULL:
            node_aux2.left.parent = node_aux1

        node_aux2.parent = node_aux1.parent
        if node_aux1.parent == None:
            self.root = node_aux2
        elif node_aux1 == node_aux1.parent.left:
            node_aux1.parent.left = node_aux2
        else:
            node_aux1.parent.right = node_aux2
        node_aux2.left = node_aux1
        node_aux1.parent = node_aux2

    def right_rotate(self, node_aux1):
        self.rotacoes += 1
        node_aux2 = node_aux1.left
        node_aux1.left = node_aux2.right
        if node_aux2.right != self.TNULL:
            node_aux2.right.parent = node_aux1

        node_aux2.parent = node_aux1.parent
        if node_aux1.parent == None:
            self.root = node_aux2
        elif node_aux1 == node_aux1.parent.right:
            node_aux1.parent.right = node_aux2
        else:
            node_aux1.parent.left = node_aux2
        node_aux2.right = node_aux1
        node_aux1.parent = node_aux2

    def list(self):
        if(self.root!=self.TNULL):
            return self._list(self.root.left)+["{} {}".format(self.root.topico,self.root.contagem)]+self._list(self.root.right)

    def _list(self,node):
        if(node!=self.TNULL):
            return self._list(node.left)+["{} {}".format(node.topico,node.contagem)]+self._list(node.right)
        else:
            return []

    def search(self, topico):
        return self._search(self.root, topico)

    def _search(self, node, topico):
        if node == self.TNULL or topico == node.topico:
            return node

        if topico < node.topico:
            return self._search(node.left, topico)
        return self._search(node.right, topico)

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
        tree=Redtree()
        N = 20000 * j
        consola = ["ADD_SUBJECT", "GET_SUBJECT_COUNT", "LIST_ALL"]
        user = "user"
        #palavras = ["eu", "sou", "uma", "maquina"]
        lista = []
        contador_insercoes = 0
        sum_time = 0
        topicos=[]
        percentagem_topicos=0.2
        n_gets=0
        contador_topicos=0
        contador_acessos = 0
        for h in range(int(N*percentagem_topicos)):
            contador_topicos+=1
            name = user + str(random.randint(1, N))
            if(contador_topicos<int(N*percentagem_topicos*0.05)):
                topicos += [name]
            lista += ["{} {}".format(consola[0], name)]

        for i in range(int(N*(1-percentagem_topicos))):
            indice = random.randint(1, 2)
            if (indice == 1):
                contador_acessos+=1
                if(contador_acessos<len(topicos)):
                    name=topicos[random.randint(1,len(topicos)-1)]
                else:
                    name = user + str(random.randint(1, N))
                lista += ["{} {}".format(consola[indice], name)]
            elif (indice == 2):
                #name = user + str(random.randint(1, N))
                lista += [consola[indice]]
        lista += ["FIM"]
        sum_rotacoes = 0
        sum_time = 0
        p = 0
        #print(lista[0])
        comando = " "
        while(comando[0]!="FIM"):
            #comando = input()
            comando = lista[p]
            comando = comando.split(" ")
            #print(comando)
            if(comando[0]=="ADD_SUBJECT"):
                start = timeit.default_timer()
                tree.insert((comando[1]))
                time = timeit.default_timer() - start
                sum_time += time
                #outln("REGISTADO")
            elif(comando[0]=="GET_SUBJECT_COUNT"):
                start = timeit.default_timer()
                node=tree.search((comando[1]))
                time = timeit.default_timer() - start
                sum_time += time
                '''if(node!=tree.TNULL):
                    outln("{} {}".format((comando[1]),node.contagem))
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
        print("------------\nNºentradas: {}\n% acessos: {}\nTempo: {} s\nRotações: {}\n------------\n".format(N,
                                                                                                                  "0.9 de 0.05",
                                                                                                                  sum_time,
                                                                                                                      tree.rotacoes))
