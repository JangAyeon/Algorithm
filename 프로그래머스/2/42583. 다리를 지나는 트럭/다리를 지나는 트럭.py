"""

출처를 통해서 보니 다리를 건너는데 필요한 시간이 bridge_length만큼 드는거 같아요
예제에서는 위 변수가 2이기 때문에 처음 무게가 7인 트럭이 지나는데 2초가 걸립니다.
즉 1~2초 구간에는 무게가 7인 트럭이 다리위에 있어서 무게 4인 트럭이 다리위에 못올라가죠
3초가 됐을 대 무게가 7인 트럭이 다 지나가서 다리위에 없으므로 무게가 4인 트럭이 지나가기 시작합니다.
무게가 4인 트럭은 3,4초 동안 다리를 지나고 5초가 됐을 때는 다리를 건너있게 되는거죠
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    que = deque()
    w = truck_weights.pop(0)
    que.append([bridge_length,w])

    while que:
        answer+=1
        load = []
        sum_=count=0
        while que:
            time, value = que.popleft()
            if time-1>0:
                load.append([time-1,value ])
                sum_+=value
                count+=1
        for m in load:
            que.append(m)
        if truck_weights and sum_+truck_weights[0]<=weight and count+1<=bridge_length:
            w = truck_weights.pop(0)
            que.append([bridge_length, w])
        ##print(truck_weights, que,answer)
                
    return answer