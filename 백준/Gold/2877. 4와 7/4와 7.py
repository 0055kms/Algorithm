import sys
input = sys.stdin.readline
K = int(input())
l = 1
t = 2
while True:
    if K <= t:
        mod = t-K+1
        break
    else:
        l += 1
        t += (2**l)
"""
l자리 수 중 mod번째 큰 수
444   8
447   7
474   6
477   5
744   4
747   3
774   2
777   1
"""
k = 2**l
ans = ''
while len(ans) != l:
    k //= 2
    if k >= mod: ans += '7'
    else:
        ans += '4'
        mod -= k
print(ans)
