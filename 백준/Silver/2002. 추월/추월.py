import sys
input = sys.stdin.readline
N = int(input())
S,E = {},[]
for i in range(N): S[input().rstrip()] = i
for _ in range(N): E.append(S[input().rstrip()])
ans = 0
while E:
    if E[0] != min(E): ans += 1
    E.pop(0)
print(ans)