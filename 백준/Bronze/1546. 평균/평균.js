const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout

})

const input = []

rl.on("line", line => input.push(line)).on("close", () => {
    const N = +input[0]
    const arr = input[1].split(" ").map(Number)
    const total = arr.reduce((acc, item)=>acc+item, 0)
    const M = Math.max(...arr)
    const answer = total/M*100/N
    console.log(answer)
})