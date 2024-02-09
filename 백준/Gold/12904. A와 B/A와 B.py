import sys
input = sys.stdin.readline
S = input().rstrip()
T = input().rstrip()
ans = 0
while T:
    if T[-1] == "A": T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]
    if S == T: ans = 1
print(ans)
