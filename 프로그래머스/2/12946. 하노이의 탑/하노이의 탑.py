import sys
sys.setrecursionlimit(10**6)

def solution(n):
    def get_other(s,e):
        if not (s == 1 or e == 1): return 1
        if not (s == 2 or e == 2): return 2
        if not (s == 3 or e == 3): return 3
    """
    1 3 7 ..
    n개 옮기기 작업
    1. 1번의 n-1개를 2번으로
    2. 1번의 n번을 3번으로
    3. 2번의 n-1개를 3번으로
    """
    def move(s,e,n): #s번에서 e번으로 n개 옮길 때 방법을 2차원 배열로 return
        method = []
        if n == 1: return [[s,e]]
        o = get_other(s,e)
        method.extend(move(s,o,n-1))
        method.append([s,e])
        method.extend(move(o,e,n-1))
        return method
    print(move(1,3,2))
    print(move(2,3,2))
    return move(1,3,n)