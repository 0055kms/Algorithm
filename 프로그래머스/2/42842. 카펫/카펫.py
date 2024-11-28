def solution(brown, yellow):
    #yc >= yr
    #brown = (2yr + 2yc + 4)
    #yellow = [yr*yc]
    #answer = [yc+2,yr+2]
    
    yr_plus_yc = (brown-4)//2
    yr_x_yc = yellow
    num_list = []
    for i in range(1,yr_plus_yc//2 + 1):
        num_list.append((yr_plus_yc-i,i))
    for yc,yr in num_list:
        if yc*yr == yellow: break
    
    answer = [yc+2,yr+2]
    return answer