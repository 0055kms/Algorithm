import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def d(s,e):
    diff = e-s
    if diff == 1: return
    for i in range(s+diff//3,s+diff//3*2):
        A[i] = ' '
    d(s,s+diff//3)
    d(s+diff//3*2,e)

while True:
    try:
        N = int(input())
        A = ['-'] * (3**N)
        d(0,len(A))
        print(''.join(A))
    except: break


"""
0 27

9 18
0 9   18 27
"""