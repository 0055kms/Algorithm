import sys
sys.setrecursionlimit(10**6)

def solution(word):
    ans = 0
    alpha = ['A','E','I','O','U']
    words = []
    def dfs(cur):
        words.append(''.join(cur))
        if len(cur) == 5: return
        for c in alpha:
            cur.append(c)
            dfs(cur)
            cur.pop()
    dfs([])
    for i,v in enumerate(words):
        if v == word: return i