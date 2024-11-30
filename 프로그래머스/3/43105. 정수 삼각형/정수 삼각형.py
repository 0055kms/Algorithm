def solution(triangle):
    answer = 0
    l = len(triangle)
    if l == 1: return triangle[0][0]
    
    for h in range(1,l): # 1 2 3 4
        triangle[h][0] += triangle[h-1][0]
        triangle[h][h] += triangle[h-1][h-1]
        for i in range(1,h): #() (1) (1,2) (1,2,3) 
            triangle[h][i] += (max(triangle[h-1][i],triangle[h-1][i-1]))
    return max(triangle[-1])
    