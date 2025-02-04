const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []


rl.on("line", (line) => {
    const s = line.trim()
    lines.push(s)

}).on("close", () => {
const N = Number(lines[0])
const arr = lines.slice(1).map(Number) // 난이도 순으로 배치
let answer = 0
//'console.log(arr)
    for(let i = N-1;i>0;i--){
        if(arr[i]<=arr[i-1]){
            const gap = arr[i-1]-arr[i]+1
            arr[i-1]-=gap
            answer+=gap
            //console.log(arr, gap, answer)
            
        }
    }

    console.log(answer)






    
})