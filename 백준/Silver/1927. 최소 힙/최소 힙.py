import sys
input = sys.stdin.readline
from queue import PriorityQueue
N = int(input())
rlist = []
q = PriorityQueue()
for _ in range(N):
    rlist.append(int(input()))
for i in rlist:
    if i == 0:
        if q.qsize() == 0: print(0)
        else: print(q.get())
    else: q.put(i)
