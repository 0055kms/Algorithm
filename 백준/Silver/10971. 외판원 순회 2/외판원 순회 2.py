import sys
input = sys.stdin.readline
N = int(input())
W = [[x for x in map(int,input().split())] for _ in range(N)]
ans = float("inf")
for i in range(N):
    for j in range(N):
        if W[i][j] == 0: W[i][j] = float("inf")

def dfs():
    global ans
    if len(tmp) == N:
        tmp_ans = W[tmp[N-1]][tmp[0]]
        for i in range(N-1):
            tmp_ans += W[tmp[i]][tmp[i+1]]
        ans = min(ans,tmp_ans)
        return
    for i in range(N):
        if not visit[i]:
            tmp.append(i); visit[i] = True
            dfs()
            tmp.pop(); visit[i] = False

for start in range(N):
    tmp = [start]
    visit = [False] * N
    visit[start] = True
    dfs()
print(ans)