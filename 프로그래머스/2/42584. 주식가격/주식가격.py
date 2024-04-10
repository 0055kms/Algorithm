def solution(prices):
    """
    스택에 인덱스를 저장하고 prices[idx]가 값임
    스택의 위부터 값큰거 가짐
    while (스택 and 스택(탑)의 값 > 새로들어오는애 값):
        스택 탑 빼고 
    새로운거 넣고 스택모든요소들 k+=1
    
    
    
    3
    2
    1
    """
    answer = [0] * len(prices)
    stack = []
    for idx in range(len(prices)):
        while (stack and prices[stack[-1]] > prices[idx]):
            stack.pop()
        stack.append(idx)
        if idx != len(prices)-1:
            for i in stack:
                answer[i] += 1
    return answer