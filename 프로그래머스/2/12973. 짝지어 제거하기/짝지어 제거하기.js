function solution(word)
{
    var answer = -1;
    const stack = []
    for(let s of word ){
        if(stack.length>0 && stack[stack.length-1]===s){
            stack.pop()
        }
        else{
            stack.push(s)
        }
        // console.log(stack)
    }
    if (stack.length>0){
        answer = 0
    }
    else{
        answer=1
    }
 
    

    return answer;
}