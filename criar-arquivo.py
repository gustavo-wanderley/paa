import random
def create_file():
    v = []
    for i in range(10000):
        v.append(i)
    random.shuffle(v)
    f = open('desordenado.txt','w+')
    for x in range(10000):
        f.write(str(v[x]) + '\n')
    f.close()
create_file()