function solution(brown, yellow) {
    let answer = [];
    for(let i=1;i<=(yellow**(1/2));i++){
        
   
        if((i+(yellow/i))*2==(brown-4)){
            answer = [i+2, yellow/i+2]
            answer.sort((a,b)=>b-a)
            // console.log(answer)
        }

    }
    return answer;
}