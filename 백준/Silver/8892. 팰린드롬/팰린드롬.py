import sys
input = sys.stdin.readline

T = int(input())
def p():
    k = int(input())
    ar = []
    for _ in range(k): ar.append(input().rstrip())
    for i in range(k):
        for j in range(k):
            if i != j:
                new = ar[i] + ar[j]
                if new == new[::-1]:
                    print(new); return
    print(0); return
for _ in range(T):
    p()