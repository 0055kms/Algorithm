def solution(n):
    nx,ny = -1,0
    k = 0
    num = 1
    A = [[0] * (i+1) for i in range(n)]
    for i in range(n,0,-1):
        for _ in range(i):
            if k == 0:
                nx += 1
            elif k == 1:
                ny += 1
            else:
                nx -= 1
                ny -= 1
            A[nx][ny] = num
            num += 1
        k = (k+1)%3
    
    answer = [i for j in A for i in j]
    return answer

"""
ㅡ
ㅡㅡ
ㅡㅡㅡ
ㅡㅡㅡㅡ
ㅡㅡㅡㅡㅡ
아래 5   오른 4   왼위 3
아래 2   오른 1   왼위 0
"""