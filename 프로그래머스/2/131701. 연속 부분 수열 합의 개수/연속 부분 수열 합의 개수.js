function solution(elements) {
    const dp = [Array.from({length:elements.length},()=>0)]
    const n = elements.length
    for(let i=0;i<n;i++){
        const row = []
        for(let j=0;j<n;j++){
            const prevIdx = (j-1+n)%n
            const number = dp[dp.length-1][prevIdx]+elements[j]
            row.push(number)
        }
        dp.push(row)
    }
    const flatted = dp.flat()
    const answer = (new Set(flatted).size-1)
    return answer;
}