import sys
sys.setrecursionlimit(10**6)

def solution(begin, target, words):
    answer = sys.maxsize
    if target not in words: return 0

    def diff(s1,s2):
        tmp = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                tmp += 1
        return tmp

    visit = [False] * len(words) 
    def dfs(cur,depth):
        nonlocal answer
        if words[cur] == target:
            answer = min(answer,depth)
        for i in range(len(words)):
            if not visit[i] and diff(words[i],words[cur]) == 1:
                visit[i] = True
                dfs(i,depth+1)
                visit[i] = False
        
    for i in range(len(words)):
        if diff(words[i],begin) <= 1:
            visit[i] = True
            dfs(i,1) #i로 시작
            visit[i] = False
    
    
    return answer