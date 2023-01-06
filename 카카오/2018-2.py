import re

def solution(dartResult):
    ans=[]
    pattern = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
    token = pattern.findall(dartResult)
    for i, j, k in token:
        print(i,j,k)
        if j == "S":
            tmp = int(i)
        elif j == "D":
            tmp = int(i)**2
        elif j == "T":
            tmp = int(i)**3
        if k=="*":
            tmp *=2
            if ans:
                ans[-1]*=2
        elif k =="#":
            tmp *=-1
        ans.append(tmp) 
    #print(ans)
    return sum(ans)

print(solution("1S2D*3T"))