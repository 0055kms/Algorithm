from collections import deque

def solution(maps):
    answer = -1
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    r,c = len(maps),len(maps[0])
    visit = [[False for _ in range(c)] for _ in range(r)]
    D = [[0 for _ in range(c)] for _ in range(r)]
    D[0][0] = 1
    visit[0][0] = True
    q = deque([(0,0)])
    while q:
        cx,cy = q.popleft()
        for dx,dy in dir:
            nx,ny = cx+dx,cy+dy
            if 0 <= nx <= r-1 and 0 <= ny <= c-1 and not visit[nx][ny] and maps[nx][ny]:
                visit[nx][ny] = True
                D[nx][ny] = D[cx][cy] + 1
                q.append((nx,ny))
    
    if not visit[r-1][c-1]: return -1
    else: return D[r-1][c-1]
    """
    1 0 1 1 1
    1 0 1 0 1
    1 0 1 1 1 
    1 1 1 0 1
    0 0 0 0 1
    
    """