import sys
from heapq import *
input = sys.stdin.readline
N = int(input())
mhq = []
for _ in range(N):
    line = [*map(int,input().split())]
    if line[0] == 0:
        print(-1 if not mhq else -heappop(mhq))
    else:
        for i in line[1:]:
            heappush(mhq,-i)