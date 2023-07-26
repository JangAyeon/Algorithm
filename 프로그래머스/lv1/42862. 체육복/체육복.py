# 1번 예제 : 13 [ 13, 6, 1 ] [ 11, 9, 8, 7] 11
# 2번 예제 : 5, [4, 5], [3, 4] 4 (lost와 reserve에 동시에 있는 경우)
# 3번 예제 : 5, [1, 2, 3], [2, 3, 4] 4 (다른 사람 빌려주기 전에 나 자신부터 빌려줘야 함)
"""
sort를 안했을때 오답이 나오는 반례
학생 4인
분실 2인 [3,1]
여분 2인 [2,4]

sort를 안하게되면 2번 학생의 여분을 3번학생에게 전달하여 분실 1번, 여분 4번 두명의 학생이 체육복 전달을 못하게됩니다
"""

def solution(n, lost, reserve):

    # 1번 예제
    lost.sort()
    reserve.sort()
    
    temp = [] # 빌리지 못한 사람
    
    # 3번 예제
    for i in lost: # 일단 나 자신부터 빌려주기 
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            
    for idx in range(len(lost)):
        x = lost[idx]
        if x in reserve: # 2번 예제
            reserve.remove(x)
        elif x-1 in reserve:
            reserve.remove(x-1)
        elif x+1 in reserve:
            reserve.remove(x+1)
        else:
            temp.append(x)

    answer = n-len(temp)
    return answer