import sys
input = sys.stdin.readline
"""
시작 기준으로 정렬
ans = 0
prev = [,] 이전에 덮은 널빤지 (웅덩이 아님)

s,e
if prev[1] + 1 > e: 다음 단계로
else:
    s = max(s,prev[1]+1)
    널빤지 작업하면서 ans 증가,prev 업데이트
"""
N,L = map(int,input().split())
cmds = [[*map(int,input().split())] for _ in range(N)]
cmds.sort(key = lambda x: x[0])
prev = [-1,-1]
ans = 0
for s,e in cmds:
    e -= 1
    if prev[1] + 1 > e: continue
    s = max(s,prev[1]+1)
    need_len = e-s+1
    if need_len % L == 0: cnt = need_len // L
    else: cnt = need_len // L + 1
    ans += cnt
    prev = [s,s+cnt*L-1]
print(ans)


