import sys
input = sys.stdin.readline
n = int(input())
k = [[*map(int,input().split())]for _ in range(n)]
k.sort(key=lambda x: x[0])
k = [x[1] for x in k]
D = [1] * n
for i in range(1,n):
    for j in range(i):
        if k[i] > k[j]: D[i] = max(D[i],D[j]+1)
print(n-max(D))