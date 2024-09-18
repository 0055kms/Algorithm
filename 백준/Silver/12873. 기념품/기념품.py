import sys
input = sys.stdin.readline
N = int(input())
A = [x+1 for x in range(N)]

t = 1
idx = 0
while len(A) != 1:
    tv = t ** 3
    idx = (idx + tv - 1) % len(A)
    A.pop(idx)
    t += 1
print(A[0])