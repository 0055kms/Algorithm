import sys
input = sys.stdin.readline
N = int(input())
board = [[*input().rstrip()] for _ in range(N)]
g_ans = 0
s_ans = 0

for x in range(N):
    l = 0
    for y in range(N):
        if board[x][y] == '.': l +=1
        else: l = 0
        if l == 2: g_ans += 1

for y in range(N):
    l = 0
    for x in range(N):
        if board[x][y] == '.': l += 1
        else: l = 0
        if l == 2: s_ans += 1
print(g_ans,s_ans)
