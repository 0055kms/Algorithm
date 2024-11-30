def solution(progresses, speeds):
    answer = []
    can = [0] * len(speeds)
    for i in range(len(speeds)):
        p = 100-progresses[i] #7 70 45
        s = speeds[i]
        if p % s == 0: can[i] = (p//s)
        else: can[i] = (p//s+1)
    can = can[::-1]
    while can:
        tmp = 1
        first = can.pop()
        while can and can[-1] <= first:
            can.pop()
            tmp += 1
        answer.append(tmp)
    return answer