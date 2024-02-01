import heapq
def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)
    while n != 0:
        now = -heapq.heappop(works)
        if now == 0: break
        now , n = now -1, n-1
        heapq.heappush(works,-now)
    
    ans = 0
    for i in works:
        ans += i*i
    return ans