import sys
from heapq import *
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M = int(input())
    A = [*map(int,input().split())]
    for _ in range((M-1)//10):
        A.extend([*map(int,input().split())])
    max_h , min_h = [],[]
    pList = []
    for i in range(M):
        if i == 0:
            pList.append(A[i])
            heappush(min_h,A[i])
        elif i == 1:
            if min_h[0] < A[i]:
                heappush(max_h,-heappop(min_h))
                heappush(min_h,A[i])
            else:
                heappush(max_h,-A[i])
        elif i % 2 == 0: #홀수번째
            if -max_h[0] > A[i]:
                heappush(max_h,-A[i])
                heappush(min_h,-heappop(max_h))
            else:
                heappush(min_h,A[i])
            pList.append(min_h[0])
        else:
            if min_h[0] < A[i]:
                heappush(min_h,A[i])
                heappush(max_h,-heappop(min_h))
            else:
                heappush(max_h,-A[i])
    print(len(pList))
    while pList:
        print(*pList[:10],end='')
        pList = pList[10:]
        if pList: print()
    print()

"""
큰 수 min_h 에 (min_h[0]은 큰 수중 가장 작은)
작은 수 max_h 에 (max_h[0]은 작은 수중 가장 큰)
(홀수일 때) min_h 가 한 개 더 많고 min[0]이 중간값

max 0       0 min
1 2 3       5 6 7 8
"""