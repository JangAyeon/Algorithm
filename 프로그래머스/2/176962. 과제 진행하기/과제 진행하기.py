def solution(plans):
    answer=[]
    stack =[]
    n = len(plans)
    
    for idx in range(n):
        subject, hhmm, time = plans[idx]
        hh, mm= map(int, hhmm.split(":"))
        time = int(time)
        plans[idx][1] = hh*60+mm
        plans[idx][2]=time
    plans.sort(key=lambda x:x[1])
    print(plans)
    for idx in range(n-1):
        gap = plans[idx+1][1]-plans[idx][1]
        stack.append([plans[idx][0], plans[idx][2]])

        while gap and stack:
            if gap>=stack[-1][1]: ## 다음 과제 전까지 현재 과제 다 할 수 있음
                name, time=stack.pop()
                answer.append(name)
                gap-=time
            else: ## 다음 과제 전까지 현재 과제 다 끝내지 못함
                stack[-1][1]-=gap
                gap = 0
    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
    
                


    return answer
