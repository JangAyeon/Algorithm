def solution(targets):
    
    ## 시작 시간이 빠르고 지속 시간이 긴 것 순으로 나열
    targets.sort(key=lambda x:(x[1], (x[0])))
    ##print(targets)
    curr_start, curr_end = targets[0]
    count = 1
    for next_start, next_end in targets[1:]:
        ##print(curr_start, curr_end, next_start, next_end, count)
        ## 구간이 겹치는 게 있으면 그냥 넘기기
        if curr_end<=next_start:
            curr_start =next_start
            curr_end = next_end
            count+=1
            
        


    answer = count
    return answer