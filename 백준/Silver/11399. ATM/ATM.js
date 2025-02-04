const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


const lines = []



rl.on("line", (line) => {
    lines.push(line.trim())
}).on("close", () => {
    const N = Number(lines[0])
    const arr = lines[1].split(" ").map(Number)
    arr.sort((a, b) => a - b)
    arr.unshift(0)
    for (let i = 1; i < arr.length; i++) {


        arr[i] += arr[i - 1]
    }
    const answer = arr.reduce((acc, curr) => (acc += curr), 0)

    console.log(answer)

})