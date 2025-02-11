const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})



const lines = []




rl.on("line", (line) => {
    lines.push(line.trim())
}).on("close", () => {
    const T = +lines[0]
    const N = +lines[1]
    const a = lines[2].split(' ').map(Number)
    const K = +lines[3]
    const b = lines[4].split(' ').map(Number)

    let answer = 0;

    let A = new Map();
    for (let i = 0; i < N; i++) {
        let sum = 0;
        for (let j = i; j < N; j++) {
            sum += a[j]
            A.set(sum, (A.get(sum) ?? 0) + 1)
        }
    }

    for (let i = 0; i < K; i++) {
        let sum = 0;
        for (let j = i; j < K; j++) {
            sum += b[j];
            answer += A.get(T - sum) ?? 0;
        }
    }

    console.log(answer)

})