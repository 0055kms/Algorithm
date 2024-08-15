import sys
input = sys.stdin.readline

isPrime = [True] * 300000
isPrime[0] = False; isPrime[1] = False
for i in range(2,int(300000**0.5)+1):
    if isPrime[i]:
        for j in range(i*2,300000,i):
            isPrime[j] = False

PrimeCnt = [0] * 300000
cnt = 0
for i in range(300000):
    if isPrime[i]: cnt += 1
    PrimeCnt[i] = cnt


while True:
    n = int(input())
    if n == 0: break
    print(PrimeCnt[2*n]-PrimeCnt[n])