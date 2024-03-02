import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
nums = [*map(int,input().split())]
op = [*map(int,input().split())]
max_val , min_val = -sys.maxsize,sys.maxsize
def dfs(val,depth):
    global max_val,min_val
    if depth == N-1:
        max_val = max(max_val,val)
        min_val = min(min_val,val)
    else:
        for i in range(4):
            if op[i]:
                op[i] -= 1
                tmp = update(val,i,depth+1)
                dfs(tmp,depth+1)
                op[i] += 1

def update(val,cmd,idx):
    if cmd == 0:
        return val + nums[idx]
    elif cmd == 1:
        return val - nums[idx]
    elif cmd == 2:
        return val * nums[idx]
    else:
        return int(val / nums[idx])
dfs(nums[0],0)
print(max_val)
print(min_val)

