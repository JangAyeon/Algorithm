def timeToMin(time):
    hh,mm = map(int,time.split(":"))
    return hh*60+mm

## 현재 시간과 다음 과제 꼭 시작해야 하는 시간(=gap) 구함
    ## gap 내에 현재 과제 다 할 수 있는 경우 => 정답에 추가
    ## gap 내 현재 과제 다 못하는 경우 => 남은 시간 갱신 해 

def solution(plans):
    answer = []
    stack = []
    plans.sort(key=lambda x:x[1]) ## 과제 꼭 시작해야 하는 순서대로 나열
    
    for idx in range(0, len(plans)-1):
        curr_, next_ = plans[idx], plans[idx+1]
        gap = timeToMin(next_[1])- timeToMin(curr_[1])
        stack.append([curr_[0], int(curr_[2])])
        while stack and gap:
            if stack[-1][-1]<=gap: #
                name, time = stack.pop()
                answer.append(name)
                gap-=time
            else:
                stack[-1][-1]-=gap
                gap=0
    answer.append(plans[idx+1][0])
    while stack:
        name, time = stack.pop()
        answer.append(name)


        
    return answer