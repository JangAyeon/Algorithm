def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.append(distance)
    rocks.sort()
    ### 주어진 gap으로 제거된 바위 갯수 구하는 함수
    def getCount(dist):
        curr = 0
        removed = 0
        gap_min = 1000000000
        for next_ in rocks:
            gap = next_-curr
            if(dist>gap):
                removed+=1
            else:
                curr = next_
                gap_min = min(gap_min, gap)
                
        return [removed, gap_min]
    
    while(start<=end):
        mid=(start+end)//2
        count, gap_min = getCount(mid)
        if count>n:
            end = mid-1
        else:
            start = mid+1
            answer = max(answer, gap_min)
                
    return answer