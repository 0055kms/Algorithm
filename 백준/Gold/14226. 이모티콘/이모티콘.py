import sys
from collections import deque
input = sys.stdin.readline
S = int(input())
v = [[False] * 2001 for _ in range(2001)]
q = deque()
q.append((1, -1, 0))
v[1][0] = True
while q:
    val, copy, t = q.popleft()
    if val == S:
        print(t)
        break
    if 0 <= val - 1 and not v[val - 1][copy]:
        v[val - 1][copy] = True
        q.append((val - 1, copy, t + 1))
    if copy != -1 and 0 <= val + copy <= 2000 and not v[val + copy][copy]:
        v[val + copy][copy] = True
        q.append((val + copy, copy, t + 1))
    if not v[val][val]:
        v[val][val] = True
        q.append((val, val, t + 1))
