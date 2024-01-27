import sys
input = sys.stdin.readline
from queue import PriorityQueue
from collections import deque
rows,cols = map(int,input().split())
dir = [(0,1),(0,-1),(1,0),(-1,0)]
Graph = [[0]*cols for _ in range(rows)]
Visited = [[False]*cols for _ in range(rows)]
for y in range(rows):
    line = [*map(int,input().split())]
    for x in range(cols):
        Graph[y][x] = line[x]

l = []
def mark(y,x,markn):
    q = deque()
    q.append((y,x))
    Visited[y][x] = True
    Graph[y][x] = markn
    while q:
        ny,nx = q.popleft()
        for dy,dx in dir:
            if 0 <= ny+dy <= rows-1 and 0 <= nx + dx <= cols-1\
                and not Visited[ny+dy][nx+dx] and Graph[ny+dy][nx+dx] !=0 :
                Visited[ny+dy][nx+dx] = True
                Graph[ny+dy][nx+dx] = markn
                q.append((ny+dy,nx+dx))
markn = 1
for y in range(rows):
    for x in range(cols):
        if not Visited[y][x] and Graph[y][x] == 1:
            mark(y,x,markn)
            markn += 1

pq = PriorityQueue()
def make(y,x):
    originmark = Graph[y][x]
    for dy,dx in dir:  #4방향 각각 한방향으로 bfs
        cnt = 0
        q = deque()
        q.append((y,x))
        while q:
            ny,nx = q.popleft()
            if Graph[ny][nx] != 0 and Graph[ny][nx] != originmark:
                if cnt-1 >= 2: pq.put((cnt-1,originmark,Graph[ny][nx]))
                break
            if 0<=ny+dy<=rows-1 and 0<=nx+dx<=cols-1 and Graph[ny+dy][nx+dx] != originmark:
                q.append((ny+dy,nx+dx))
                cnt += 1
for y in range(rows):
    for x in range(cols):
        if Graph[y][x] != 0: make(y,x)

#1부터 markn-1개 있다
Parent = [x for x in range(markn)]
def find(a):
    if a == Parent[a]: return a
    else:
        Parent[a] = find(Parent[a])
        return Parent[a]
def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b: Parent[b] = a

cnt2 = 0
result = 0
while cnt2 < markn-2 and pq.qsize() > 0:
    w,s,e = pq.get()
    if find(s) != find(e):
        union(s,e)
        cnt2 +=1
        result += w
if cnt2 == markn-2: print(result)
else: print(-1)