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
