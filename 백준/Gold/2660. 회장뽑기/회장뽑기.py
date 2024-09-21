import sys
input = sys.stdin.readline
N = int(input())
D = [[float("inf")]*N for _ in range(N)]
for i in range(N):
    D[i][i] = 0
while True:
    s,e = map(int,input().split())
    if s == -1 and e == -1: break
    s-=1; e-=1
    D[s][e] = 1
    D[e][s] = 1
for k in range(N):
    for s in range(N):
        for e in range(N):
            D[s][e] = min(D[s][e],D[s][k]+D[k][e])
MIN = float("inf")
for i in range(N):
    MIN = min(MIN,max(D[i]))
ans = []
for i in range(N):
    if max(D[i]) == MIN: ans.append(i+1)
ans.sort()
print(MIN,len(ans))
print(*ans)