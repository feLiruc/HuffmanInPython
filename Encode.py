from itertools import groupby
from heapq import *

# Node para abstração dos nós da heap que vai ser gerada
class Node(object):
    esquerda = None
    direita = None
    dado = None
    peso = 0

    # Metódo construtor pro object Node iniciando dado e peso de cada nó
    def __init__(self, d, p):
        self.dado = d
        self.peso = p

    # Método para setar os nós filhos(esquerdo e direito) de cada nó da pilha
    def setChildren(self, ne, nd):
        self.esquerda = ne
        self.direita = nd

    # Método sobreposto pra visualização das informações(print) dentro do nó
    def __repr__(self):
        return "Dado: "+str(self.dado)+" - Peso: "+str(self.peso)+" - esquerda: "+str(self.esquerda)+" - direita: "+str(self.direita)+"\n"

    # Implementaçã de sobrecarga de método LESS THAN necessaria pra verificação da queue no Python3
    def __lt__(self, other):
        return self.peso < other.peso

def Huffman(input, nomeArquivo):
    itemqueue =  [Node(a,len(list(b))) for a,b in groupby(sorted(input))]
    itemqueue = sorted(itemqueue,reverse=True)
    while len(itemqueue) > 1:
        e = heappop(itemqueue)
        d = heappop(itemqueue)
        n = Node(None, d.peso+e.peso)
        n.setChildren(e,d)
        heappush(itemqueue, n)

    codes = {}

    def codeIt(s, node):
        if node.dado:
            if not s:
                codes[node.dado] = "0"
            else:
                codes[node.dado] = s
        else:
            codeIt(s+"0", node.esquerda)
            codeIt(s+"1", node.direita)

    codeIt("",itemqueue[0])

    try:
        f = open(nomeArquivo+".enc", 'w')
        f.write(str(codes)+"\n")
        f.write("".join([codes[a] for a in input]))
        f.close()
    except:
        print("Erro ao abrir arquivo, tente novamente")
