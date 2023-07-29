
def solution(n, lost, reserve):
    
    # 여벌 체육복 가져왔는데 도난 당하는 경우 발생에 따른 차집합 처리
    # lost와 reserve 동시에 등장하는 학생은 본인꺼 본인이 입어야하는 상황으로 아예 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    # lost_set으로 순회 돌면 안되는 이유
    # 여벌 빌려줄 수 있는 학생 있는 경우 pop 하는 이러면 
    # 순회는 도는 와중에 해당 집합에서 변경 발생해 에러!
    for s in reserve_set: 
        if s-1 in lost_set:
            lost_set.remove(s-1)
        elif s+1 in lost_set:
            lost_set.remove(s+1)
            
    answer = n - len(lost_set)
    return answer