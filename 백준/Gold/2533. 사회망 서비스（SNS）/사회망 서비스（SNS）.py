import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**7)

def dfs(n):
    visited[n] = True
    for next in graph[n]:
        if visited[next]: continue
        else:
            visited[next] = True
            dfs(next)
            dp[n][0] += dp[next][1]
            dp[n][1] += min(dp[next])
    return


if __name__ == '__main__':
    N = int(input())
    dp = [[0,1] for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(N-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    dfs(1)
    print(min(dp[1]))



"""
dp[노드넘버][얼리유무] = 얼리유무 일때 노드넘버까지의 최소 얼리어답터 수
dp[현재노드][False] = dp[이전노드][True] 들의 합
dp[현재노드][true] = min(dp[이전노드]) 들의 합 
"""