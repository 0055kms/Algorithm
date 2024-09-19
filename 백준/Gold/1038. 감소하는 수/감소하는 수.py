import sys
input = sys.stdin.readline
N = int(input())

if N >= 1023:
    print(-1)
    sys.exit()
t = 0 # t번째 수 체크중
k = 1 # 길이 k 수 체크중
def dfs():
    global t,k
    if len(num) == k:
        if t == N:
            print(''.join(map(str, num)))
            sys.exit()
        else:
            t += 1

    for i in range(0,10):
        if num[-1] > i:
            num.append(i)
            dfs()
            num.pop()

while True:
    for i in range(0,10):
        num = [i]
        dfs()
    k += 1
    if k> 10:
        print(-1); break