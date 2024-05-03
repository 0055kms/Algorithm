import sys
from collections import deque
input = sys.stdin.readline
n = int(input())  # 4
"""
1. 스택에 i를 저장한다  2. 만약 새로 저장하려는 i의 nums[i]가 nums[stack[-1] 보다
크다면 크지않을때까지 계속 pop하고
팝한 i의 result[i] 는 새로 저장하려는 i의 nums[i]
"""
nums = list(map(int,input().split()))  # 3 5 2 7
stack = []
result = [-1] * n
for i in range(n):
    while stack and nums[i] > nums[stack[-1]]:
        result[stack.pop()] = nums[i]
    stack.append(i)
for i in range(n):
    print(result[i], end = ' ')