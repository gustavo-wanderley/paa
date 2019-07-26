import os
def insertion_sort(A): 
    for i in range(1, len(A)):  
        key = A[i] 
        j = i-1
        while j >=0 and key < A[j] : 
                A[j+1] = A[j] 
                j -= 1
        A[j+1] = key 

def merge():
    cont = 1
    pos = 0
    k = 0
    V = []
    overLimit = 1000
    belowLimit = 0
    while k < 10:
        with open('desordenado.txt','r+') as f:
            while True:
                n = f.readline()
                if n:
                    n = int(n)
                    if n < overLimit  and n >= belowLimit:
                        V.append(n)
                        if cont % 1000 == 0:
                            nameTemp = 'temp'+str(pos)+'.txt'
                            insertion_sort(V)
                            l = open(nameTemp, 'w+')
                            for j in range(1000):
                                line = str(V[j])+'\n'
                                l.write(line)
                            l.close()
                            pos = pos + 1
                            V = []
                            overLimit = overLimit + 1000
                            belowLimit = belowLimit + 1000
                        cont = cont + 1
                else:
                    break
        k = k + 1

def file_final():
    V = []
    t = 0
    fi = open('ordenado.txt','w+')
    while t < 10:
        nameTemp = 'temp'+str(t)+'.txt'
        with open(nameTemp, 'r+') as f:
            while True:
                n = f.readline()
                if n:
                    V.append(int(n))
                else: 
                    break
        os.remove(nameTemp)
        for i in range(len(V)):
            fi.write(str(V[i])+'\n')
            
        V = []
        t = t + 1
    fi.close()
    
merge()
file_final()