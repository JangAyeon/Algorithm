def getCount(str):
    countDic = {}
    keys = list(set(str))
    for key in keys:
        countDic[key] = str.count(key)
    return countDic

def getSplit(str):
    splitDic={}
    keys = list(set(str))
    for key in keys:
        splitDic[key] = 0
    flag = False
    for i in range(0, len(str)-1):
        #print(str[i],str[i+1])
        if str[i]!=str[i+1]:
            splitDic[str[i]]+=1
            flag = True
    if flag:
        splitDic[str[-1]]+=1
            
    #print(splitDic)
    return  splitDic
            


def solution(str):
    answer = []
    countDic = getCount(str)
    splitDic = getSplit(str)
    
    for key in countDic.keys():
        if countDic[key]>=2 and splitDic[key]>1:
            answer.append(key)
    if len(answer)>0:
        answer.sort()
        answer = "".join(answer)
    else:
        answer = "N"
    #print(answer, countDic, splitDic)
    return answer