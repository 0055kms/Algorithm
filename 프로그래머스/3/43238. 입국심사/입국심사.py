def solution(n, times):
    times.sort()
    answer = 0
    s,e = 0,times[-1] * n
    while s<=e:
        m = (s+e)//2
        tmp_ans = 0
        for time in times: tmp_ans += (m//time)
        if tmp_ans >= n: #m분의 시간으로 n명이상 처리가 가능
            e = m-1
        else: #불가능
            s = m+1
    
    return e+1