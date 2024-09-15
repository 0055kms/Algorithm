import sys
input = sys.stdin.readline
N = int(input())
A = [x for x in map(int,input().split())]
"""
오른쪽에서 등장횟수 더큰
1. 내림차순 스택
2. top > cur 일때까지 빼면서 top들 값 업데이트
3. top > cur 이면 cur 업데이트 
"""
count = {}
for i in A:
    if i in count: count[i] += 1
    else: count[i] = 1
for i in range(len(A)):
    A[i] = [A[i],count[A[i]],i] #수,등장횟수,인덱스

stack = []
ans = [-1] * N
for i in range(N):
    while stack:
        if stack[-1][1] >= A[i][1]:
            stack.append(A[i])
            break
        else:
            ans[stack[-1][2]] = A[i][0]
            stack.pop()
    if not stack: stack = [A[i]]
print(*ans)