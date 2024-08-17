import sys
from collections import deque
input = sys.stdin.readline
"""
정답 : ?
을
입력값 순서대로 내려놓으면
1 2 3 4 N
앞을 위로 함


"""

N = int(input())
ans = deque()
ar = [x for x in map(int,input().split())][::-1]
card = [x+1 for x in range(N)]
for i in range(N):
    cmd = ar[i]
    if cmd == 1:
        ans.appendleft(card[i])
    elif cmd == 2:
        ans.insert(1,card[i])
    elif cmd == 3:
        ans.append(card[i])
print(*ans)
