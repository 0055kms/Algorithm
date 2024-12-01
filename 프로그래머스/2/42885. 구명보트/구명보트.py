def solution(people, limit):
    """
    [10, 20, 30, 40, 50, 60, 60, 70, 90, 100]
    """
    answer = len(people)
    s,e = 0,len(people) -1
    people.sort()
    while s < e:
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
            answer -= 1
        else:
            e -= 1
            
    return answer