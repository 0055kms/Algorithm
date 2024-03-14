def solution(sequence, k):
    answer = []
    su_len = 1e7
    sp,ep = 0,0
    tmp = sequence[0]
    l = len(sequence)
    
    while ep >= sp:
        if tmp < k:
            ep += 1
            if ep == l: break
            tmp += sequence[ep]
        elif tmp > k:
            tmp -= sequence[sp]
            sp += 1
            
        else:
            if ep - sp < su_len:
                su_len = ep - sp
                answer = [sp,ep]
            ep += 1
            if ep == l: break
            tmp += sequence[ep]
    
    return answer