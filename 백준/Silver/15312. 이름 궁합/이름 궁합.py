import sys
input = sys.stdin.readline
match = {}
ar = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
for i in range(65,65+len(ar)):
    match[chr(i)] = ar[i-65]
A = input().rstrip()
B = input().rstrip()
l = len(A)
ar.clear()
for i in range(l):
    ar.append(match[A[i]])
    ar.append(match[B[i]])
l = len(ar)

for i in range(l-1,1,-1):
    tmp = [0] * i
    for j in range(i):
        tmp[j] = (ar[j] + ar[j+1]) % 10
    ar = tmp
for i in ar:
    print(i,end='')