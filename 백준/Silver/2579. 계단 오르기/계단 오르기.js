const readline = require("readline")
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

const lines = []


rl.on("line", line=>lines.push(line)).on("close",()=>{
    const T = +lines[0]
    const arr = [0,...lines.slice(1).map(Number)]
    const dp = Array.from({length:T+1}).fill(0)
    // console.log(arr, dp)


    for(let i=1;i<=T;i++){
        if(i==1){dp[1]=arr[1]}
        else if(i==2){dp[2] = arr[1]+arr[2]}
        else{
            dp[i] = Math.max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3])
        }
        
    }
 
    console.log(dp.pop())



})