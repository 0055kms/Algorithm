import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()
ans,IOI = 0,0
i = 0

while i < M - 1:
    if S[i:i+3] == 'IOI':
        IOI += 1
        if IOI == N:
            ans += 1
            IOI -= 1
        i += 2
    else:
        IOI = 0
        i += 1

print(ans)
