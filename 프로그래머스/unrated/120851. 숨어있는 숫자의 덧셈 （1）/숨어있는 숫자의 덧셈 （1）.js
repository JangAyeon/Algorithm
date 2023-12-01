function solution(my_string) {
    const arr = [...my_string]
    let numbers = []
    for(let a of arr){
        if(!isNaN(a)){
         numbers.push(a)   
        }
    }
    numbers = numbers.map(Number)
    let total = numbers.reduce((curr,res)=>curr+res,0)
    return total;
}