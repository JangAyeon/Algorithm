function solution(last, rocks, N) {
    let answer = 0;
    rocks.sort((a,b)=>a-b)
    rocks = [...rocks,last]
    const M = rocks.length
    let [left, right] = [1, last]
    // console.log(rocks)
    function getRemoved(target){
        let [start, count] = [0,0]
        for(let i=0;i<M;i++){
            const gap = rocks[i]-start
            // console.log(start, rocks[i], count)
            if(gap>=target){start = rocks[i]}
            else{count+=1}
        }
        
        return count
    }
    while(left<=right){
        const mid = Math.ceil((left+right)/2)
        const count = getRemoved(mid)
        // console.log("####",count, mid)
        if(count>N){
            right = mid-1
        }else{
            left=mid+1
            answer = mid
            
        }
    }
    return answer;
}