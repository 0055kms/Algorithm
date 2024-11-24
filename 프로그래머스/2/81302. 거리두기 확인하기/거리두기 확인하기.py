from collections import deque


def solution(places):
    answer = []
    def find(place):
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        #P: 사람
        #O: 빈 테이블
        #X: 파티션은 이동 불가 파티션 사이에 둬도 거리 지킨 것
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    q = deque([(x,y,0)])
                    visit = [[False for _ in range(5)] for _ in range(5)]
                    visit[x][y] = True
                    while q:
                        cx,cy,cd = q.popleft()
                        if cd == 2: continue
                        for dx,dy in dir:
                            nx,ny,nd = dx+cx,dy+cy,cd+1
                            if not (0<=nx<=4 and 0<=ny<=4): continue
                            if visit[nx][ny] or place[nx][ny] == 'X': continue
                            if place[nx][ny] == 'P': return 0
                            visit[nx][ny] = True
                            q.append((nx,ny,nd))
        return 1      
                            
        
    for place in places:
        answer.append(find(place))
    
    return answer