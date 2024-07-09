function solution(numbers) {
    var answer = [];
    let n = numbers.length
    
    for (let i=0;i<n;i++){
        answer.push(0)
    }

    let stack = [0]
    for(let i=1;i<n;i++){
        while (stack.length>0 &&numbers[stack[stack.length-1]]<numbers[i]){
            answer[stack.pop()]=numbers[i]
        }
            
        stack.push(i)
    }
    
    while (stack.length!=0){
        answer[stack.pop()]=-1
    }
    
    return answer;
}