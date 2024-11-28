def solution(brown, yellow):
    #rows >= cols
    #두수의 곱  (작,크)-같가능 경우의 수들 구해서 튜플형식으로 저장
    #각각 (cols,rows)로 경우 만족하는지 보고 만족한다면 [rows+2,cols+2]를 리턴
    mul = []
    for i in range(1,yellow+1):
        if i > yellow**0.5: break
        if yellow % i == 0:
            mul.append((i,yellow//i))
    for cols,rows in mul:
        if (cols+rows)*2 + 4 == brown:
            return [rows+2,cols+2]
    
    