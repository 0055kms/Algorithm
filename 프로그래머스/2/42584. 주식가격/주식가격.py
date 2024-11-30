def solution(prices):
    answer = [0] * len(prices)
    prices = [(i,prices[i]) for i in range(len(prices))]
    stack = []
    for i,v in prices:
        while stack and v < stack[-1][1]:
            ni,nv = stack.pop()
            answer[ni] = i-ni
        stack.append((i,v))
    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = len(answer) -1 - i
        
    return answer