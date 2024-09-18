import sys
input = sys.stdin.readline
from collections import defaultdict
time = 0
fr,fc,fk = map(int,input().split())
A = [[*map(int,input().split())] for _ in range(3)]
R,C = 3,3
while time != 101:
    if 0<=fr-1<=R-1 and 0<=fc-1<=C-1 and A[fr-1][fc-1] == fk:
        print(time)
        sys.exit()
    if R >= C: #R연산
        max_len_R = -float("inf")
        for x in range(R):
            dict = defaultdict(int)
            new = []
            for y in range(C):
                if A[x][y] != 0: dict[A[x][y]] += 1
            items = list(dict.items())
            items.sort(key = lambda x: (x[1],x[0]))
            for k,v in items[:50]:
                new.append(k)
                new.append(v)
            max_len_R = max(max_len_R,len(new))

        new_A = [[0] * max_len_R for _ in range(R)]

        for x in range(R):
            dict = defaultdict(int)
            new = []
            for y in range(C):
                if A[x][y] != 0: dict[A[x][y]] += 1
            items = list(dict.items())
            items.sort(key = lambda x: (x[1],x[0]))
            for k,v in items[:50]:
                new.append(k)
                new.append(v)
            for i in range(len(new)):
                new_A[x][i] = new[i]
        C = max_len_R
        A = new_A

    else: #C
        max_len_C = -float("inf")
        for y in range(C):
            dict = defaultdict(int)
            new = []
            for x in range(R):
                if A[x][y] != 0: dict[A[x][y]] += 1
            items = list(dict.items())
            items.sort(key=lambda x: (x[1], x[0]))
            for k, v in items[:50]:
                new.append(k)
                new.append(v)
            max_len_C = max(max_len_C, len(new))

        new_A = [[0] * C for _ in range(max_len_C)]

        for y in range(C):
            dict = defaultdict(int)
            new = []
            for x in range(R):
                if A[x][y] != 0: dict[A[x][y]] += 1
            items = list(dict.items())
            items.sort(key=lambda x: (x[1], x[0]))
            for k, v in items[:50]:
                new.append(k)
                new.append(v)
            for i in range(len(new)):
                new_A[i][y] = new[i]
        R = max_len_C
        A = new_A
    time += 1
print(-1)