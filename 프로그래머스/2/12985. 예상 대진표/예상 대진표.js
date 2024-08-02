function solution(n,a,b)
{
    let answer = 0;
    for(let i=2;i<n+1;i*=2){
        answer+=1
        //console.log(Math.ceil(a/i),Math.ceil(b/i))
        if(Math.ceil(a/i)===Math.ceil(b/i)){
            break
        }
    }



    return answer;
}