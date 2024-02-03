import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

R, C = map(int, input().split())
Visited = [[False] * C for _ in range(R)]

for y in range(R):
    line = input().rstrip()
    for x in range(C):
        if line[x] == 'x':
            Visited[y][x] = True

dir = [(-1, 1), (0, 1), (1, 1)]
ans = 0

def dfs(nowy, nowx):
    if nowx == C - 1:
        return True
    for dy, dx in dir:
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < R and 0 <= nx < C and not Visited[ny][nx]:
            Visited[ny][nx] = True  
            if dfs(ny, nx):  
                return True
    return False

for sy in range(R):
    if dfs(sy, 0):  
        ans += 1

print(ans)
