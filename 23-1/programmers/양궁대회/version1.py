from copy import deepcopy

max_diff = 0
answer = []

def calcScore(apeach, lyan):
    Ascore, Lscore = 0, 0
    for i in range(11):
        if ((apeach[i]==0) and (lyan[i] ==0)):
            continue
        elif apeach[i]>=lyan[i]:
            Ascore+=(10-i)
        else:
            Lscore+=(10-i)
    return Lscore - Ascore

def dfs(apeach, lyan, n, i):
    
    global max_diff, answer
    if i == 11: # 모든 화살판 점수 다 돈 경우 (1점 ~ 10점)
        if n!=0:
            lyan[10] = n # 남은 화살 다 0점 쏴야함
        # 점수 계산
        diff_score = calcScore(apeach, lyan)
        # 점수 더 낮거나 비긴 경우 : 진 거임
        if diff_score<=0:
            return
        # 점수 더 높은 경우 : 이긴 거임
        result = deepcopy(lyan)
        if max_diff<diff_score: # 승리 - 더 큰 점수 차 등장 
            answer = [result] # 아예 답안 케이스 교체 
            max_diff = diff_score
            return
        
        if max_diff == diff_score: # 승리 - 동일 점수 차 등장 
            answer.append(result) # 답안 케이스 추가 
        return
        
        
    
    # 화살 쏘는 경우
    if apeach[i]<n: # 어피치가 쏜 갯수보다 더 많이 쏠수 있음
        
        cnt = apeach[i]+1 # 어피치가 쏜 갯수보다 1개 더 쏨
        lyan.append(cnt)
        #print("yes",apeach, lyan,n,i)
        dfs(apeach, lyan, n - cnt, i+1)
        lyan.pop()
    
    # 화살 쏘지 않는 경우
    cnt = 0
    lyan.append(cnt)
    #print("no",apeach, lyan,n,i)
    dfs(apeach, lyan, n-cnt, i+1)
    lyan.pop()

def solution(n, apeach):
    global answer, max_diff
    dfs(apeach, [],n,0)
    if answer==[]:
        return [-1]
    answer.sort(key=lambda x: x[::-1], reverse = True)
    return answer[0]
    
    
