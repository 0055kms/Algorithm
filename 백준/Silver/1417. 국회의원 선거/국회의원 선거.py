import sys
from heapq import *
N = int(input())
if N == 1: print(0); sys.exit()

ans = 0
dasom = int(input())
hq = []
for _ in range(N-1):
    heappush(hq,-int(input()))
while -hq[0] >= dasom:
    now = -heappop(hq)
    now , dasom, ans = now-1, dasom+1 , ans +1
    heappush(hq,-now)
print(ans)