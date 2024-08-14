import sys
input = sys.stdin.readline
count = {}
name = input().rstrip()
for c in name:
    if c not in count: count[c] = 1
    else: count[c] += 1

front = []
cnt = 0
for c in count:
    if count[c] % 2 == 1:
        cnt += 1
        mid = c
    for _ in range(count[c]//2):
        front.append(c)
front.sort()
front = ''.join(front)

if cnt > 1: print("I'm Sorry Hansoo")
elif cnt == 1:
    print(front,end='')
    print(mid,end='')
    print(front[::-1],end='')
else:
    print(front,end='')
    print(front[::-1],end='')