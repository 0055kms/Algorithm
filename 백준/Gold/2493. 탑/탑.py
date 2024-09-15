import sys
input = sys.stdin.readline
N = int(input())
A = [x for x in map(int,input().split())]
"""
왼쪽 더 큰 것 인덱스, 없으면 0
스택에서 왼쪽에 더 작은 것들은 필요x -> 스택 내림차순
cur > top: pop()
9 5
"""
stack = [(A[0],1)] #값,인덱스
ans = [0] * len(A)
for i in range(1,N):
    cur = A[i]
    while stack:
        if cur > stack[-1][0]:
            stack.pop()
        else:
            ans[i] = stack[-1][1]
            break
    stack.append((cur, i + 1))
print(*ans)