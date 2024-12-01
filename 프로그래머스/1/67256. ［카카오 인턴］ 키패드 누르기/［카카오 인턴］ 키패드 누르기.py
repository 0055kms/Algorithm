def solution(numbers, hand):
    answer = []
    posi = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),'*':(3,0),0:(3,1),'#':(3,2)}
    
    def calc(s,e):
        x1,y1 = posi[s]
        x2,y2 = posi[e]
        return abs(x1-x2) + abs(y1-y2)
        
    l,r = '*','#'
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            l = num
            answer.append('L')
        elif num == 3 or num == 6 or num == 9:
            r = num
            answer.append('R')
        else:
            if calc(l,num) > calc(r,num):
                r = num
                answer.append('R')
            elif calc(r,num) > calc(l,num):
                l = num
                answer.append('L')
            else:
                if hand == 'right':
                    r = num
                    answer.append('R')
                else:
                    l = num
                    answer.append('L')
    return ''.join(answer)