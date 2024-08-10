import sys
from heapq import *
input = sys.stdin.readline
N = int(input())
hq = []
for _ in range(N):
    nums = [x for x in map(int,input().split())]
    for n in nums:
        if len(hq) < N:
            heappush(hq,n)
        else:
            heappush(hq,n)
            heappop(hq)
print(hq[0])