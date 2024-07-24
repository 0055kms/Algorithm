import sys
input = sys.stdin.readline
N = int(input())
A = [*map(int,input().split())]
A.sort()
abs_min = float("inf")
result = []
"-97 -6 -2 6 98"
for t in A: #중복 안됨
    si,ei = 0,len(A)-1
    while si < ei:
        if A[si] == t: si += 1
        elif A[ei] == t: ei -= 1
        else:
            if abs_min > abs(t+A[si]+A[ei]):
                result = [t,A[si],A[ei]]
                abs_min = abs(t+A[si]+A[ei])
            if t+A[si]+A[ei] <= 0: si += 1
            else: ei -= 1
result.sort()
print(*result)