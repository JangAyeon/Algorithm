

def solution(word):
    cntX =cntY= 0
    answer=0
    for idx in range(len(word)):
        if cntX==0:
            start = idx
            cntX+=1
        else:
            if word[idx]==word[start]:
                cntX+=1
            else:
                cntY+=1
        if cntX==cntY:
            print(word[start:idx+1])
            answer+=1
            cntX =cntY= 0
            
        
    ## print(answer, start, cntX, cntY, idx)
    if cntX!=0:
        answer+=1
    return answer