def solution(distance, rocks, n):
    answer = -float("inf")
    start,end= 0,distance
    rocks.append(distance)
    rocks.sort()
    while start<=end:
        mid = (start+end)//2
        curr =0 
        remove_cnt = 0
        gap_min = float("inf")
        for rock in rocks:

            gap = rock-curr
            if gap <mid:
                
                remove_cnt +=1
            else:
                curr = rock
                gap_min=min(gap, gap_min)
        
        ## 제거 횟수가 주어진 횟수보다 큰 경우
        ## 제거 횟수를 줄이려면 거리를 더 줄여야 함
        if remove_cnt>n:
            end = mid-1

            ##answer = max(answer, max_gap)
        ## 제거 횟수가 주어진 횟수보다 더 작은 경우
        ## 제거 횟수를 늘리려면 주어진 횟수를 더 키워야 함
        else:
            start = mid+1
            answer = max(answer, gap_min)
           
    return answer