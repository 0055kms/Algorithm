import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
d = [[*map(int,input().split())] for _ in range(n)]
d.sort(key = lambda x: x[1])
ans = PriorityQueue()
for pay,date in d:
    ans.put((pay,date))
    if ans.qsize() > date: ans.get()
answer = 0
while ans.qsize() != 0:
    k = ans.get()
    answer += k[0]
print(answer)