

function solution(n) {
    let maxN = 10;
    let answer = 1;
    for(let i=1;i<=maxN;i++){
        answer*=i
        if(answer==n){return i}
        else if(answer>n){return i-1}

    }
    return answer;
}