from collections import deque

def solution(m, n, puddles):
    dir = [(0,1),(1,0)]
    answer = 0
    r,c = n,m
    A = [[0 for _ in range(c)] for _ in range(r)]
    for tc,tr in puddles:
        A[tr-1][tc-1] = -1
    
    A[0][0] = 1
    q = deque()
    q.append((0,0))
    while q:
        cx,cy = q.popleft()
        for dx,dy in dir:
            nx,ny = dx+cx,dy+cy
            if 0 <= nx <= r-1 and 0 <= ny <= c-1 and A[nx][ny] != -1:
                A[nx][ny] += A[cx][cy]
                if (nx,ny) not in q: q.append((nx,ny))
    
    return A[r-1][c-1]%1000000007