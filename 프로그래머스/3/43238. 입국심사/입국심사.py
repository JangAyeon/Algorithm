def solution(n, times):

    answer = 0
    
    def getCount(t):
        total = 0
        for e in times:
            total+=(t//e)
        print("##: time: ", t, "ppl: ",total)
        return total
    start, end = 1,max(times)*n
    answer = max(times)*n
    while(start<=end):
        mid = (start+end)//2
        ppl = getCount(mid)
        if(ppl<n):
            start = mid+1
        else:
            answer = min(answer, mid)
            end = mid-1
    print(answer)
    return answer