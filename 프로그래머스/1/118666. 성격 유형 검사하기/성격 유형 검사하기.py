def getScore( score):
    if 1<=score<=3:
        result = [3,2,1]
        return 0, result[score-1]
    elif score==4:
        return -1, -1
    else:
        result = [1,2,3]
        return 1, result[score-5]
    



def solution(survey, choices):

    result = {"R":0, "T":0, "C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    n = len(survey)
    for idx in range(n):
        a, b = getScore((choices[idx]))
        key = survey[idx][a]
        if a==-1:
            continue
        result[key]+=b
    answer=""
    for a,b in [["R","T"], ["F","C"],["J","M"], ["A","N"]]:
        if result[a]>result[b]:
            answer+=a
        elif result[a]==result[b]:
            answer+=sorted([a,b])[0]
            
        else:
            answer+=b
    print(answer)



    return answer