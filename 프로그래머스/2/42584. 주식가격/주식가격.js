function solution(prices) {
    const N = prices.length
    const answer = Array.from({length:N}).fill(0);
    const stack = [0]
    for(let i=1;i<N;i++){
        while(stack.length>0 && prices[stack[stack.length-1]]>prices[i]){
            j=stack.pop()
            answer[j] = i-j
        }
        stack.push(i)
        
    }
    while(stack.length>0){
        const j = stack.pop()
        answer[j] = N-1-j
    }

    console.log(answer, stack)

    return answer;
}