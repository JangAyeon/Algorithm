function solution(numbers) {
    numbers.sort((a,b)=>b-a)
    // console.log(numbers)
    let answer = numbers[0]*numbers[1]
    return answer;
}