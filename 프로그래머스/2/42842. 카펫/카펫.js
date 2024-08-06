function solution(brown, yellow) {
    let answer = [];
    for(let i=1;i<=Math.sqrt(yellow);i++){
        
   
        if((i+(yellow/i))*2==(brown-4)){
            answer = [yellow/i+2,i+2]
            // answer.sort((a,b)=>b-a)
            // console.log(answer)
        }

    }
    return answer;
}