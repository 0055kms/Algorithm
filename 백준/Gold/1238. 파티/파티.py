import sys
input = sys.stdin.readline
from heapq import *

N,M,X = map(int,input().split()) #마을 수, 도로 수, 출발 마을 번호
Elist = [[] for _ in range(M+1)]
Rlist = [[] for _ in range(M+1)]
for _ in range(M):
    s,e,w = map(int,input().split())
    Elist[s].append((e,w))
    Rlist[e].append((s,w))
def dijkstra(start):
    D = [float("inf")] * (N+1)
    D[start] = 0
    q = []; heappush(q,(start,D[start]))
    while q:
        cur_n,cur_d = heappop(q)
        for next_n,new_d in Elist[cur_n]:
            next_d = cur_d + new_d
            if next_d < D[next_n]:
               D[next_n] = next_d
               heappush(q,(next_n,next_d))
    return D

def dijkstra2(start):
    D = [float("inf")] * (N+1)
    D[start] = 0
    q = []; heappush(q,(start,D[start]))
    while q:
        cur_n,cur_d = heappop(q)
        for next_n,new_d in Rlist[cur_n]:
            next_d = cur_d + new_d
            if next_d < D[next_n]:
               D[next_n] = next_d
               heappush(q,(next_n,next_d))
    return D

ans = 0
go = dijkstra(X)
come = dijkstra2(X)
for i in range(1,N+1):

    ans = max(go[i]+come[i],ans)
print(ans)