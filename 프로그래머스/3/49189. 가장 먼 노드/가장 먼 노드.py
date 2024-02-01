from collections import deque
def solution(n, edge):
    ans = 0
    Visited = [False] * (n+1)
    D = [0] * (n+1)
    Elist = [[] for _ in range(n+1)]
    for s,e in edge:
        Elist[s].append(e)
        Elist[e].append(s)
    
    q = deque([1])
    Visited[1] = True
    while q:
        now = q.popleft()
        for i in Elist[now]:
            if not Visited[i]:
                Visited[i] = True
                D[i] = D[now] + 1
                q.append(i)
    max_val = max(D)
    for i in D[1:]:
        if i == max_val: ans += 1
    return ans