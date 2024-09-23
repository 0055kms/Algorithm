import sys
from heapq import *
n,m = map(int,input().split())
hq = [x for x in map(int,input().split())]
heapify(hq)
for _ in range(m):
    x,y = heappop(hq),heappop(hq)
    for _ in range(2): heappush(hq,x+y)
print(sum(hq))