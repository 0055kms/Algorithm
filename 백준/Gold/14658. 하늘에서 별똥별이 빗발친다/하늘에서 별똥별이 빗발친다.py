import sys; input = sys.stdin.readline
from itertools import product
N,M,L,K = map(int,input().split())
ans = sys.maxsize
stars = []
for _ in range(K):
    x,y = map(int,input().split())
    stars.append((x,y))
for z1,z2 in product(stars,repeat = 2):
    minX,minY = min(z1[0],z2[0]),min(z1[1],z2[1])
    maxX,maxY = minX + L , minY + L
    tmp = 0
    for x,y in stars:
        if minY <= y <= maxY and minX <= x <= maxX:
            tmp += 1
    ans = min(K-tmp,ans)
print(ans)