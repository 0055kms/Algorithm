import sys
from math import ceil
input = sys.stdin.readline
N,need = map(int,input().split())
wood = [x for x in map(int,input().split())]
s,e = 0,max(wood)
while s<=e:
    m = (s+e)//2
    get = 0
    for w in wood:
        if w>=m: get += (w-m)
    if get>= need: s = m +1
    else: e = m -1
print(s-1)