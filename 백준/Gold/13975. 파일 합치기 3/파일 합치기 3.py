import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    A = [*map(int,input().split())]
    ans = 0
    heapq.heapify(A)
    while len(A) > 1: 
        x1,x2 = heapq.heappop(A),heapq.heappop(A)
        tmp = x1+x2
        ans += (tmp)
        heapq.heappush(A,tmp)
    print(ans)
