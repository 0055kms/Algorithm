from collections import deque

def solution(n, computers):
    Elist = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                Elist[i].append(j)
                
    visit = [False] * n
    answer = 0
    
    def bfs(x):
        q = deque([x])
        visit[x] = True
        while q:
            now = q.popleft()
            for next in Elist[now]:
                if not visit[next]:
                    visit[next] = True
                    q.append(next)

    for i in range(n):
        if not visit[i]:
            answer += 1
            bfs(i)
    print(Elist)
    return answer