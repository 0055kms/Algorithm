import sys
input = sys.stdin.readline

R,C,K = map(int,input().split())
A = [[*map(int,input().split())] for _ in range(R)]
cmdList = [*map(int,input().split())]
for cmd in cmdList:
    if cmd == 1:
        new = [[0 for _ in range(C)] for _ in range(R)]
        for y in range(C):
            for x in range(R):
                new[x][y] = A[R-1-x][y]
        A = new
    elif cmd == 2:
        new = [[0 for _ in range(C)] for _ in range(R)]
        for x in range(R):
            for y in range(C):
                new[x][y] = A[x][C-1-y]
        A = new
    elif cmd == 3:
        R,C = C,R
        new = [[0 for _ in range(C)] for _ in range(R)]
        for x in range(R):
            for y in range(C):
                new[x][y] = A[C-1-y][x]
        A = new
    elif cmd == 4:
        R,C = C,R
        new = [[0 for _ in range(C)] for _ in range(R)]
        for x in range(R):
            for y in range(C):
                new[x][y] = A[y][R-1-x]
        A = new
    elif cmd == 5:
        new = [[0 for _ in range(C)] for _ in range(R)]
        a1 = [x[:C//2] for x in A[:R//2]]
        a2 = [x[C//2:C] for x in A[:R//2]]
        a3 = [x[C//2:C] for x in A[R//2:R]]
        a4 = [x[:C//2] for x in A[R//2:R]]

        for i in range(R//2):
            new[i][:C//2] = a4[i]
            new[i][C//2:C] = a1[i]
        for i in range(R//2, R):
            new[i][:C//2] = a3[i - R//2]
            new[i][C//2:C] = a2[i - R//2]
        A = new

    elif cmd == 6:
        new = [[0 for _ in range(C)] for _ in range(R)]
        a1 = [x[:C//2] for x in A[:R//2]]
        a2 = [x[C//2:C] for x in A[:R//2]]
        a3 = [x[C//2:C] for x in A[R//2:R]]
        a4 = [x[:C//2] for x in A[R//2:R]]

        for i in range(R//2):
            new[i][:C//2] = a2[i]
            new[i][C//2:C] = a3[i]
        for i in range(R//2, R):
            new[i][:C//2] = a1[i - R//2]
            new[i][C//2:C] = a4[i - R//2]
        A = new
for row in A:
    print(*row)