import sys
input = sys.stdin.readline
"""
왼쪽 -> 자신 -> 오른쪽 -> 부모
              1
            2 1 2              d = 2
        3 2 3 1 3 2 3          d = 3
4 3 4 2 4 3 4 1 4 3 4 2 4 3 4  d = 4
"""
K = int(input())
data = [x for x in map(int,input().split())]

ptrn = [1]
for _ in range(K-1):
    new_ptrn = []
    for p in ptrn:
        new_ptrn.append(p+1)
    new_ptrn.append(1)
    for p in ptrn:
        new_ptrn.append(p+1)
    ptrn = new_ptrn
for i in range(len(ptrn)):
    ptrn[i] -= 1
ans = [[] for _ in range(K)]

for i,v in enumerate(ptrn):
    ans[v].append(data[i])
for a in ans:
    print(*a)