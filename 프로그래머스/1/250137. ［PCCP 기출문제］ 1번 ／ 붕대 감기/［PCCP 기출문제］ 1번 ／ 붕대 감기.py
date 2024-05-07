"""
문제에서 주어진 예시 풀이 과정을 보면 공격을 당하기 전까지 회복을 하고 공격을 당하는 것을 알 수 있습니다. 고로 글쓴이의 로직인 공격을 먼저 깎고 health <= 0 이면 return -1 하는 것은 오류 라고 생각 합니다.
"""


def solution(bandage, health, attacks):
    end = attacks[-1][0]
    curr_health = health
    s = 0
    for t in range(end+1):
        if t==attacks[0][0]:
            curr_health-=attacks[0][1]
            attacks.pop(0)
            if curr_health<=0: ## 공격 받아 죽은 경우
                return -1
            else:
                s = 0
        else: ## 공격이 아닌 경우
            s+=1 ## 연속
            if s==bandage[0]: ## 연속 회복 성공
                curr_health = min(health, curr_health+bandage[2]+bandage[1])
                s=0
            else:
                curr_health=min(health, curr_health+bandage[1])
        ##print(t, curr_health)
            
    answer = curr_health
    return answer