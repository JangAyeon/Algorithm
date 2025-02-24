const readline = require("readline")
const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout
})

const lines = []

rl.on("line", (line) => {
    lines.push(line.trim())
}).on("close", () => {

    const [N, K] = lines[0].split(" ").map(Number)
    const arr = lines[1].split("")
    //console.log("close", lines, arr, N, K)
    let p1 = 0
    let p2 = 1
    let answer = []
    const hams = []
    for (let i = 0; i < N; i++) {
        if (arr[i] === "P") {
            for (let j = i - K; j <= i + K; j++) {

                if (j < 0 || j > N) {
                    continue
                }
                //console.log(i, j)
                if (arr[j] === "H") {

                    answer.push([j, i])
                    arr[j] = "0"
                    arr[i] = "0"
                    break
                }

            }
        }

    }
    console.log(answer.length)
})