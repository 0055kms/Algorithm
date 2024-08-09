import sys
from collections import deque
input = sys.stdin.readline
dir = ((-1,0),(1,0),(0,-1),(0,1))
R,C = map(int,input().split())
ar = [[0 for _ in range(C)] for _ in range(R)] #숲
visit = [[0 for _ in range(C)] for _ in range(R)] #도착 시간
q = deque()
for i in range(R):
    row = input().strip()
    for j in range(C):
        ar[i][j] = row[j]
        if row[j] == '*': q.appendleft((i,j)); visit[i][j] = 1
        if row[j] == 'S': q.append((i,j)); visit[i][j] = 1
ans = -100
while q:
    curx,cury = q.popleft()
    for dx,dy in dir:
        nx ,ny = dx+curx , dy + cury
        if not (0<=nx<=R-1 and 0<=ny<=C-1): continue
        if visit[nx][ny] or ar[nx][ny] == 'X': continue
        if ar[nx][ny] == 'D' and ar[curx][cury] == 'S': ans = visit[curx][cury] + 1; break
        if ar[nx][ny] == 'D' and ar[curx][cury] == '*': continue
        if ar[nx][ny] == '*' and ar[curx][cury] == 'S': continue
        q.append((nx,ny))
        visit[nx][ny] = visit[curx][cury] + 1
        ar[nx][ny] = ar[curx][cury]
    if ans != -100:
        break
print(ans-1 if ans != -100 else "KAKTUS")




