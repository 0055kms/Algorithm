import sys
import heapq
input = sys.stdin.readline
h = [0] #강의실별 끝나는 시간
N = int(input())
s = [[*map(int,input().split())] for _ in range(N)]
s.sort(key = lambda x: (x[0],x[1]),reverse=True)
while s:
    S,T = s.pop()
    now = heapq.heappop(h)
    if now <= S: heapq.heappush(h,T)
    else:
        heapq.heappush(h,T)
        heapq.heappush(h,now)
print(len(h))
