const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout

})

const lines = []

rl.on("line", (line) => {

    lines.push(line.trim())
}).on("close", () => {
    let [N, K] = lines[0].split(" ").map(Number)
    const minBall = 0.5 * (1 + K) * K
    let answer
    if (N < minBall) {
        answer = -1
    } else {
        N -= minBall
        if (N % K === 0) {
            answer = K - 1
        } else {
            answer = K
        }
    }
    console.log(answer)

})