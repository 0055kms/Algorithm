import sys
input = sys.stdin.readline
N = int(input())
A = [[0 for _ in range(N)] for _ in range(N)]
dir = [(-1,0),(1,0),(0,-1),(0,1)]
likeList = [0] * (N**2+1)
for _ in range(N**2):
    cmd = [x for x in map(int,input().split())]
    stu = cmd[0]; likes = cmd[1:]
    likeList[stu] = likes
    check = [] #(좋인접,비어인접,x,y)
    for x in range(N):
        for y in range(N):
            if A[x][y] == 0: #비어있는칸만
                like = 0
                empty = 0
                for dx,dy in dir:
                    nx,ny = x+dx,y+dy
                    if not (0 <= nx <= N-1 and 0<= ny <= N-1): continue
                    if A[nx][ny] in likes: like += 1
                    if A[nx][ny] == 0: empty += 1
                check.append((like,empty,x,y))
    check.sort(key = lambda x: (-x[0],-x[1],x[2],x[3]))
    s = check[0]
    A[s[2]][s[3]] = stu

ans = 0
table = {0:0,1:1,2:10,3:100,4:1000}
for x in range(N):
    for y in range(N):
        stu = A[x][y]
        like = 0
        for dx,dy in dir:
            nx,ny = dx+x,dy+y
            if not (0<=nx<=N-1 and 0<=ny<=N-1): continue
            if A[nx][ny] in likeList[stu]: like += 1
        ans += table[like]
print(ans)