import sys
input = sys.stdin.readline
R,C = map(int,input().split())
ar = [[x for x in map(int,input().split())] for _ in range(R)]
rA,cA,bA = 0,0,R*C
for x in range(R):
    rA += ar[x][0]
    for y in range(C-1):
        if ar[x][y] < ar[x][y+1]: rA += (ar[x][y+1]-ar[x][y])

for y in range(C):
    cA += ar[0][y]
    for x in range(R-1):
        if ar[x][y] < ar[x+1][y]: cA += (ar[x+1][y]-ar[x][y])

print((rA+cA+bA)*2)
