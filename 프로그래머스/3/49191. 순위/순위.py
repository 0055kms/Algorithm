from collections import deque
def solution(n, results):
    ans = 0
    nn = n
    Elist = [[] for _ in range(n)]
    Flist = [[] for _ in range(n)]
    for s,e in results:
        Elist[e-1].append(s-1)
        Flist[s-1].append(e-1)
        
    def bfs(x):
        tmp = 1
        nonlocal nn
        visit = [False] * nn
        q = deque([x])
        visit[x] = True
        while q:
            cur = q.popleft()
            for n in Elist[cur]:
                if not visit[n]:
                    visit[n] = True
                    tmp += 1
                    q.append(n)
                    
        visit = [False] * nn
        q = deque([x])
        visit[x] = True
        while q:
            cur = q.popleft()
            for n in Flist[cur]:
                if not visit[n]:
                    visit[n] = True
                    tmp += 1
                    q.append(n)
                    
        if tmp == nn: return True
        else:  return False
        
    for p in range(n):
        if bfs(p):
            print(p) ##
            ans += 1
    return ans