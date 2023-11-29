function solution(numbers, k) {
    let n=1;
    let turn=0
    while(n!=k){
        turn=(turn+2)%numbers.length
        //console.log(turn,n)
        n++
        
        
    }
    let answer = numbers[turn]
    return answer;
}