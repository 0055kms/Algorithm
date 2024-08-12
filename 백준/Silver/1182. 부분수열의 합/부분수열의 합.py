import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N,S = map(int,input().split())
ar = [x for x in map(int,input().split())]
tmp = []
ans = 0

def dfs(s):
    global ans
    if tmp and sum(tmp) == S: ans += 1
    if len(tmp) == N: return
    for i in range(s,N):
        tmp.append(ar[i])
        dfs(i+1)
        tmp.pop()
dfs(0)
print(ans)