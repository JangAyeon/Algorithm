function solution(n)
{
    let answer = 0
    while(n!=0){
        if(n%2==1){answer+=1}
        n=Math.floor(n/2)
        // console.log(answer, n)
    }

    return answer;
}