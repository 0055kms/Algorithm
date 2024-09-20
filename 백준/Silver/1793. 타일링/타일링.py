import sys
input = sys.stdin.readline
dp = [0] * 251
dp[0] = 1
dp[1] = 1
dp[2] = 3
for i in range(3,251):
    dp[i] = 2*dp[i-2] + dp[i-1]
"""
1 = 세로 1          1
2 = 세로 1  가로 2   3
3 = 세로 3  가로 2    5
4 = 세로 5  가로 6    11
5 = 세로 11 가로 10   21
6 = 세로 21 가로 22   43
7 = 세로 43 가로 42   85
8 = 세로 85 가로 86   171  
"""

while True:
    try:
        N = int(input())
        print(dp[N])
    except:
        break
