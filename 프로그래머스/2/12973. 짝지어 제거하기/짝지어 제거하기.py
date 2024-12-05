def solution(s):
    answer = -1
    if len(s) == 1: return 0
    if len(s) == 2:
        if s[0] == s[1]: return 1
        else: return 0
    """
    
    
    ab a
    """
    stack = []
    for c in s:
        stack.append(c)
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()            
    if stack: return 0
    else: return 1