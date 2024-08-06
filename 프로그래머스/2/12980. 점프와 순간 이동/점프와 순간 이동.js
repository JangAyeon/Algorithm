function solution(n)
{
// n.toString(2) : 2진수 만들기
    const arr = n.toString(2).split("").map(Number)
    const answer = arr.reduce((e, temp)=>(temp+e),0)
    return answer;
}