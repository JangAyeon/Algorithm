const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []
rl.on("line", line => lines.push(line)).on("close", () => {

    const N = +lines[0]
    const arr = lines.slice(1).map((item)=>item.split(" ").map(Number))
    arr.sort((a,b)=>(a[1]-b[1]||a[0]-b[0]))
    let answer = 0
    let end = -1
    for(let e of arr){
        if(e[0]>=end){
            answer++
            end = e[1]
        }
    }
    
    // console.log(arr)
    console.log(answer)

})