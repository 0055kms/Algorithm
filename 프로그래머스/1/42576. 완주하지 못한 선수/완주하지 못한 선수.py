def solution(participant, completion):
    count = dict()
    for p in participant:
        if p not in count:
            count[p] = 1
        else:
            count[p] += 1
    for c in completion:
        count[c] -= 1
    
    for key in count:
        if count[key] == 1:
            return key
        
    answer = ''
    return answer