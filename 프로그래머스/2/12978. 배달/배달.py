def solution(N, road, K):
    ans = 0
    inf = float("inf")
    D = [[inf] * (N+1) for _ in range(N+1)]
    D[1][1] = 0
    for s,e,w in road:
        D[s][e] = min(D[s][e],w)
        D[e][s] = min(D[e][s],w)
        
    for k in range(N+1):
        for s in range(N+1):
            for e in range(N+1):
                D[s][e] = min(D[s][e],D[s][k] + D[k][e])
    for i in D[1][1:]:
        if i <= K: ans +=1
    return ans
        
    