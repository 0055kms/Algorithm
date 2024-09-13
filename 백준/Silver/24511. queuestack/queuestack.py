import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = [*map(int,input().split())]
B = [*map(int,input().split())]
M = int(input())
cmd = [*map(int,input().split())]

ar = []
for i in range(len(A)):
    if A[i] == 0:
        ar.append(B[i])
q = deque(ar)
ans = []
for c in cmd:
    q.appendleft(c)
    ans.append(q.pop())
print(*ans)