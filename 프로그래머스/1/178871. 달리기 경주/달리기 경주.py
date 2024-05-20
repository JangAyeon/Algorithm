from collections import deque

def solution(players, callings):
    aDic,bDic={},{}
    for i in range(len(players)):
        p=players[i]
        aDic[i]=p
        bDic[p]=i

    

    for player in callings:
        a=bDic[player]  ## 추월 선수 (player,a)
        p=aDic[a-1] ## 추월 당하는 선수 (p, a-1)
        bDic[player]=a-1
        bDic[p]=a
        aDic[a-1]=player
        aDic[a]=p
    answer = []
    for i in range(len(players)):
        answer.append(aDic[i])
    

        
    return answer