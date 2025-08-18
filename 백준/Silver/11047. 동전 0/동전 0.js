const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []
rl.on("line", line => lines.push(line)).on("close", () => {
    let [N ,M]= lines[0].split(" ").map(Number)
    const arr = lines.slice(1).map(Number).sort((a,b)=>b-a)
    let answer = 0
    for(let e of arr){
        const k = Math.floor(M/e)
        M -= e * k
        answer+=k
        // console.log(k, M, answer)
    }

    console.log(answer)

})