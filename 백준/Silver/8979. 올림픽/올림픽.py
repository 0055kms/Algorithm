import sys
input = sys.stdin.readline
N,K = map(int,input().split())
ar = []
for _ in range(N):
    tmp = [x for x in map(int,input().split())]
    if tmp[0] == K: ans = tmp[1:]
    ar.append(tmp[1:])
ar.sort(key = lambda x: (x[0],x[1],x[2]),reverse = True)
for i in range(len(ar)):
    if ar[i] == ans: print(i+1); break