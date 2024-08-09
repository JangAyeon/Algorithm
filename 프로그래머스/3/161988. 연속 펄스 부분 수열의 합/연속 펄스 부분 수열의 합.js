


function solution(sequence) {
    const pulse = [[-1,1],[1,-1]]
    let answer = Infinity;
    for (let p of pulse){
        const arr = [0]
        for(let idx=0;idx<sequence.length;idx++){
            ///console.log(sequence[idx],p[idx%2],sub[idx])
            arr.push(sequence[idx]*p[idx%2]+arr[arr.length-1])
        }
        //subSum(sub)
        const max_ = arr.reduce((max, v) => max >= v ? max : v, -Infinity);
        const min_ = arr.reduce((min, v) => min <= v ? min : v, Infinity);
        
        answer = Math.abs(max_-min_)
    }

   
    return answer;
}