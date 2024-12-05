from collections import deque

def solution(places):
    dir = [(0,-1),(0,1),(-1,0),(1,0)]
    answer = []
    def f(place):
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    visit = [[False for _ in range(5)] for _ in range(5)]
                    D = [[0 for _ in range(5)] for _ in range(5)]
                    visit[x][y] = True
                    q = deque([(x,y)])
                    while q:
                        cx,cy = q.popleft()
                        for dx,dy in dir:
                            nx,ny = cx+dx,cy+dy
                            if 0 <= nx <= 4 and 0 <= ny <= 4 and visit[nx][ny] == False and place[nx][ny] != 'X':
                                if place[nx][ny] == 'P': return 0
                                D[nx][ny] = D[cx][cy] + 1
                                visit[nx][ny] = True
                                if D[nx][ny] < 2: q.append((nx,ny))
        return 1
    
    for p in places:
        answer.append(f(p))
    return answer