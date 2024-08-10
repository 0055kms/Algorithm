import sys
from collections import deque
input = sys.stdin.readline
dir = ((-1,0),(1,0),(0,-1),(0,1))
start = [] #도연
ans = 0 #마지막에 0일 시 TT
N,M = map(int,input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    row = input().rstrip()
    for j in range(M):
        board[i][j] = row[j]
        if row[j] == 'X': visit[i][j] = 1
        if row[j] == 'I': start = [i,j]
q = deque(); q.append(start)
visit[start[0]][start[1]] = 1
while q:
    curx,cury = q.popleft()
    for dx,dy in dir:
        nx,ny = curx+dx , cury+dy
        if not (0<=nx<=N-1 and 0<=ny<=M-1) or visit[nx][ny] == 1 : continue
        if board[nx][ny] == 'P': ans += 1
        visit[nx][ny] = 1
        q.append([nx,ny])
if not ans: ans = "TT"
print(ans)
