def solution(phone_book):
    phone_book.sort()
    
    def is_p(s1,s2): #s2가 길이가 더 길고 s1이 접두어
        if len(s1) == len(s2): return False
        elif len(s2) < len(s1): s1,s2 = s2,s1
        for i in range(len(s1)):
            if s1[i] != s2[i]: return False
        return True
        
    for i in range(len(phone_book)-1):
        if is_p(phone_book[i],phone_book[i+1]):
            return False
    return True