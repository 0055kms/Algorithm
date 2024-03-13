import sys
input = sys.stdin.readline
N,M = map(int,input().split())
board = [[0] * N for _ in range(N)]
for y in range(N):
    line = [*map(int,input().split())]
    for x in range(N):
        board[y][x] = line[x]
gu = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
dir = [(),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
dir2 = [(1,1),(1,-1),(-1,1),(-1,-1)]

for _ in range(M):
    dd,ww = map(int,input().split())
    dy,dx = dir[dd][0]*ww,dir[dd][1]*ww
    new_gu = []
    for y,x in gu:
        ny,nx = (y+dy)%N,(x+dx)%N
        board[ny][nx] += 1
        new_gu.append((ny,nx))

    #모든 y x 에 대하여 물복사마법
    for y,x in new_gu:
        for dy2,dx2 in dir2:
            ny,nx = dy2+y,dx2+x
            if 0<=ny<=N-1 and 0<=nx<=N-1 and board[ny][nx]:
                board[y][x] += 1

    gu = []
    for y in range(N):
        for x in range(N):
            if board[y][x] >= 2:
                if not (y,x) in new_gu:
                    gu.append((y,x))
                    board[y][x] -= 2

ans = 0
for y in range(N):
    for x in range(N):
        ans += board[y][x]
print(ans)