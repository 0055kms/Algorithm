def solution(n, costs):
    parent = [x for x in range(n)]
    def find(a):
        if a != parent[a]: parent[a] = find(parent[a])
        return parent[a]
    def union(a,b):
        a,b=find(a),find(b)
        parent[b] = a
    
    costs.sort(key = lambda x: x[2], reverse = True)
    ans = 0
    cnt = 0
    while cnt < n-1:
        s,e,w = costs.pop()
        if find(s) != find(e):
            ans += w
            cnt += 1
            union(s,e)
    
    return ans