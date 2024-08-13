import sys
input = sys.stdin.readline

def num(a):
    return str(a) * 10
N = int(input().strip())
ar = [x for x in map(int, input().split())]
ar.sort(key=lambda x: (num(x)), reverse=True)

if ar[0] == 0:
    print(0)
else:
    for i in ar:
        print(i, end='')
