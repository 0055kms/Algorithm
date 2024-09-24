from heapq import *

def solution(scoville, K):
    A = scoville
    ans = 0
    heapify(A)
    while len(A) != 1:
        if A[0] >= K: return ans
        else:
            heappush(A,heappop(A)+2*heappop(A))
            ans += 1
    return(ans if A[0] >= K else -1)