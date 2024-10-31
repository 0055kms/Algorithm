import sys
input = sys.stdin.readline
N,M = map(int,input().split()) #N권 M더미
for _ in range(M):
    k = int(input())
    num = [x for x in map(int,input().split())]
    sort_num = sorted(num,reverse = True)
    for i,v in enumerate(num):
        if v != sort_num[i]:
            print("No")
            sys.exit(0)
print("Yes")