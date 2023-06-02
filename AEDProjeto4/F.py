from sys import stdin,stdout
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

    def insert(self, topico):
        node = Node(topico)
        node.parent = None
        node.topico = topico
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.topico < x.topico:
                x = x.left
            elif(node.topico > x.topico):
                x = x.right
            else:
                x.contagem+=1
                return

        node.parent = y
        if y == None:
            self.root = node
        elif node.topico < y.topico:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

        def fix_insert(self, k):
            while k.parent.color == 1:
                if k.parent == k.parent.parent.right:
                    u = k.parent.parent.left
                    if u.color == 1:
                        u.color = 0
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        k = k.parent.parent
                    else:
                        if k == k.parent.left:
                            k = k.parent
                            self.right_rotate(k)
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        self.left_rotate(k.parent.parent)
                else:
                    u = k.parent.parent.right

                    if u.color == 1:
                        u.color = 0
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        k = k.parent.parent
                    else:
                        if k == k.parent.right:
                            k = k.parent
                            self.left_rotate(k)
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        self.right_rotate(k.parent.parent)
                if k == self.root:
                    break
            self.root.color = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


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
    tree=Redtree()
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

    comando = " "
    while(comando[0]!="FIM"):
        comando = input()
        comando = comando.split(" ")
        if(comando[0]=="ADD_SUBJECT"):
            tree.insert((comando[1]))
            outln("REGISTADO")
        elif(comando[0]=="GET_SUBJECT_COUNT"):
            node=tree.search((comando[1]))
            if(node!=tree.TNULL):
                outln("{} {}".format((comando[1]),node.contagem))
            else:
                outln("SUBJECT NAO ENCONTRADO")
        elif(comando[0]=="LIST_ALL"):
            lista=tree.list()
            for i in lista:
                outln(i)
            outln("FIM")
