from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    w = 0
    q = deque([0]*bridge_length)
    t = truck_weights[::-1]
    while t:
        time += 1
        tmp = q.popleft()
        w -= tmp
        if w + t[-1] <= weight:
            now = t.pop()
            q.append(now)
            w += now
        else:
            q.append(0)
        
        
    return time + bridge_length


# 7
# 0 7
# 4   7
# 5 4 7
# 6 0 5 4 7

# 다음 트럭이 다리에 올수있다 vs 올수없다
# 올수있다면 