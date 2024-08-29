import sys
input = sys.stdin.readline
from heapq import *
dir = [(-1,0),(1,0),(0,-1),(0,1)]
C,R = map(int,input().split())
A = [[*map(int,input().rstrip())] for _ in range(R)]
D = [[float("inf")] * C for _ in range(R)]
D[0][0] = 0
q = []
heappush(q,(0,(0,0)))
while q:
    cur_d , cur_p = heappop(q)
    for dx,dy in dir:
        nx,ny = cur_p[0] + dx,cur_p[1]+dy
        if not (0<=nx<=R-1 and 0<=ny<=C-1): continue
        if cur_d + A[nx][ny] >= D[nx][ny]: continue
        D[nx][ny] = cur_d + A[nx][ny]
        heappush(q,(D[nx][ny],(nx,ny)))
print(D[-1][-1])