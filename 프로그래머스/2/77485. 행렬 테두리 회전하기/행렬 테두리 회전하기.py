from collections import deque

def solution(rows, columns, queries):
    cols = columns
    answer = []
    A = [[0 for _ in range(cols)] for _ in range(rows)]
    num = 1
    for x in range(rows):
        for y in range(cols):
            A[x][y] = num
            num+=1
    for x1,y1,x2,y2 in queries:
        q = deque()        
        for x in range(x1,x2):
            q.append(A[x-1][y1-1])
        for y in range(y1,y2):
            q.append(A[x2-1][y-1])
        for x in range(x2,x1,-1):
            q.append(A[x-1][y2-1])
        for y in range(y2,y1,-1):
            q.append(A[x1-1][y-1])
        answer.append(min(q))
        q.rotate(-1)
        for x in range(x1,x2):
            A[x-1][y1-1] = q.popleft()
        for y in range(y1,y2):
            A[x2-1][y-1] = q.popleft()
        for x in range(x2,x1,-1):
            A[x-1][y2-1] = q.popleft()
        for y in range(y2,y1,-1):
            A[x1-1][y-1] = q.popleft()    
    return answer
    # x: 행(row)
    
"""
    1. 행렬 생성
    2.for x1, y1, x2, y2 in qu:
        q = deque()
        x1 y1     x2 y1    x2 y2    x1 y2
        (x1,y1) 부터 (x2-1,y1) 까지 덱에 넣기
        (x2,y1) 부터 (x2,y2-1) 까지 덱에
        (x2,y2) 부터 (x1+1,y2)
        (x1,y2) 부터 (x1,y1+1)
        
        answer.append(min(q))
        q.rotate()
        while q:
            //아까 그대로 q.popleft() 하면서 배열에 넣기
"""