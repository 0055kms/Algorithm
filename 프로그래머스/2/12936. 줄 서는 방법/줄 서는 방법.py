from math import factorial as f

def solution(n, k):
    remain = [x for x in range(1,n+1)]
    k -= 1
    result = []
    
    for i in range(n-1,-1,-1):
        """
        맨앞 1: 24개
                두번째 2: 6개
                      3: 6개
                      
             2: 24개
                두번째 1: 6개
                      3:  6개
                      
        i 2  k 4   val 2   remain [1,2,3]
        
        """
        val = k//f(i)
        k -= val*f(i)
        now = remain.pop(val)
        result.append(now)
    return result