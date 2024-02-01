from collections import deque
def solution(N, road, K):
    answer = 0
    Visited = [False] * (N+1)
    D = [0] * (N+1)
    Elist = [[] for _ in range(N+1)]
    for s,e,w in road:
        Elist[s].append((e,w))
        Elist[e].append((s,w))
    for i in range(len(Elist)):
        Elist[i].sort(key = lambda x: x[1])
        
    def bfs(n):
        q = deque([n])
        Visited[n] = True
        while q:
            now = q.popleft()
            for next,d in Elist[now]:
                if not Visited[next]:
                    Visited[next] = True
                    D[next] = D[now] + d
                    q.append(next)
    bfs(1)
    for i in D[1:]:
        if i <= K: answer += 1
    return Elist
    