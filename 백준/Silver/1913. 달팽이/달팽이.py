import sys
input = sys.stdin.readline
N = int(input())
U = int(input())
A = [[0 for _ in range(N)] for _ in range(N)]
dir = [(1,0),(0,1),(-1,0),(0,-1)];
d,curx,cury,n = 0,0,0,N**2
A[0][0] = N**2
while True:
    if curx == N // 2 and cury == N // 2: break
    while True: #더 못 가면 break
        dx,dy = dir[d]
        nx,ny = curx+dx,cury+dy
        if curx == N//2 and cury == N//2: break
        if 0<=nx<=N-1 and 0<=ny<=N-1 and A[nx][ny] == 0:
            n -= 1
            A[nx][ny] = n
            curx,cury = nx,ny
        else: break
    d = (d+1)%4
for i in range(N): print(*A[i])
for x in range(N):
    for y in range(N):
        if A[x][y] == U:
            print(x+1,y+1)
            break
