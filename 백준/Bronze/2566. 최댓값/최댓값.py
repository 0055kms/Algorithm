import sys
input = sys.stdin.readline
A = [[x for x in map(int,input().split())] for _ in range(9)]
max_val = A[0][0]
max_posi = (1,1)
for x in range(9):
    for y in range(9):
        if A[x][y] > max_val:
            max_posi = (x+1,y+1)
            max_val = A[x][y]
print(max_val)
print(*max_posi)