import sys
input = sys.stdin.readline
two = [i//2 + 1 for i in range(10001)]
three = [0] * 10001
for i in range(10001):
    tmp = 0
    for j in range(0,i+1,3):
        tmp += two[i-j]
    three[i] = tmp
n = int(input())
for _ in range(n):
    print(three[int(input())])
