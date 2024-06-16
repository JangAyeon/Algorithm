import math 
def solution(r1, r2):

    [a,b] = [r1,r2] if r1>r2 else [r2,r1]
    ##print("##",a,b)
    answer = 0
    inner = 0
    for r in range(1,r2+1):
        if r<r1:
            end = int(math.sqrt(r2**2-r**2)) 
            start = math.ceil(math.sqrt(r1**2-r**2))
        else:
            end = int(math.sqrt(r2**2-r**2) )
            start = 0
        answer+=(end-start+1)

    answer*=4



    return answer
