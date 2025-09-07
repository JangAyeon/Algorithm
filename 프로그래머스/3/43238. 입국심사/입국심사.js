function solution(n, times) {

    
    function getCount(t){
        let total = 0
        for(let e of times){
            total+=Math.floor(t/e)
        }
        console.log(`### time: ${t} ppl: ${total}`)
        return total
    }
    let [start, end] = [1, Math.max(...times)*n]
    let answer = Math.max(...times)*n
    while(start<=end){
        mid = Math.floor((start+end)/2)
        ppl = getCount(mid)
        if(ppl<n){start=mid+1}
        else{
            answer = Math.min(answer, mid)
            end = mid-1
        }
        
    }
    console.log(answer)
    return answer;
}