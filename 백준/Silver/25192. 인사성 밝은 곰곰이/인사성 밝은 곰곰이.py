import sys
input = sys.stdin.readline
N = int(input())
visit = set()
ans = 0
for _ in range(N):
    cmd = input().rstrip()
    if cmd == "ENTER": visit.clear()
    else:
        if cmd not in visit:
            ans += 1
            visit.add(cmd)
print(ans)