const readline = require("readline")
const rl = readline.createInterface({
input:process.stdin,
output:process.stdout

})

const lines = []

rl.on(("line"),(line)=>{
lines.push(line.trim())


}).on(("close"),()=>{
const [N,K] = lines[0].split(" ").map(Number)
const arr = lines[1].split(" ").map(Number)
let sum_ = arr.slice(0,K).reduce((acc, curr)=>(
    acc+=curr
),0)
let answer = sum_
let start = 0
let end = K-1
while(end+1<arr.length){
    end+=1
    sum_ = sum_-arr[start]+arr[end]
    //console.log("빼기:" ,arr[start], "더하기: ",arr[end],"총합", sum_)
    start+=1
    answer = Math.max(answer, sum_)
    
}
console.log(answer)
})