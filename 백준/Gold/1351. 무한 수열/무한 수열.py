import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N,P,Q = map(int,input().split())
save = {}
save[0] = 1
def f(cur):
    global save,P,Q
    if cur not in save:
        save[cur] = (f(cur//Q) + f(cur//P))
    return save[cur]
print(f(N))