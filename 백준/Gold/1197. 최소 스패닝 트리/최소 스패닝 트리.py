import sys
input = sys.stdin.readline
V,E = map(int,input().split())
El = []
Vcnt = 1
cnt = 0
uf = [x for x in range(V+1)]
for _ in range(E):
    El.append([*map(int,input().split())])
El.sort(key = lambda x: x[2])

def find(a):
    if uf[a] == a: return a
    else:
        uf[a] = find(uf[a])
        return uf[a]

def union(a,b): 
    a = find(a)
    b = find(b)
    if a!=b: uf[b] = a

for s,e,w in El:
    if find(s) == find(e): continue
    else:
        union(s,e)
        Vcnt += 1
        cnt += w
        if Vcnt == V: break
print(cnt)

