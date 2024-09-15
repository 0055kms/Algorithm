import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
A = [[*map(int,input().rstrip())] for _ in range(9)]
zeros = []
"""
행 체크 -> 열 -> 블록
0 1 2  3 4 5  6 7 8
"""
for x in range(9):
    for y in range(9):
        if A[x][y] == 0:
            zeros.append((x,y))

def check(x,y,k):
    for i in range(9):
        if A[x][i] == k: return False
        if A[i][y] == k: return False
    if 0 <= x <= 2: xList = [0,1,2]
    elif 3 <= x <= 5: xList = [3,4,5]
    else: xList = [6,7,8]
    if 0 <= y <= 2: yList = [0,1,2]
    elif 3 <= y <= 5: yList = [3,4,5]
    else: yList = [6,7,8]

    for i in xList:
        for j in yList:
            if A[i][j] == k: return False
    return True

def dfs(d):
    if d == len(zeros):
        for i in range(9):
            for j in range(9):
                print(A[i][j],end='')
            print()
        sys.exit(0)
    x,y = zeros[d]
    for k in range(1,10):
        if not check(x,y,k): continue
        A[x][y] = k
        dfs(d+1)
        A[x][y] = 0
dfs(0)
