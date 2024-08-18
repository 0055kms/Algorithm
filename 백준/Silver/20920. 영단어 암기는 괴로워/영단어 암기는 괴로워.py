import sys
input = sys.stdin.readline
N,M = map(int,input().split())

count = {}

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in count: count[word] += 1
        else: count[word] = 1

words = [] # 단어, 횟수
for key in count:
    val = count[key]
    words.append([key,val])

words.sort(key = lambda x: (-x[1],-len(x[0]),x[0]))
for w in words:
    print(w[0])