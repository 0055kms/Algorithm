import sys
input = sys.stdin.readline

def find_year(M, N, x, y):
    k = x
    while k <= M * N:
        if (k - 1) % N + 1 == y:
            return k
        k += M
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(find_year(M, N, x, y))
