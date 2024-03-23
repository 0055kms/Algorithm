import sys
from copy import deepcopy
input = sys.stdin.readline
result = 0
N = int(input())
B = [[*map(int,input().split())] for _ in range(N)]

def move(board,cmd): #보드 반환함
    if cmd == 0: #위
        for x in range(N):
            ptr = 0
            for y in range(1,N):
                if board[y][x]:
                    tmp = board[y][x]
                    board[y][x] = 0
                    if board[ptr][x] == 0:
                        board[ptr][x] = tmp
                    elif board[ptr][x] == tmp:
                        board[ptr][x] = 2*tmp
                        ptr += 1
                    else:
                        ptr += 1
                        board[ptr][x] = tmp
    elif cmd == 1: #아래
        for x in range(N):
            ptr = N-1
            for y in range(N-2,-1,-1):
                if board[y][x]:
                    tmp = board[y][x]
                    board[y][x] = 0
                    if board[ptr][x] == 0:
                        board[ptr][x] = tmp
                    elif board[ptr][x] == tmp:
                        board[ptr][x] = 2*tmp
                        ptr -= 1
                    else:
                        ptr -= 1
                        board[ptr][x] = tmp
    elif cmd == 2: #오른쪽
        for y in range(N):
            ptr = 0
            for x in range(1,N):
                if board[y][x]:
                    tmp = board[y][x]
                    board[y][x] = 0
                    if board[y][ptr] == 0:
                        board[y][ptr] = tmp
                    elif board[y][ptr] == tmp:
                        board[y][ptr] = 2*tmp
                        ptr += 1
                    else:
                        ptr += 1
                        board[y][ptr] = tmp
    else: #왼쪽
        for y in range(N):
            ptr = N-1
            for x in range(N-2,-1,-1):
                if board[y][x]:
                    tmp = board[y][x]
                    board[y][x] = 0
                    if board[y][ptr] == 0:
                        board[y][ptr] = tmp
                    elif board[y][ptr] == tmp:
                        board[y][ptr] = 2*tmp
                        ptr -= 1
                    else:
                        ptr -= 1
                        board[y][ptr] = tmp
    return board

def dfs(board,depth):
    global result
    if depth == 5:
        tmp_result = max(map(max,board))
        result = max(tmp_result,result)
        return
    else:
        for i in range(4):
            tmp_board = move(deepcopy(board),i)
            dfs(tmp_board,depth+1)
dfs(B,0)
print(result)