import sys
input = sys.stdin.readline
from itertools import product
nList = list(product(['1','2','3','4','5','6','7','8','9'],repeat = 3))
nList = [x for x in nList if not (x[0] == x[1] or x[1] == x[2] or x[0] == x[2])]

def compare(qes,s,b):
    global nList
    new = []
    for i,v in enumerate(nList):
        ts,tb = 0,0
        for j in range(3):
            if v[j] == qes[j]: ts +=1
            elif v[j] in qes: tb += 1
        if ts == s and tb == b: new.append(v);
    nList = new

N = int(input())
for _ in range(N):
    qes , s, b = map(int,input().split())
    compare(str(qes),s,b)
print(len(nList))