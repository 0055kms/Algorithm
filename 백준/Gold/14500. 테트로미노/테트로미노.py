import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
dir = ((-1,0),(1,0),(0,-1),(0,1))

ans = -float("inf")

def dfs(x,y,tmp_ans,d):
    global ans
    if d == 3:
        ans = max(tmp_ans,ans)
        return
    for dx,dy in dir:
        nx ,ny = dx+x,dy+y
        if 0<=nx<=N-1 and 0<=ny<=M-1 and not visit[nx][ny]:
            visit[nx][ny] = True
            dfs(nx,ny,tmp_ans+board[nx][ny],d+1)
            visit[nx][ny] = False

    visit[x][y] = False

def T(x,y):
    global ans
    for g in range(4):
        tdir = []
        for l in range(4):
            if l != g: tdir.append(dir[l])

        tmp_ans = board[x][y]
        for dx,dy in tdir:
            nx,ny = x+dx,y+dy
            if not (0<=nx<=N-1 and 0<=ny<=M-1): break
            else: tmp_ans += board[nx][ny]
        ans = max(tmp_ans,ans)


N,M = map(int,input().split())
board = [[x for x in map(int,input().split())] for _ in range(N)]
visit = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visit[i][j] = True
        dfs(i,j,board[i][j],0)
        visit[i][j] = False
        T(i,j)
print(ans)
"""
dfs로 탐색
깊이 3 될 시 ans = max(ans,tmp_ans)
조건 : 칸범위, 방문
tmp_ans 에 값추가

T모양 가운데 기준 dir에서 하나씩 제외하고 방문
if 불가능: return
else: tmp_ans 에 값 저장
세개 모두 다함 -> 업데이트
"""