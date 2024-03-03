import sys
from itertools import combinations as c
input = sys.stdin.readline
N = int(input())
people = [x for x in range(N)]
board = [[*map(int,input().split())] for _ in range(N)]
min_val = sys.maxsize
for team1 in c(people,N//2):
    team2 = [x for x in people if x not in team1]
    tmp1 , tmp2 = 0,0
    for s,e in c(team1,2):
        tmp1 += (board[s][e]+board[e][s])
    for s,e in c(team2,2):
        tmp2 += (board[s][e]+board[e][s])
    tmp_val = abs(tmp1-tmp2)
    min_val = min(tmp_val,min_val)

print(min_val)