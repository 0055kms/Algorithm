import sys; input = sys.stdin.readline
R,C,M = map(int,input().split())
board = [[[] for _ in range(C)] for _ in range(R)]
dir = [(-1,0),(1,0),(0,1),(0,-1)]



def control(x):
    if x == 0 or x == 2: return x + 1
    else: return x - 1

def catch(y):
    global ans
    for x in range(R):
        if board[x][y]:
            ans += board[x][y][0][2]
            board[x][y] = []
            return

def move():
    global board
    tmp_board = [[[] for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y]:
                s, d, size = board[x][y][0]
                ny, nx = y, x
                for _ in range(s):
                    dx,dy = dir[d]
                    if 0 <= ny + dy < C and 0 <= nx + dx < R:
                        ny += dy
                        nx += dx
                    else:
                        d = control(d)
                        dx,dy = dir[d]
                        ny += dy
                        nx += dx
                if not tmp_board[nx][ny] or tmp_board[nx][ny][0][2] < size:
                    tmp_board[nx][ny] = [[s, d, size]]
    board = tmp_board


if __name__ == '__main__':
    ans = 0
    for _ in range(M):
        r, c, s, d, size = map(int, input().split())
        board[r - 1][c - 1].append([s, d - 1, size])

    for y in range(C):
        catch(y)
        move()
    print(ans)
