import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
A = [deque([*map(int,input().rstrip())]) for _ in range(T)]
K = int(input())
for _ in range(K):
    num,dir = map(int,input().split())
    num-=1
    rotateList = [(num,dir)]
    cur_num = num
    cur_dir = dir
    while cur_num >= 1:
        if A[cur_num-1][2] != A[cur_num][6]:
            cur_num -= 1; cur_dir *= -1
            rotateList.append((cur_num,cur_dir))
        else: break

    cur_num = num
    cur_dir = dir
    while cur_num <= T-2:
        if A[cur_num][2] != A[cur_num+1][6]:
            cur_num += 1; cur_dir *= -1
            rotateList.append((cur_num,cur_dir))
        else: break

    for n,d in rotateList:
        A[n].rotate(d)


ans = 0
for t in A:
    if t[0] == 1: ans += 1
print(ans)