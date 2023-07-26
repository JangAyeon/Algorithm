# 13 [ 13, 6, 1 ] [ 11, 9, 8, 7] 11
# 5, [4, 5], [3, 4] 4 (lost와 reserve에 동시에 있는 경우)
# 5, [1, 2, 3], [2, 3, 4] 4
def solution(n, lost, reserve):
    #n = 5
    #lost = [1, 2, 3]
    #reserve = [2, 3, 4]
    lost.sort()
    reserve.sort()
    temp = [] # 빌리지 못한 사람
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            
    for idx in range(len(lost)):
        x = lost[idx]
        if x in reserve:
            reserve.remove(x)
        elif x-1 in reserve:
            reserve.remove(x-1)
        elif x+1 in reserve:
            reserve.remove(x+1)
        else:
            temp.append(x)

    answer = n-len(temp)
    return answer