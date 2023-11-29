function solution(numbers, direction) {
    if(direction==="right"){
        let x = numbers.pop()
        numbers.unshift(x)
    }
    else{
        let x = numbers.shift()
        numbers.push(x)
    }
    
    return numbers;
}