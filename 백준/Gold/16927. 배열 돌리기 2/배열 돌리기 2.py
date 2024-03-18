#leetaekyu2077 님의 블로그에 게시된 풀이를 참고했습니다
import sys
from collections import deque
q = deque()
input = sys.stdin.readline
rows,cols,R = map(int,input().split())
A = [[*map(int,input().split())] for _ in range(rows)]
loop = min(rows,cols)//2
for l in range(loop):
    q.clear()
    q.extend(A[l][l:cols-l])
    q.extend([row[cols-1-l] for row in A[l+1:rows-l]])
    q.extend(A[rows-1-l][l:cols-l-1][::-1])
    q.extend([row[l] for row in A[l+1:rows-1-l]][::-1])
    q.rotate(-R)
    for x in range(l,cols-l): A[l][x] = q.popleft()
    for y in range(l+1,rows-l): A[y][cols-1-l] = q.popleft()
    for x in range(cols-l-2,l-1,-1): A[rows-l-1][x] = q.popleft()
    for y in range(rows-2-l,l,-1): A[y][l] = q.popleft()

for y in range(rows):
    print(*A[y])