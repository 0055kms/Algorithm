import sys
input = sys.stdin.readline
from collections import defaultdict
N,L = map(int,input().split())
dicts = [defaultdict(int) for _ in range(L)]
for _ in range(N):
    S = input().rstrip()
    for i in range(L):
        dicts[i][S[i]] += 1
ans = 0
for i in range(L):
    dict = dicts[i]
    A = list(dict.items())
    A.sort(key = lambda x: (-x[1],x[0]))
    ans += (N-A[0][1])
    print(A[0][0],end='')
print()
print(ans)