import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    B = input().rstrip()
    ans = 0
    for i, c in enumerate(B):
        if c == '1':
            ans += 2**(len(B) - i) - 1
            ans *= -1
    print(ans if ans > 0 else -ans)