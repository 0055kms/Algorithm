import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
input = sys.stdin.readline
dir = [(0,1),(0,-1),(1,0),(-1,0)]
ans = 0 #max로 업데이트
rows,cols = map(int,input().split())
graph = [[3] * cols for _ in range(rows)]
empty = []
bir = []
for y in range(rows):
    line = [*map(int,input().split())]
    for x in range(cols):
        graph[y][x] = line[x]
        if line[x] == 0: empty.append((y,x))
        elif line[x] == 2: bir.append((y,x))
for s1,s2,s3 in combinations(empty,3):
    tmp_ans = 0
    board = deepcopy(graph)
    board[s1[0]][s1[1]] = 1
    board[s2[0]][s2[1]] = 1
    board[s3[0]][s3[1]] = 1
    q = deque()
    for ss in bir: q.append(ss)
    while q:
        nowy,nowx = q.popleft()
        for dy,dx in dir:
            ny,nx = nowy+dy,nowx+dx
            if 0<=ny<=rows-1 and 0<=nx<=cols-1 and board[ny][nx] == 0:
                board[ny][nx] = 2
                q.append((ny,nx))
    for y in range(rows):
        for x in range(cols):
            if board[y][x] == 0: tmp_ans += 1
    ans = max(ans,tmp_ans)
print(ans)