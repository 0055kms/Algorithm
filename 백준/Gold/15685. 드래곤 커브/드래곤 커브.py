import sys
input = sys.stdin.readline
dir = [(0,1),(-1,0),(0,-1),(1,0)]
graph = [[0] * 101 for _ in range(101)]
N = int(input())
ans = 0
for _ in range(N):
    x,y,d,g = map(int,input().split())
    curve = [d]
    graph[y][x] = 1
    for _ in range(g):
        tmp_curve = []
        for i in curve: tmp_curve.append((i+1)%4)
        tmp_curve = tmp_curve[::-1]
        curve.extend(tmp_curve)
    for k in curve:
        y,x = y+dir[k][0] , x + dir[k][1]
        graph[y][x] = 1
for sy in range(100):
    for sx in range(100):
        if graph[sy][sx] and graph[sy][sx+1] and\
                graph[sy+1][sx] and graph[sy+1][sx+1]:
            ans += 1
print(ans)