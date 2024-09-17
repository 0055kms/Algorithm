import sys
input = sys.stdin.readline
N = int(input())
A = [*map(int,input().split())]
cmd = [*map(int,input().split())] #개수 + - * //   몇개 남았는지로?
min_ans , max_ans = float("inf"),-float("inf")

u = 0
def dfs():
    global min_ans, max_ans
    if len(tmp) == N-1:
        tmp_ans = A[0]
        for i in range(N-1):
            if tmp[i] == 0:
                tmp_ans = tmp_ans + A[i+1]
            elif tmp[i] == 1:
                tmp_ans = tmp_ans - A[i+1]
            elif tmp[i] == 2:
                tmp_ans = tmp_ans * A[i+1]
            elif tmp[i] == 3:
                tmp_ans = int(tmp_ans / A[i+1])
        min_ans = min(min_ans,tmp_ans)
        max_ans = max(max_ans,tmp_ans)
        return
    for k in range(4):
        if cmd[k]:
            tmp.append(k); cmd[k] -= 1
            dfs()
            tmp.pop(); cmd[k] += 1
tmp = []
dfs()
print(max_ans)
print(min_ans)