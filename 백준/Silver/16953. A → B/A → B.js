const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split(" ").map(Number)


const start = input[0]
const N = input[1]
let answer = -1



function dfs(count, num){
    //console.log(count, num)
    if (num>N){
        return
    }
    else if(num==N){
        answer = count+1
        return
    }
    dfs(count+1, Number(`${num}1`))
    dfs(count+1, num*2)
}

dfs(0, start)
console.log(answer)