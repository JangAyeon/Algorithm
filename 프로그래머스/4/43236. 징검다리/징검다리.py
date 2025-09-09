def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    def getRemovedCount(dist):
        start = 0
        removed = 0
        for e in rocks:
            gap = e-start
        
            if (gap<dist):
                removed +=1
                continue
            start=e
        return removed
    start = 0
    end = distance
    answer = 0
    while(start<=end):
        mid = (start+end)//2
        count = getRemovedCount(mid)
        if(count<=n):
            start = mid+1
            answer = max(answer, mid)
        else:
            end= mid-1
            

                
    return answer