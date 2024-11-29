from itertools import permutations

def solution(expression):
    option = ['*', '+', '-']
    cases = list(permutations(option))
    ans = []

    string = []
    prev = 0
    for i in range(len(expression)):
        if expression[i] in option:
            string.append(expression[prev:i])
            string.append(expression[i])
            prev = i + 1
    string.append(expression[prev:])

    for case in cases:
        tmp = string[:]  
        for cmd in case:
            idx = 0
            while idx < len(tmp):
                if tmp[idx] == cmd:
                    if cmd == '*':
                        tmp[idx-1:idx+2] = [str(int(tmp[idx-1]) * int(tmp[idx+1]))]
                    elif cmd == '+':
                        tmp[idx-1:idx+2] = [str(int(tmp[idx-1]) + int(tmp[idx+1]))]
                    elif cmd == '-':
                        tmp[idx-1:idx+2] = [str(int(tmp[idx-1]) - int(tmp[idx+1]))]
                    idx -= 1
                idx += 1
        ans.append(abs(int(tmp[0])))

    return max(ans)
