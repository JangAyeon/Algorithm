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
    const [n, m] = lines[0].split(" ").map(Number)
    const arr = lines.slice(1).map((r) => Number(r))
    arr.sort((a, b) => -a + b)
    //console.log(n, m, arr)
    let a = m
    let answer = 0
    for (let q of arr) {
        const k = parseInt(a / q)
        a -= q * k
        //console.log(q, a, k)
        answer += k

        if (a <= 0) {
            break
        }

    }
    console.log(answer)


})