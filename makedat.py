import random

processionA=[]
processionB=[]
N = 1000
for i in range(N):
    processionA.append(list())
    processionB.append(list())
    for j in range(N):
        processionA[i].append(random.randint(1, 99))
        processionB[i].append(random.randint(1, 99))

with open('a.dat', 'w') as file:
    for i in range(N):
        for a in processionA[i]:
            file.write(str(a) + ' ')
        file.write('\n')

with open('b.dat', 'w') as file:
    for i in range(N):
        for b in processionB[i]:
            file.write(str(b) + ' ')
        file.write('\n')
