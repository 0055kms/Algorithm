import sys
input = sys.stdin.readline
from heapq import *
N,M = map(int,input().split())
edges = []
for _ in range(M):
    s,e,t = map(int,input().split())
    heappush(edges,(t,s,e))

parent = [x for x in range(N+1)]
def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b: parent[b] = a

def find(a):
    if a!=parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

date = 1
while edges:
    t,s,e = heappop(edges)
    if find(s) == find(e) or t != date: break
    date += 1
    union(s,e)

print(date)