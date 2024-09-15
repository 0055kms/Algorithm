import sys
input = sys.stdin.readline
from collections import deque
N,W,L = map(int,input().split()) #트럭 수,다리 길이,최대 하중
A = [x for x in map(int,input().split())]
q = deque([0] * W)
weight = 0
time = 0
for t in A:
    time += 1
    weight -= q.popleft()
    while weight + t > L:
        time += 1
        weight -= q.popleft()
        q.append(0)
    else:
        weight += t
        q.append(t)
print(time + W)