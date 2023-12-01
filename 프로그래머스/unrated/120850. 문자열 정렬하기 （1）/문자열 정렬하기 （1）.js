function solution(my_string) {
    const string = [...my_string]
    let numbers = []
    for(let a of string){
        if (!isNaN(a)){
            numbers.push(a)
        }
    }
    numbers = numbers.map(Number)
    numbers.sort((a,b)=>a-b)
    // console.log(numbers)
    return numbers;
}