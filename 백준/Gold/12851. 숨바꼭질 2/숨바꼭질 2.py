import sys
from collections import deque

input = sys.stdin.readline

S, E = map(int, input().split())
D = [[float("inf"), 0] for _ in range(100001)]

q = deque([S])
D[S][0] = 0
D[S][1] = 1

while q:
    posi = q.popleft()

    for np in [posi - 1, posi + 1, posi * 2]:
        if 0 <= np <= 100000:
            if D[np][0] > D[posi][0] + 1:
                D[np][0] = D[posi][0] + 1
                D[np][1] = D[posi][1]
                q.append(np)
            elif D[np][0] == D[posi][0] + 1:
                D[np][1] += D[posi][1]

print(D[E][0])
print(D[E][1])
