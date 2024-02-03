N, B, C = 0, 3, 2
ans = 0
v, cnt = [], []
N = int(input())
v = list(map(int, input().split()))
cnt = [0] * N
ans += B * v[0]
for i in range(1, N):
    m = min(v[i], v[i - 1])
    v[i] -= m
    cnt[i] += m
    ans += C * m
    m = min(v[i], cnt[i - 1]) 
    v[i] -= m
    ans += C * m
    ans += B * v[i]
print(ans)
