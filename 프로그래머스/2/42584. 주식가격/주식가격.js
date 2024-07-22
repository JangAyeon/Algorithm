function solution(prices) {
    var answer = new Array(prices.length).fill(0);
    const stack = []
    for(let idx=0;idx<prices.length;idx++){

        while(prices[idx]<prices[stack[stack.length-1]]){
            answer[stack.pop()]+=1       
        }
        for(let i of stack){
                answer[i]+=1
        }
        stack.push(idx)


        
        // console.log(answer, stack,prices[idx])
    }
    
    return answer;
}