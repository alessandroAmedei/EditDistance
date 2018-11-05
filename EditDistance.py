import math

import numpy as np

class EditDistance():

    def __init__(self):
        self.cost=1
        self.copy=0


    def compute(self,x,y):
        m = x.__len__()
        n = y.__len__()
        c = np.zeros((m+1,n+1))
        op = np.zeros((m+1,n+1))

        for i in range(0,m+1):
            c[i,0] = i*self.cost
            op[i,0] = 3
        for j in range (0,n+1):
            c[0,j] = j*self.cost
            op[0,j] = 4

        for i in range (1,m+1):
            for j in range (1,n+1):
                c[i,j] = math.inf
                if x[i-1] == y[j-1]:
                    c[i,j]=c[i-1,j-1]+ self.copy
                    op[i,j]=0
                if x[i-1] != y[j-1] and (c[i-1,j-1]+self.cost) < c[i,j]:
                     c[i,j]=c[i-1,j-1]+self.cost
                     op[i,j] = 1
                if i>=2 and j>=2 and (x[i-1]==y[j-2]) and (x[i-2]==y[j-1]) and (c[i-2,j-2] + self.cost < c[i,j]):
                    c[i,j] = c[i-2,j-2] + self.cost
                    op[i,j] = 2
                if c[i-1,j] + self.cost < c[i,j]:
                    c[i,j] = c[i-1,j] + self.cost
                    op[i,j] = 3
                if c[i,j-1] + self.cost < c[i,j]:
                    c[i,j] = c[i,j-1] + self.cost
                    op[i,j] = 4

        return c

    # COPY:0 REPLACE:1 TWIDDLE:2 DELETE:3 INSERT:4


    def OpSequence(self,op,i,j):
        j2=None
        i2=None
        if i==0 and j==0:
            return
        if op[i,j]==0 or op[i,j]==1:
            i2=i-1
            j2=j-1
        elif op[i,j]==2:
            i2=i-2
            j2=i-2
        elif op[i,j]==3:
            i2=i-1
            j2=j
        elif op[i,j]==4:
            i2=i
            j2=j-1
        self.OpSequence(op,i2,j2)
        print(op[i,j])


class ngramObject:
    def __init__(self,word):
        self.word=word
        self.ngramList=[]
    def append(self,igram):
        self.ngramList.append(igram)


class ngramFunction:
    'Mi serve una function che passandogli una parola e un dizionario e un numero, mi restituisca tutte le parole i quali ngram si intersecavano (di almeno due) con quelli della parola'

    def dizionario_to_ngrams(self,dizionario,n):
        ngrams=[]
        for i in range (0,dizionario.__len__()):
            word = dizionario[i]
            ngo = ngramObject(word)
            for j in range(0,word.__len__()-n+1):
                ngo.append(word[j:j+n])
            ngrams.append(ngo)
        return ngrams

    def word_to_ngrams(self,word,n):
        ngo = ngramObject(word)
        for j in range(0,word.__len__()-n+1):
            ngo.append(word[j:j+n])
        return ngo

    def make_subDitionary_ngram(self,dizionario,word,n,m):
        ngo= self.dizionario_to_ngrams(dizionario,n)
        ngw= self.word_to_ngrams(word,n)
        'Qui bissogna aggiungere ngo in subDitionary se matcha!'
        for i in range(0,ngo.__len__()):
            ngw2 = ngo[i].ngramList





def dizionario(nome_file):
        lessico = []
        with open(nome_file, 'r') as f:
            for line in f:
                for word in line.split():
                    lessico.append(word)
        return lessico




dizionario = dizionario("60000.txt")
a = ngramFunction().dizionario_to_ngrams(dizionario,3)
print('try')
'''

ed = EditDistance()

for i in range(0,a.__len__()):
    c = ed.compute(x,a[i])
    if(c[x.__len__(),a[i].__len__()] < 3):
        print(a[i])

'''








