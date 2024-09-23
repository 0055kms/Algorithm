import sys
from heapq import *
input = sys.stdin.readline
hq = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0: print(0 if not hq else -heappop(hq))
    else: heappush(hq,-x)