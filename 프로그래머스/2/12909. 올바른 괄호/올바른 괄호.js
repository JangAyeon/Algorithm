function solution(s){
    var answer = true;
    const stack = []
    for(let e of s){
        // console.log(e)
        if(e =="("){
            stack.push(e)
        }else{
            if(stack.length){stack.pop()}
            else{
                answer=false
                break
            }
        }
    }
    // console.log(stack)
    return stack.length?false:answer;
}