import sys
input = sys.stdin.readline
from collections import deque

S,E = map(int,input().split())
D = [[float("inf"), -1] for _ in range(100001)]



q = deque(); q.append([S,0])
D[S][0] = 0
while q:
    posi,time = q.popleft()
    np,nt = posi-1,time+1
    if 0<=np<=100000 and D[np][0] > nt:
        D[np][0] = nt
        D[np][1] = posi
        q.append([np,nt])

    np,nt = posi+1,time+1
    if 0<=np<=100000 and D[np][0] > nt:
        D[np][0] = nt
        D[np][1] = posi
        q.append([np,nt])

    np,nt = posi*2,time+1
    if 0<=np<=100000 and D[np][0] > nt:
        D[np][0] = nt
        D[np][1] = posi
        q.append([np,nt])

print(D[E][0])
q.clear()
q.append(D[E])
ans = [E]
while q:
    time,prev = q.popleft()
    if time == 0: break
    ans.append(prev)
    q.append(D[prev])
print(*ans[::-1])
