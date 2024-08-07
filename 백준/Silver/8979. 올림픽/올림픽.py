import sys
input = sys.stdin.readline
N,K = map(int,input().split())
ar = []
for _ in range(N):
    ar.append([x for x in map(int,input().split())])
ar.sort(key = lambda x: (x[1],x[2],x[3]),reverse = True)
for i in range(len(ar)):
    if ar[i][0] == K: ans = i; ans_tmp = ar[i]; break
for p in ar:
    if p == ans_tmp: ans -= 1
print(ans+1)