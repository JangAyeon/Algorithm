function isAble(n){
    for (let i=n-1;i>=2;i--){

        if (n%i==0){

            return true
        }
        
    }
    return false
}


function solution(n) {
    let answer = []
    for(let i=4;i<=n;i++){
        if(isAble(i)){

            answer.push(i)
        }
    }
    return answer.length;
}