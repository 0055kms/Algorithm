import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1:
            if heapq.heappop(scoville) < K:
                return -1
            else: return answer
        else:
            a,b = heapq.heappop(scoville),heapq.heappop(scoville)
            if a < K:
                answer += 1
                heapq.heappush(scoville,a+b*2)
            else: break         
    return answer
    