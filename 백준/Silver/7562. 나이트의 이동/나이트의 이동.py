import sys
input = sys.stdin.readline
from collections import deque
dir = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

T = int(input())
for _ in range(T):
    l = int(input())
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())
    B = [[float("inf") for _ in range(l)] for _ in range(l)] #현재 위치가 최소 몇번만에 도착가능한지
    B[sx][sy] = 0
    q = deque(); q.append((sx,sy))
    while q:
        x,y = q.popleft()
        for dx,dy in dir:
            nx,ny = x+dx,y+dy
            if 0<=nx<=l-1 and 0<=ny<=l-1 and B[x][y] + 1 < B[nx][ny]:
                B[nx][ny] = B[x][y] + 1
                q.append((nx,ny))
    print(B[ex][ey])

