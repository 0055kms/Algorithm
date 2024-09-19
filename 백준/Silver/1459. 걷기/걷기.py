import sys
input = sys.stdin.readline
X,Y,W,S = map(int,input().split())
if W*2 < S:
    print(X*W+Y*W)
else:
    if X > Y: MIN = Y; MAX = X
    else: MIN = X; MAX = Y
    ans = MIN * S
    res = MAX-MIN
    if S < W:
        ans += (res//2 *2*S)
        res %= 2
        ans += (res*W)
    else:
        ans += (res*W)
    print(ans)