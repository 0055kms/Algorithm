def solution(n, times):
    s,e = min(times),n*max(times)
    
    def check(hour):
        cnt = 0
        for t in times:
            cnt += (hour//t)
        if cnt >= n: return True
        else: return False
    
    while s<=e:
        m = (s+e)//2
        if check(m): #m시간 안에 심사 가능함?
            e = m-1
        else:
            s = m+1
            
    return s