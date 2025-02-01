const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []

rl.on(("line"), (line) => {
    lines.push(line.trim())
}).on(("close"), () => {
    const [N, M] = lines[0].split(" ").map(Number)
    const arr = lines[1].split(" ").map(Number)
    let start = 0
    let end = M - 1
    let sum_ = arr.slice(0, end + 1).reduce((acc, curr) => (acc += curr), 0)
    let answer = sum_
    while (end + 1 < N) {
        end += 1
        sum_ = sum_ - arr[start] + arr[end]
        start += 1
        answer = Math.max(answer, sum_)
    }
    console.log(answer)

})