from collections import deque



def solution(numbers, target):
    def bfs():
        nonlocal ans
        q = deque([(0,0)]) #idx , num
        while q:
            cur_idx,num = q.popleft()
            if cur_idx == len(numbers):
                if num == target: ans += 1
                continue
            q.append((cur_idx+1,num+numbers[cur_idx]))
            q.append((cur_idx+1,num-numbers[cur_idx]))
    
    ans = 0
    bfs()
    return ans