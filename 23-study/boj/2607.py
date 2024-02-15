import sys
input = sys.stdin.readline

n = int(input())

standard = list(input().strip())
words = [list(input().strip()) for _ in range(n-1)]
#print(words)

## 단어의 각 문자 갯수 사전 반환하는 함수
def createCountDic(word):
    dic = dict()
    for char in word:
        if char not in dic.keys():
            dic[char]=1
        else:
            dic[char]+=1
    return dic
    
## 구성의 차이 구하는 함수
def calcDic(standardDic, wordDic):
    diff = 0
    ## 기준 문자열과 비교 문자열에 동시에 있는 문자
    commonKeys = set(standardDic.keys()) & set(wordDic.keys())
    ## 기준 문자열에만 존재하는 문자
    standardOnly = set(standardDic.keys()) - set(wordDic.keys())
    ## 비교 문자열에만 존재하는 문자
    wordOnly = set(wordDic.keys()) - set(standardDic.keys())
    #print(commonKeys, standardOnly, wordOnly)
    
    for char in commonKeys:
        diff += abs(standardDic[char]-wordDic[char])
    for char in standardOnly:
        diff+=standardDic[char]
    for char in wordOnly:
        diff+=wordDic[char]
    return diff

## 구성의 차이에 대해 비슷한 단어인지 판별하는 함수
def isAble(diff, word, standard):
    if diff==0 or diff==1:
        return True
    if diff==2 and (len(word)==len(standard)):
        return True
    else:
        return False

standardDic = createCountDic(standard)
answer=0
for word in words:
    wordDic = createCountDic(word)
    diff = calcDic(standardDic, wordDic)
    if isAble(diff, word, standard):
        answer+=1
print(answer)
