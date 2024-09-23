import sys
from heapq import *
N = int(input())
A = [[x for x in map(int,input().split())] for _ in range(N)] # [일,점수]
#마감일 긴 순
A.sort(reverse = True)

hq = []
day = N
ans = 0
for day in range(N,0,-1):
    while A:
        if A[0][0] >= day:
            d,w = A.pop(0)
            heappush(hq,(-w,d))
        else: break
    if hq:
        ans += (-heappop(hq)[0])
    day -= 1
print(ans)
"""
hq에 현재 날짜로 가능한 것들 추가, hq는 과제 점수 기준 최대 힙
if hq: pop및 정답 업데이트
"""