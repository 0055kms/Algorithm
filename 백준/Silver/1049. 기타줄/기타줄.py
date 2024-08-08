import sys
input = sys.stdin.readline
N,M = map(int,input().split())
min6 = float("inf")
min1 = float("inf")
for _ in range(M):
    b6,b1 = map(int,input().split())
    min6 = min(min6,b6)
    min1 = min(min1,b1)
if(6*min1 <= min6):
    print(min1*N)
else:
    ans = 0
    ans += (N//6 * min6)
    ans += min((N%6 * min1),min6)
    print(ans)