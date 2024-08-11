import sys
from collections import deque
input = sys.stdin.readline
dir =  ((-1,0),(1,0),(0,-1),(0,1))
R,C,K = map(int,input().split())
visit = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            visit[i][j] = 1
ans = []
for i in range(R):
    for j in range(C):
        if not visit[i][j]:
            tmp = 1
            q = deque(); q.append((i,j))
            visit[i][j] = True
            while q:
                curx,cury = q.popleft()
                for dx,dy in dir:
                    nx,ny = curx+dx,cury+dy
                    if not (0<=nx<=R-1 and 0<=ny<=C-1): continue
                    if visit[nx][ny]: continue
                    tmp += 1
                    visit[nx][ny] = True
                    q.append([nx,ny])
            ans.append(tmp)
print(len(ans))
ans.sort()
print(*ans)