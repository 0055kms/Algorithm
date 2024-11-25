def solution(s):
    s = s[2:-2]
    sets = s.split('},{')
    set_list = []
    for numbers in sets:
        nums = numbers.split(',')
        set_list.append(nums)
        
    set_list.sort(key = lambda x: len(x))
    answer = []
    memory = set()
    for num_list in set_list:
        for num in num_list:
            if num not in memory:
                answer.append(int(num))
                memory.add(num)
                break
    return answer