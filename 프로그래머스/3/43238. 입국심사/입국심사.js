function solution(n, times) {
    // 주어진 시간 (t) 동안 사람 몇명 심사 가능한지
    // t 동안 - n명 이상 처리 가능 -> t 줄이기
    //       - n명 미만 처리 가능 -> t 늘이기
    
    function getCnt(limit){
        let count = 0
        for(let time of times){
            count +=Math.floor(limit/time)
        }
        return count
    }
    let answer = 1000000000*n
    let [left, right] = [1,1000000000*n]
    while(left<=right){
        let mid=Math.ceil((left+right)/2)
        const cnt = getCnt(mid)
        if(cnt>=n){
            right = mid-1
            answer = Math.min(answer, mid)
        }else{
            left = mid+1
        }
    }
    
    return answer;
}