const readline = require("readline")
const rl = readline.createInterface({

input:process.stdin,
output:process.stdout

})


const lines = []
rl.on("line", line=>lines.push(line)).on("close", ()=>{

const N = +lines[0]
const arr = [0,...lines.slice(1).map(Number)]
const dp = Array.from({length:N+1}).fill(0)


for(let i=1;i<=N;i++){

    if(i==1){dp[1] = arr[1]}
    else if(i==2){dp[2] = arr[1]+arr[2]}
    else{
            dp[i]=Math.max(dp[i-1], arr[i]+arr[i-1]+dp[i-3], arr[i]+dp[i-2])
    }

}

console.log(Math.max(...dp))
})