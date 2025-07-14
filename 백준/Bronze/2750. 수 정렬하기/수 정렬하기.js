const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


const input = []
rl.on("line",line=> input.push(line)).on("close", () => {
    const [N, ...res] = input.map(Number)
    res.sort((a,b)=>a-b)
    const answer = res.join('\n')
    console.log(answer)
})