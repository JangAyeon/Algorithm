function solution(numbers) {
    n = numbers.length
    const sum_ = new Set()
    for(let i=0;i<n;i++){
        for(let j=i+1;j<n;j++){
            const number = numbers[i]+numbers[j]
            sum_.add(number)
            
        }
    }
    const answer = Array.from(sum_)
    answer.sort((a,b)=>a-b)
    console.log(answer)
    
    return answer;
}