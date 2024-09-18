import sys
input = sys.stdin.readline
dir = [(-1,0),(0,1),(1,0),(0,-1)] #북동남서
R,C = map(int,input().split())
sx,sy,sd = map(int,input().split())
A = [[x for x in map(int,input().split())] for _ in range(R)]
ans = 0
"""
if 현재칸 0:
    현재 칸 2로
    ans += 1
if 주변 4칸 청소 불가능
    if 후진가능
        한칸후진
        처음으로 돌아감
    else
        멈춤!
else
    while True:
        반시계 방향 회전
        if 앞쪽 청소 가능:
            한칸전진
            처음으로 돌아감
"""
def f(x,y,d):
    global ans
    if A[x][y] == 0:
        A[x][y] = 2
        ans += 1
    flag = False #True면 주변 청소 가능
    for _ in range(4):
        d = (d-1)%4
        dx,dy = dir[d]
        nx,ny = x+dx,y+dy
        if 0<=nx<=R-1 and 0<=ny<=C-1 and A[nx][ny] == 0:
            flag = True
            f(nx,ny,d)
            break
    if not flag:
        dd = (d+2)%4
        dx,dy = dir[dd]
        nx,ny = x+dx,y+dy
        if 0<=nx<=R-1 and 0<=ny<=C-1 and A[nx][ny] != 1:
            f(nx,ny,d)
        else:
            print(ans)
            sys.exit()
f(sx,sy,sd)