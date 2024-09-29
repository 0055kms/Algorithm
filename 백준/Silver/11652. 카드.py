import sys
input = sys.stdin.readline
from collections import defaultdict
dic = defaultdict(int)
N = int(input())
for _ in range(N): dic[int(input())] += 1
A = list(dic.items())
A.sort(key = lambda x: (-x[1],x[0]))
print(A[0][0])
