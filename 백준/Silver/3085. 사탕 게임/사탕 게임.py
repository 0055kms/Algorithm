import sys
input = sys.stdin.readline
N = int(input())
Board = []
ans = 0
for _ in range(N):
    col = input().rstrip()
    line = []
    for c in col: line.append(c)
    Board.append(line)

def check():
    maxx = 0
    for y in range(N):
        prev = Board[y][0]
        cnt = 1
        for x in range(1,N):
            cur = Board[y][x]
            if prev == cur: cnt += 1
            else:
                prev = cur
                cnt = 1
            maxx = max(cnt,maxx)
    for x in range(N):
        prev = Board[0][x]
        cnt = 1
        for y in range(1,N):
            cur = Board[y][x]
            if prev == cur: cnt += 1
            else:
                prev = cur
                cnt = 1
            maxx = max(cnt,maxx)

    return maxx

def y_count(y,x): #y,y+1 교환 > 최대길이return > 원래대로
    Board[y][x], Board[y + 1][x] = Board[y + 1][x], Board[y][x]
    maxx = check()
    Board[y][x], Board[y + 1][x] = Board[y + 1][x], Board[y][x]
    return maxx

def x_count(y,x): #x,x+1 교환 > 최대길이return > 원래대로
    Board[y][x], Board[y][x+1] = Board[y][x+1],Board[y][x]
    maxx = check()
    Board[y][x], Board[y][x+1] = Board[y][x+1],Board[y][x]
    return maxx

for y in range(N-1):
    for x in range(N):
        ans = max(ans,y_count(y,x))

for y in range(N):
    for x in range(N-1):
        ans = max(ans,x_count(y,x))

print(ans)

