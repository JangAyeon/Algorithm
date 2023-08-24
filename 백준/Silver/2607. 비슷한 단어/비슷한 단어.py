import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]
#print(arr)


    
# 같은 구성의 차이 구하는 함수
def getDiff(sampleDic, stringDic):
    diff = 0 
    sampleKeys = list(sampleDic.keys())
    stringKeys = list(stringDic.keys())
    keys = list(set(sampleKeys+stringKeys))
    for key in keys:
        if key not in sampleKeys:
            diff +=stringDic[key]
        elif key not in stringKeys:
            diff +=sampleDic[key]
        else:
            diff+=abs(sampleDic[key]-stringDic[key])
            
    return diff
    
# 구성의 차이가 "비슷한 차이"에 해당하는지 확인하는 함수
def isSameWord(diff, sampleDic, stringDic):
    if diff ==0 or diff==1:
        return True
    # 교체 
    if diff==2 and sum(sampleDic.values())==sum(stringDic.values()):
        return True
    else:
        return False


# 문자와 그 갯수를 딕셔너리 형태로 반환        
def getCountDic(sample, string):
    sampleDic = dict()
    stringDic = dict()
    for i in sample:
        if i not in sampleDic:
            sampleDic[i]=1
        else:
            sampleDic[i]+=1
    for i in string:
        if i not in stringDic:
            stringDic[i]=1
        else:
            stringDic[i]+=1
    #print(sampleDic, stringDic)
    return sampleDic, stringDic
        

# 한문자 추가, 한문자 빼기, 한 문자 교체 => 같은 구성

answer = 0
sample = arr[0]
compare = arr[1:]

for string in compare:
    sampleDic, stringDic = getCountDic(sample, string)
    diff = getDiff(sampleDic, stringDic)
    if isSameWord(diff, sampleDic, stringDic):
        #print("diff: ",diff, string)
        answer+=1
print(answer)