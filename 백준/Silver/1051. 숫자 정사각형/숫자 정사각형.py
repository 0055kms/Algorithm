import sys
input = sys.stdin.readline
N,M = map(int,input().split())
ar = []
for _ in range(N):
    ar.append([*map(int,input().rstrip())])


for l in range(min(N,M)-1,-1,-1):
    for sx in range(0,N-l):
        for sy in range(0,M-l):
            if ar[sx][sy] == ar[sx+l][sy] and ar[sx][sy] == ar[sx][sy+l] and ar[sx][sy] == ar[sx+l][sy+l]:
                print((l+1)**2)
                sys.exit()
