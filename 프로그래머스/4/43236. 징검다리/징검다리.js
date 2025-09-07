function solution(distance, rocks, n) {
    var answer = 0;
    function getCount(dist){
        let [gap_min, removed, curr] = [1000000000,0,0]
        for(let next_ of rocks){
            const gap = next_ - curr
            if(gap>=dist){ /* 최소 간격이 주어진 dist로 유지됨 */
                curr = next_
                gap_min = Math.min(gap, gap_min)
            }else{ /* 삭제하지 않으면 최소 간격이 gap이 됨 */
                removed +=1
            }
        }
        return [removed, gap_min]
    }
    
    
    rocks = [...rocks, distance]
    rocks.sort((a,b)=>a-b)
    console.log(rocks)
    answer = 0
    let [start, end]=[0, distance]
    
    while(start<=end){
        const mid = Math.floor((start+end)/2)
        const [removed_count, gap_min] = getCount(mid)
       
        /* 더 많이 없애야 하는 경우: 간격 길이 줄여야 함 */
        if(removed_count>n){
            console.log(removed_count, gap_min,n, mid)
            end = mid-1
            
        }
        else{
            console.log(removed_count, gap_min,n)
            start = mid+1
            answer = Math.max(answer, gap_min)
        }
    }
    return answer;
}