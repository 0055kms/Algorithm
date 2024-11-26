def solution(s):
    answer = [0,0] #이진 변환 횟수, 과정에서 제거된 모든 0의 개수
    while s != '1':
        answer[0] += 1
        cnt = 0
        for i in range(len(s)):
            if s[i] == '0': cnt += 1
        answer[1] += cnt
        s = s.replace('0','')
        bin_num = str(bin(len(s)))[2:]
        s = bin_num
    return answer