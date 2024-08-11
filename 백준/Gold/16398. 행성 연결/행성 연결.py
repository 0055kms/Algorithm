import sys
input = sys.stdin.readline
from heapq import *
N = int(input())
edges = []

if (N == 1): print(0); sys.exit()
for i in range(N):
    row = [*map(int,input().split())]
    for j in range(N):
        if i!=j: heappush(edges,(row[j],i,j))

parent = [x for x in range(N)]
def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b: parent[b] = a
def find(a):
    if a != parent[a]: parent[a] = find(parent[a])
    return parent[a]

ans = 0
tmp = 0
while True:
    w,s,e = heappop(edges)
    if find(s) == find(e): continue
    union(s,e)
    tmp += 1
    ans += w
    if tmp == N-1: break
print(ans)
