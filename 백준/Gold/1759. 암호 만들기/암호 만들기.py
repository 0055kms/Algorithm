import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
L,C = map(int,input().split())
A = [*input().split()]
A.sort()
#모음 한 개 이상 나머지 자음으로 총 길이 L, 증가하는 순서 -> 조합의 개수만 구하면 됨
#A에서 총 L개 뽑은것들 -> 거기서 모음 한 개 이상 있다면 답임
word = ''
wordList = []

def dfs(idx):
    global word
    if len(word) == L: wordList.append(word); return
    for i in range(idx,C):
        c = A[i]
        word += c
        dfs(i+1)
        word = word[:-1]
dfs(0)
for word in wordList:
    mcnt = 0 # 모음 수
    for c in word:
        if c in ['a','e','i','o','u']: mcnt += 1
    gcnt = L-mcnt
    if mcnt >= 1 and gcnt >= 2: print(word)

