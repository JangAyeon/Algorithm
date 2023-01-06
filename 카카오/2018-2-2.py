# 2018 KAKAO BLIND RECRUITMENT [1차] 다트 게임

import re

def solution(dartResult):
    ans=[]
    pattern = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
    token = pattern.findall(dartResult)
    # [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]

    cal = {
        "S": lambda val : val,
        "D" : lambda val : val**2,
        "T": lambda val : val**3
    }
    
    for i, j, k in token:
       #print(i,j,k)
        if j == "S":
            tmp = cal["S"](int(i))
        elif j == "D":
            tmp = cal["D"](int(i))
        elif j == "T":
            tmp = cal["T"](int(i))
        if k=="*":
            tmp *=2
            if ans:
                ans[-1]*=2
        elif k =="#":
            tmp *=-1
        ans.append(tmp) 
    #print(ans)
    return sum(ans)

#print(solution("1S2D*3T"))