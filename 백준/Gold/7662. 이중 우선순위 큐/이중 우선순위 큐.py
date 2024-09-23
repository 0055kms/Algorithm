import sys
from heapq import *
from collections import defaultdict
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    min_hq,max_hq = [],[]
    k = int(input())
    count = defaultdict(int) #0이면 원래 없거나 다른 큐에서 제거된 수임
    for idx in range(k):
        cmd,val = input().rstrip().split()
        val = int(val)
        if cmd == 'I':
            heappush(min_hq,val); heappush(max_hq,-val)
            count[val] += 1
        else:
            if val == 1: #최댓값 삭제
                while max_hq:
                    if count[-max_hq[0]] == 0:
                        heappop(max_hq)
                        continue
                    count[-heappop(max_hq)] -= 1
                    break
            else:
                while min_hq: #최소
                    if count[min_hq[0]] == 0:
                        heappop(min_hq)
                        continue
                    count[heappop(min_hq)] -= 1
                    break
    min_val,max_val = None,None
    while min_hq:
        if count[min_hq[0]] == 0:
            heappop(min_hq)
            continue
        min_val = min_hq[0]
        break
    while max_hq:
        if count[-max_hq[0]] == 0:
            heappop(max_hq)
            continue
        max_val = -max_hq[0]
        break
    if max_val == None: print("EMPTY")
    else: print(max_val,min_val)