import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    A = [*map(int,input().split())]
    for i in range(len(A)):
        A[i] = (A[i],i)
    q = deque(A)
    time = 0
    while True:
        max_val = -float("inf")
        for v,i in q:
            if max_val < v: max_val = v
        if q[0][0] == max_val:
            time += 1
            tv,ti = q.popleft()
            if ti == M:
                print(time)
                break
        else: q.append(q.popleft())