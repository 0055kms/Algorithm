import sys
input = sys.stdin.readline
count = {}
ans = -1
ans_max = -float("inf")
N = int(input())
for _ in range(N):
    k = int(input())
    if k in count: count[k] += 1
    else: count[k] = 1
for key in count:
    val = count[key]
    if val > ans_max:
        ans_max = val
        ans = key
    elif val == ans_max and key < ans:
        ans = key
print(ans)