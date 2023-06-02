# Author: Marco Simoes
# Adapted from Java's implementation of Rui Pedro Paiva
# Teoria da Informacao, LEI, 2022

import sys
import numpy as np
from huffmantree import HuffmanTree


class GZIPHeader:
    ''' class for reading and storing GZIP header fields '''

    ID1 = ID2 = CM = FLG = XFL = OS = 0
    MTIME = []
    lenMTIME = 4
    mTime = 0

    # bits 0, 1, 2, 3 and 4, respectively (remaining 3 bits: reserved)
    FLG_FTEXT = FLG_FHCRC = FLG_FEXTRA = FLG_FNAME = FLG_FCOMMENT = 0

    # FLG_FTEXT --> ignored (usually 0)
    # if FLG_FEXTRA == 1
    XLEN, extraField = [], []
    lenXLEN = 2

    # if FLG_FNAME == 1
    fName = ''  # ends when a byte with value 0 is read

    # if FLG_FCOMMENT == 1
    fComment = ''  # ends when a byte with value 0 is read

    # if FLG_HCRC == 1
    HCRC = []

    def read(self, f):
        ''' reads and processes the Huffman header from file. Returns 0 if no error, -1 otherwise '''

        # ID 1 and 2: fixed values
        self.ID1 = f.read(1)[0]
        if self.ID1 != 0x1f: return -1  # error in the header

        self.ID2 = f.read(1)[0]
        if self.ID2 != 0x8b: return -1  # error in the header

        # CM - Compression Method: must be the value 8 for deflate
        self.CM = f.read(1)[0]
        if self.CM != 0x08: return -1  # error in the header

        # Flags
        self.FLG = f.read(1)[0]

        # MTIME
        self.MTIME = [0] * self.lenMTIME
        self.mTime = 0
        for i in range(self.lenMTIME):
            self.MTIME[i] = f.read(1)[0]
            self.mTime += self.MTIME[i] << (8 * i)

        # XFL (not processed...)
        self.XFL = f.read(1)[0]

        # OS (not processed...)
        self.OS = f.read(1)[0]

        # --- Check Flags
        self.FLG_FTEXT = self.FLG & 0x01
        self.FLG_FHCRC = (self.FLG & 0x02) >> 1
        self.FLG_FEXTRA = (self.FLG & 0x04) >> 2
        self.FLG_FNAME = (self.FLG & 0x08) >> 3
        self.FLG_FCOMMENT = (self.FLG & 0x10) >> 4

        # FLG_EXTRA
        if self.FLG_FEXTRA == 1:
            # read 2 bytes XLEN + XLEN bytes de extra field
            # 1st byte: LSB, 2nd: MSB
            self.XLEN = [0] * self.lenXLEN
            self.XLEN[0] = f.read(1)[0]
            self.XLEN[1] = f.read(1)[0]
            self.xlen = self.XLEN[1] << 8 + self.XLEN[0]

            # read extraField and ignore its values
            self.extraField = f.read(self.xlen)

        def read_str_until_0(f):
            s = ''
            while True:
                c = f.read(1)[0]
                if c == 0:
                    return s
                s += chr(c)

        # FLG_FNAME
        if self.FLG_FNAME == 1:
            self.fName = read_str_until_0(f)

        # FLG_FCOMMENT
        if self.FLG_FCOMMENT == 1:
            self.fComment = read_str_until_0(f)

        # FLG_FHCRC (not processed...)
        if self.FLG_FHCRC == 1:
            self.HCRC = f.read(2)

        return 0


class GZIP:
    ''' class for GZIP decompressing file (if compressed with deflate) '''

    gzh = None
    gzFile = ''
    fileSize = origFileSize = -1
    numBlocks = 0
    f = None

    bits_buffer = 0
    available_bits = 0

    def __init__(self, filename):
        self.gzFile = filename
        self.f = open(filename, 'rb')
        self.f.seek(0, 2)
        self.fileSize = self.f.tell()
        self.f.seek(0)

    def decompress(self):
        ''' main function for decompressing the gzip file with deflate algorithm '''

        numBlocks = 0

        # get original file size: size of file before compression
        origFileSize = self.getOrigFileSize()
        print(origFileSize)

        # read GZIP header
        error = self.getHeader()
        if error != 0:
            print('Formato invalido!')
            return

        # show filename read from GZIP header
        print(self.gzh.fName)

        # MAIN LOOP - decode block by block
        BFINAL = 0
        while not BFINAL == 1:

            BFINAL = self.readBits(1)

            BTYPE = self.readBits(2)
            if BTYPE != 2:
                print('Error: Block %d not coded with Huffman Dynamic coding' % (numBlocks + 1))
                return

            # --- STUDENTS --- ADD CODE HERE
            #
            #ex1
            #leitura dos valores do HLIT,HDIST e HCLEN
            HLIT = self.readBits(5)
            HDIST = self.readBits(5)
            HCLEN = self.readBits(4)
            print("Ponto 1:", HLIT, HDIST,HCLEN)

            #ex2

            #funcao que guarda os valores do (HCLEN+4)x3 num array
            def lenCodigosHCLEN(self,HCLEN):
                #lista auxiliar dada no enunciado
                listaAux=[16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]
                arrayAux=np.array(listaAux)
                arrayHCLEN= np.zeros(19)
                #leitura e armazenamento dos valores lidos no array
                for i in range(HCLEN+4):
                    bits = self.readBits(3)
                    arrayHCLEN[arrayAux[i]] = bits
                return arrayHCLEN

            #array com os comprimentos (HCLEN)
            arrayHCLEN=lenCodigosHCLEN(self,HCLEN)
            print("Ponto 2:",arrayHCLEN)

            #ex3
            #funcao que recebe uma string de um numero em binario e retorna o seu correspondente na base 10
            def binarioToDecimal(binario):
                decimal = 0
                for i in range(len(binario)):
                    decimal += int(binario[i]) * (2 ** (len(binario) - (i + 1)))
                return decimal

            #funcao que recebe um numero decimal e retorna a sua conversao em binario em forma de string
            def decimal_to_binary(decimal):
                string = ""
                dividendo = decimal
                while (dividendo != 0):
                    resto = dividendo % 2
                    dividendo = int(dividendo) // 2
                    string = str(resto) + string

                return string
            #funcao que recebe um array e um objeto e retorna o indice da primeira ocorrencia desse objeto no array
            def primeira_ocorrencia(array,ocorrencia):
                for i in range(len(array)):
                    if(array[i]==ocorrencia):
                        return i
                return -1
            #funcao que recebe um valor inteiro e retorna uma string com esse valor de zeros
            def cria_string_zeros(comp):
                string=""
                for i in range((comp)):
                    string+="0"
                return string


            #funcao que gera os codigos de huffman para os dados comprimentos
            def converteComprimentos(arrayHCLEN):
                arrayComp=[]
                #inicializacao da lista final
                for i in range(len(arrayHCLEN)):
                    arrayComp+=[False]
                #inicializacao das flags
                anterior="x"
                mudanca=False
                encontrou=False
                for j in range(1,int(max(arrayHCLEN))+1):
                    for i in range(len(arrayHCLEN)):
                        #a criacao dos codigos é feita por ordem dos comprimentos
                        if(arrayHCLEN[i]==j):
                            encontrou=True
                            #primeira ocorrencia
                            if(anterior=="x"):
                                arrayComp[i]=cria_string_zeros(j)
                                anterior=arrayComp[i]
                            else:
                                if(mudanca==True):
                                    mudanca=False
                                    arrayComp[i]=anterior
                                    # retificacao caso o numero em binario nao tenha o comprimento desejado
                                    if (len(arrayComp[i]) != j):
                                        for h in range(j - len(arrayComp[i])):
                                            arrayComp[i] = "0" + arrayComp[i]
                                else:
                                    #criacao do codigo, transformando para decimal, adicionando 1 unidade e convertendo de volta para binario
                                    arrayComp[i]=decimal_to_binary(binarioToDecimal(anterior)+1)
                                    #retificacao caso o numero em binario nao tenha o comprimento desejado
                                    if(len(arrayComp[i])!=j):
                                        for h in range(j-len(arrayComp[i])):
                                            arrayComp[i]="0"+arrayComp[i]
                                    anterior=arrayComp[i]
                    #caso nao seja a primeira ocorrencia
                    if(anterior!="x"):
                        #criacao do proximo codigo
                        if(encontrou==True):
                            anterior=decimal_to_binary(binarioToDecimal(anterior) + 1)
                        anterior=anterior+"0"
                        mudanca=True
                        encontrou=False
                return arrayComp

            #funcao que guarda os codigos de huffman passados por parametro numa arvore
            def complete_tree(array):
                tree=HuffmanTree()
                for i in range(len(array)):
                    if(array[i]!=False):
                        tree.addNode(array[i],i)
                return tree
            #criacao dos codigos de huffman dos comprimentos
            arrayComprimentosHCLEN=converteComprimentos(arrayHCLEN)
            #criacao da arvore de huffman dos comprimentos
            treeHCLEN=complete_tree(arrayComprimentosHCLEN)
            print("Ponto 3:",arrayComprimentosHCLEN)

            #ex4
            #funcao que le e armazena num array os comprimento dos  códigos referentes ao alfabeto de literais/comprimentos
            def comprimentosHLIT(self,tree,HLIT):
                valor=-1
                contador=0
                arrayHLIT=np.zeros(HLIT+257,np.int16)
                #enquanto o array nao acaba
                while(contador<(HLIT+257)):
                    #enquanto nao chega a uma folha
                    while(valor<0):
                        bit=str(self.readBits(1))
                        valor=tree.nextNode(bit)
                        #print(valor)
                    #se o valor for inferior a 16 é o proprio comprimento
                    if(valor<16):
                        arrayHLIT[contador]=valor
                        contador+=1
                    #se for igual a 16 repete o valor anterior de 3 a 6 vezes
                    elif(valor==16):
                        temp=arrayHLIT[contador-1]
                        for i in range(3+self.readBits(2)):
                            if (contador != HLIT + 257):
                                arrayHLIT[contador]=temp
                                contador += 1
                    # se for igual a 17 repete o valor anterior de 3 a 10 vezes
                    elif(valor==17):
                        for i in range(3 + self.readBits(3)):
                            if(contador!=HLIT+257):
                                arrayHLIT[contador] = 0
                                contador += 1
                    # se for igual a 18 repete o valor anterior de 11 a 138 vezes
                    elif (valor == 18):
                        for i in range(11 + self.readBits(7)):
                            if (contador != HLIT + 257):
                                arrayHLIT[contador] = 0
                                contador += 1
                    #reset do ponteiro da arvore
                    tree.resetCurNode()
                    valor=-1
                return arrayHLIT

            #leitura dos comprimentos dos codigos para os literais
            arrayHLIT= comprimentosHLIT(self,treeHCLEN,HLIT)
            print("Ponto 4:", arrayHLIT)

            #ex5
            #funcao que le e armazena num array os comprimento dos códigos referentes ao alfabeto de literais/comprimentos
            def comprimentosHDIST(self, tree, HDIST):
                valor = -1
                contador = 0
                arrayHDIST = np.zeros(HDIST + 1, np.int16)
                # enquanto o array nao acaba
                while (contador < (HDIST + 1)):
                    # enquanto nao chega a uma folha
                    while (valor < 0):
                        bit = str(self.readBits(1))
                        valor = tree.nextNode(bit)
                        # print(valor)
                    # se o valor for inferior a 16 é o proprio comprimento
                    if (valor < 16):
                        arrayHDIST[contador] = valor
                        contador += 1
                    # se for igual a 16 repete o valor anterior de 3 a 6 vezes
                    elif (valor == 16):
                        temp = arrayHDIST[contador - 1]
                        for i in range(3 + self.readBits(2)):
                            if (contador != HDIST + 1):
                                arrayHDIST[contador] = temp
                                contador += 1
                    # se for igual a 17 repete o valor anterior de 3 a 10 vezes
                    elif (valor == 17):
                        for i in range(3 + self.readBits(3)):
                            if (contador != HDIST + 1):
                                arrayHDIST[contador] = 0
                                contador += 1
                    # se for igual a 18 repete o valor anterior de 11 a 138 vezes
                    elif (valor == 18):
                        for i in range(11 + self.readBits(7)):
                            if (contador != HDIST + 1):
                                arrayHDIST[contador] = 0
                                contador += 1
                    # reset do ponteiro da arvore
                    tree.resetCurNode()
                    valor = -1
                return arrayHDIST

            # leitura dos comprimentos dos codigos para as distancias
            arrayHDIST = comprimentosHDIST(self, treeHCLEN, HDIST)
            print("Ponto 5:", arrayHDIST)

            #ex6
            print("Ponto 6:")
            #conversao dos comprimentos para os codigos de huffman
            arrayCodigoHuffmanHLIT=converteComprimentos(arrayHLIT)
            #criacao da arvore com os codigos anteriores
            treeHLIT=complete_tree(arrayCodigoHuffmanHLIT)
            print("Códigos HLIT:",arrayCodigoHuffmanHLIT)
            # conversao dos comprimentos para os codigos de huffman
            arrayCodigoHuffmanHDIST = converteComprimentos(arrayHDIST)
            # criacao da arvore com os codigos anteriores
            treeHDIST = complete_tree(arrayCodigoHuffmanHDIST)
            print("Códigos HDIST:", arrayCodigoHuffmanHDIST)

            #ex7
            #leitura da arvore das distancias e retorno das distancias conforme a tabela dada no documento do deflate
            def le_bits_HDIST(self,treeHDIST):
                valor=-1
                while(valor<0):
                    bit=str(self.readBits(1))
                    valor=treeHDIST.nextNode(bit)
                treeHDIST.resetCurNode()
                if (valor < 4):
                    distancia=valor+1
                elif (valor < 6):
                    distancia=5+(2*(valor-4))+self.readBits(1)
                elif (valor < 8):
                    distancia = 9 + (4 * (valor - 6)) + self.readBits(2)
                elif (valor < 10):
                    distancia = 17 + (8 * (valor - 8)) + self.readBits(3)
                elif (valor < 12):
                    distancia = 33 + (16 * (valor - 10)) + self.readBits(4)
                elif (valor < 14):
                    distancia = 65 + (32 * (valor - 12)) + self.readBits(5)
                elif (valor < 16):
                    distancia = 129 + (64 * (valor - 14)) + self.readBits(6)
                elif (valor < 18):
                    distancia = 257 + (128 * (valor - 16)) + self.readBits(7)
                elif (valor < 20):
                    distancia = 513 + (256 * (valor - 18)) + self.readBits(8)
                elif (valor < 22):
                    distancia = 1025 + (512 * (valor - 20)) + self.readBits(9)
                elif (valor < 24):
                    distancia = 2049 + (1024 * (valor - 22)) + self.readBits(10)
                elif (valor < 26):
                    distancia = 4097 + (2048 * (valor - 24)) + self.readBits(11)
                elif (valor < 28):
                    distancia = 8193 + (4096 * (valor - 26)) + self.readBits(12)
                elif (valor < 30):
                    distancia = 16385 + (8192 * (valor - 28)) + self.readBits(13)

                return distancia


            #funcao que cria a lista final dos caracteres em ASCII
            def array_final(self, treeHLIT,treeHDIST):
                valor = -1
                contador = 0
                listaFinal=[]
                while(1):
                    #enquanto o valor é menor que 0
                    while(valor<0):
                        bit=str(self.readBits(1))
                        valor=treeHLIT.nextNode(bit)
                    treeHLIT.resetCurNode()
                    # se o valor lido for 256 acabou o bloco
                    if(valor==256):
                        break
                    # se o valor lido for inferior 256 copia o valor para a lista
                    elif(valor<256):
                        listaFinal+=[valor]
                    # se o valor lido for superior 256 retrocede a distancia correspondente
                    # e copia a sequencia com o comprimento correspondente para o fim da lista (algoritmo LZ77)
                    #o calculo do tamanho das sequencias repetidas esta de acordo com a tabela dada no documento do deflate
                    elif(valor>256):
                        if(valor<265):
                            tamanho=valor-254
                            distancia=le_bits_HDIST(self,treeHDIST)
                            len_lista=len(listaFinal)
                            for i in range(tamanho):
                                listaFinal+=[listaFinal[len_lista-distancia+i]]
                        elif(valor<269):
                            tamanho=11+(2*(valor-265))+self.readBits(1)
                            distancia = le_bits_HDIST(self,treeHDIST)
                            len_lista = len(listaFinal)
                            for i in range(tamanho):
                                listaFinal += [listaFinal[len_lista - distancia + i]]
                        elif (valor < 273):
                            tamanho=19+(4*(valor-269))+self.readBits(2)
                            distancia = le_bits_HDIST(self,treeHDIST)
                            len_lista = len(listaFinal)
                            for i in range(tamanho):
                                listaFinal += [listaFinal[len_lista - distancia + i]]
                        elif (valor < 277):
                            tamanho=35+(8*(valor-273))+self.readBits(3)
                            distancia = le_bits_HDIST(self,treeHDIST)
                            len_lista = len(listaFinal)
                            for i in range(tamanho):
                                listaFinal += [listaFinal[len_lista - distancia + i]]
                        elif (valor < 281):
                            tamanho=67+(16*(valor-277))+self.readBits(4)
                            distancia = le_bits_HDIST(self,treeHDIST)
                            len_lista = len(listaFinal)
                            for i in range(tamanho):
                                listaFinal += [listaFinal[len_lista - distancia + i]]
                        elif (valor < 285):
                            tamanho=131+(32*(valor-281))+self.readBits(5)
                            distancia = le_bits_HDIST(self,treeHDIST)
                            len_lista = len(listaFinal)
                            for i in range(tamanho):
                                listaFinal += [listaFinal[len_lista - distancia + i]]
                        elif(valor==285):
                            tamanho=258
                            distancia = le_bits_HDIST(self,treeHDIST)
                            len_lista = len(listaFinal)
                            for i in range(tamanho):
                                listaFinal += [listaFinal[len_lista - distancia + i]]
                    valor=-1
                    #treeHLIT.resetCurNode()
                return listaFinal

            #criacao da lista dos caracteres finais
            lista_final=array_final(self,treeHLIT,treeHDIST)
            print("Ponto 7:",lista_final)

            #ex8
            #funcao que recebe a lista dos caracteres em ASCII e escreve os caracteres num ficheiro passado por parametro
            def escreve_txt(lista_final,file_name):
                file=open(file_name,"w+")
                for i in range(len(lista_final)):
                    file.write(chr(lista_final[i]))
                file.close()

            #escrita no ficheiro final descompactado
            escreve_txt(lista_final,"FAQ.txt")


            # update number of blocks read
            numBlocks += 1

        # close file

        self.f.close()
        print("End: %d block(s) analyzed." % numBlocks)

    def getOrigFileSize(self):
        ''' reads file size of original file (before compression) - ISIZE '''

        # saves current position of file pointer
        fp = self.f.tell()

        # jumps to end-4 position
        self.f.seek(self.fileSize - 4)

        # reads the last 4 bytes (LITTLE ENDIAN)
        sz = 0
        for i in range(4):
            sz += self.f.read(1)[0] << (8 * i)

        # restores file pointer to its original position
        self.f.seek(fp)

        return sz

    def getHeader(self):
        ''' reads GZIP header'''

        self.gzh = GZIPHeader()
        header_error = self.gzh.read(self.f)
        return header_error

    def readBits(self, n, keep=False):
        ''' reads n bits from bits_buffer. if keep = True, leaves bits in the buffer for future accesses '''

        while n > self.available_bits:
            self.bits_buffer = self.f.read(1)[0] << self.available_bits | self.bits_buffer
            self.available_bits += 8

        mask = (2 ** n) - 1
        value = self.bits_buffer & mask

        if not keep:
            self.bits_buffer >>= n
            self.available_bits -= n

        return value


if __name__ == '__main__':

    # gets filename from command line if provided
    filename = "FAQ.txt.gz"
    if len(sys.argv) > 1:
        fileName = sys.argv[1]

    # decompress file
    gz = GZIP(filename)
    gz.decompress()
