def solution(answers):
    p1 = [1,2,3,4,5] # 5
    p2 = [2,1,2,3,2,4,2,5] # 8
    p3 = [3,3,1,1,2,2,4,4,5,5] # 10
    check = [0] * 3
    for i in range(len(answers)):
        if answers[i] == p1[i%5]: check[0] += 1
        if answers[i] == p2[i%8]: check[1] += 1
        if answers[i] == p3[i%10]: check[2] += 1
    
    max_val = max(check)
    ans = []
    for i in range(3):
        if check[i] == max_val: ans.append(i+1)
    return ans