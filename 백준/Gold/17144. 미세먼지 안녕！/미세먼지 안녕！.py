import sys
input = sys.stdin.readline
R,C,T = map(int,input().split())
gong = []
board = []
dir = [(0,1),(0,-1),(1,0),(-1,0)]
for y in range(R):
    line = [int(x) for x in map(int,input().split())]
    for x in range(C):
        if line[x] == -1: gong.append(y)
    board.append(line)
upY,dnY = gong[0],gong[1]

for _ in range(T):
    tmp = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if board[y][x] >= 5:
                val = board[y][x] // 5
                for dy,dx in dir:
                    ny,nx = y+dy,x+dx
                    if 0<=ny<=R-1 and 0<=nx<=C-1 and board[ny][nx] != -1:
                        tmp[ny][nx] += val
                        tmp[y][x] -= val
    for y in range(R):
        for x in range(C):
            board[y][x] += tmp[y][x]

    curY,curX = upY,0
    dir1 = [(-1,0),(0,1),(1,0),(0,-1)]
    move_cmd = 0
    while True:
        if curY == upY and curX == 1:
            board[curY][curX] = 0
            board[curY][curX-1] = -1
            break
        ny,nx = curY + dir1[move_cmd][0], curX+dir1[move_cmd][1]
        if 0<=ny<=upY and 0<=nx<=C-1:
            board[ny][nx],board[curY][curX] = board[curY][curX],board[ny][nx]
            curY,curX = ny,nx
        else: move_cmd += 1

    curY,curX = dnY,0
    dir2 = [(1,0),(0,1),(-1,0),(0,-1)]
    move_cmd = 0
    while True:
        if curY == dnY and curX == 1:
            board[curY][curX] = 0
            board[curY][curX-1] = -1
            break
        ny,nx = curY + dir2[move_cmd][0], curX+dir2[move_cmd][1]
        if dnY<=ny<=R-1 and 0<=nx<=C-1:
            board[ny][nx],board[curY][curX] = board[curY][curX],board[ny][nx]
            curY,curX = ny,nx
        else: move_cmd += 1

ans = 0
for y in range(R):
    for x in range(C):
        if board[y][x] != -1: ans += board[y][x]
print(ans)