def solution(num):
    if num == 1: return 0

    def find(n,depth):
        if n % 2 == 0: n //= 2
        else:  n = (n*3+1)
        
        if n == 1: return depth
        if depth == 500: return -1
        return find(n,depth+1)
    
    return find(num,1)