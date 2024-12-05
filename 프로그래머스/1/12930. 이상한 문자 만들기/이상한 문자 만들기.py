def solution(s):
    answer = []
    words = list(s.split(' '))
    for w in words:
        word = []
        for i in range(len(w)):
            if i % 2 == 0:
                word.append(w[i].upper())
            else:
                word.append(w[i].lower())
        word = ''.join(word)
        answer.append(word)
        answer.append(' ')
    
    return ''.join(answer[:-1])