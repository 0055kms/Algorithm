import sys; input = sys.stdin.readline
ans = 0
N,M = map(int,input().split())
cur_cycle = []
dir = [(-1,0),(1,0),(0,-1),(0,1)]
graph = [[0] * M for _ in range(N)]
cycled = [[0] * M for _ in range(N)]
for x in range(N):
    line = input().rstrip()
    for y in range(M):
        graph[x][y] = line[y]

for x in range(N):
    for y in range(M):
        if not cycled[x][y]:
            cur_cycle.clear()
            nx,ny = x,y
            while True:
                cur_cycle.append((nx, ny))
                if graph[nx][ny] == "U": cmd = 0
                elif graph[nx][ny] == "D": cmd = 1
                elif graph[nx][ny] == "L": cmd = 2
                elif graph[nx][ny] == "R": cmd = 3
                dx,dy = dir[cmd]
                nx,ny = nx+dx , ny+dy
                if cycled[nx][ny]:
                    for kx,ky in cur_cycle:
                        cycled[kx][ky] = 1
                    break

                elif (nx,ny) in cur_cycle:
                    for kx,ky in cur_cycle:
                        cycled[kx][ky] = 1
                    ans += 1
                    break
print(ans)

