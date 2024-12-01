from collections import deque

def solution(n, edge):
    answer = 0
    D = [-1] * n
    D[0] = 0
    Elist = [[] for _ in range(n)]
    for s,e in edge:
        Elist[s-1].append(e-1)
        Elist[e-1].append(s-1)
    
    q = deque([0])
    while q:
        cur = q.popleft()
        for n in Elist[cur]:
            if D[n] == -1:
                D[n] = D[cur] + 1
                q.append(n)
    m = max(D)
    for i in D:
        if i == m: answer += 1
    return answer